__author__ = 'asmith'

"""
Simple low-tech script to export mapbooks
"""
import arcpy
import os
import sys
import settings
import datetime
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)


def run_export(args):
    mxd = get_mxd(args[0])
    logging.info("mxd name = {}".format(mxd.filePath))
    filepath, filename = os.path.split(mxd.filePath)
    rootfilename = os.path.splitext(filename)[0]

    if mxd.isDDPEnabled:
        export_data_driven_pages(mxd, rootfilename)
    else:
        export_single_page(mxd, rootfilename, None)


def export_data_driven_pages(mxd, rootfilename):

    for pageNum in range(mxd.dataDrivenPages.pageCount):

        logging.info("DDP export page number {}".format(pageNum))
        mxd.dataDrivenPages.currentPageID = pageNum + 1
        # filepath = sys.argv[2]
        page_name = mxd.dataDrivenPages.pageRow.getValue(mxd.dataDrivenPages.pageNameField.name)
        pagefilename = "{}_{}".format(rootfilename, page_name)
        export_single_page(mxd, pagefilename, page_name)


def export_single_page(mxd, rootfilename, location):
    export_path = settings.output_dir

    pdf_name = os.path.join(export_path, "{}.pdf".format(rootfilename))
    jpeg_name = os.path.join(export_path, "{}.jpeg".format(rootfilename))
    thumbnail_filename = os.path.join(export_path, "{}_thumbnail.jpeg".format(rootfilename))
    logging.info("PDF filename {}".format(pdf_name))
    logging.info("Jpeg filename {}".format(jpeg_name))
    logging.info("thumbnail filename {}".format(thumbnail_filename))

    # PDF
    logging.info("Started exporting PDF")
    arcpy.mapping.ExportToPDF(mxd, pdf_name, data_frame='page_layout', embed_fonts=True,
                              resolution=settings.pdf_resolution,
                              image_quality=settings.pdf_quality,
                              jpeg_compression_quality=settings.pdf_jpeg_compression_quality)
    logging.info("Completed exporting PDF")

    # JPEG
    logging.info("Started exporting JPEG")
    arcpy.mapping.ExportToJPEG(mxd, jpeg_name, data_frame='page_layout',
                               df_export_height=settings.jpeg_hieght,
                               df_export_width=settings.jpeg_width,
                               resolution=settings.jpeg_resolution,
                               jpeg_quality=settings.jpeg_quality)
    logging.info("Completed exporting JPEG")

    # thumbnail
    logging.info("Started exporting Thumbnail")
    arcpy.mapping.ExportToJPEG(mxd, thumbnail_filename, data_frame='page_layout',
                               df_export_height=settings.tmbnail_hieght,
                               df_export_width=settings.tmbnail_width,
                               resolution=settings.tmbnail_resolution,
                               jpeg_quality=settings.tmbnail_jpeg_quality)
    logging.info("Completed exporting Thumbnail")

    metadata = export_mapaction_website_metadata(mxd, jpeg_name, pdf_name)
    for key, value in metadata.iteritems():
        print "key = {}\t value = {}".format(key, value)

    # return pdf_filename, thumbnail_filename


def remove_newline_char(str):
    return str


def export_kiosk_metadata(mxd):
    """
    values = {}
    values["title"] = pdf_name
    values["type"] = "PDF"
    values["snippet"] = snippet
    values["description"] = description
    values["tags"] = tags
    values["extent"] = extent_string
    values["spatialReference"] = spatial_reference_from_datafram(mxd)
    values["accessInformation"] = access_info
    values["licenseInfo"] = license_info
    values["culture"] = culture
    return values
    """
    pass

def export_mapaction_website_metadata(mxd, jpgfilename, pdffilename, location, theme):
    values = {}
    values["operationID"] = settings.maw_operational_id
    values["sourceorg"] = "MapAction"
    values["title"] = remove_newline_char(arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "title")[0].text)
    values["ref"] = os.path.splitext(os.path.split(mxd.filePath)[1])[0]
    values["language"] = "English"
    values["countries"] = "NEPAL"
    values["createdate"] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    values["createtime"] = str(datetime.datetime.now().strftime('%H:%M'))
    values["status"] = "New"

    values["xmax"] = arcpy.mapping.ListDataFrames(mxd, "Main map")[0].extent.XMax
    values["xmin"] = arcpy.mapping.ListDataFrames(mxd, "Main map")[0].extent.XMin
    values["ymax"] = arcpy.mapping.ListDataFrames(mxd, "Main map")[0].extent.YMax
    values["ymin"] = arcpy.mapping.ListDataFrames(mxd, "Main map")[0].extent.YMin
    values["proj"] = arcpy.mapping.ListDataFrames(mxd, settings.dataframe)[0].spatialReference.name
    values["datum"] = arcpy.mapping.ListDataFrames(mxd, settings.dataframe)[0].spatialReference.datumName
    values["jpgfilename"] = jpgfilename
    values["pdffilename"] = pdffilename
    values["qclevel"] = settings.maw_qclevel
    values["qcname"] = settings.maw_qcname
    values["access"] = settings.maw_access
    values["glideno"] = settings.glideno
    values["summary"] = remove_newline_char(arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "summary")[0].text)

    values["pdfresolutiondpi"] = settings.pdf_resolution
    values["mxdfilename"] =  os.path.split(mxd.filePath)[1]
    values["paperxmax"] = ""
    values["paperxmin"] = ""
    values["paperymin"] = ""
    values["paperxmax"] = ""
    values["kmzfilename"] = ""
    values["accessnotes"] = ""
    values["imagerydate"] = ""
    values["datasource"] = remove_newline_char(arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "data_sources")[0].text)
    if location is None:
        values["location"] = values["countries"]
    else:
        values["location"] = location

    values["scale"] = remove_newline_char(arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "scale")[0].text)
    values["papersize"] = settings.papersize
    values["jpgresolutiondpi"] = settings.jpgresolutiondpi

    values["jpgfilesize"] = 0
    values["pdffilesize"] = 0
    values["theme"] = theme

    return values


def export_hr_info_metadata():
    pass


def get_mxd(mxdfile):
    if mxdfile is None:
        return arcpy.mapping.MapDocument("current")
    else:
        return arcpy.mapping.MapDocument(sys.argv[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Exports MXDs to PDFs, MXDs and thumbnails. It also exports a CSV metadata file with various map'
                    'metadata fields. Handles Data Driven Pages by exporting a individual file per page'
    )
    parser.add_argument('MXD_file')  # positional, rather than option.
    parser.add_argument('-t', '--theme', default='Reference')
    args = parser.parse_args()
    run_export(args)