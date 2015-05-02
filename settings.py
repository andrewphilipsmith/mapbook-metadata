__author__ = 'asmith'

dataframe = "Main map"
papersize = "A3"
output_dir = r"D:\work\custom-software-group\code\github\mapbook-metadata\testoutput"

pdf_resolution = 300
pdf_quality = u'NORMAL'  # BEST, BETTER, NORMAL, FASTER, FASTEST
pdf_jpeg_compression_quality = 80

jpeg_width = 4761
jpeg_hieght = 3369
jpeg_resolution = 300
jpeg_quality = 80

tmbnail_width = 20
tmbnail_hieght = 20
tmbnail_resolution = 96
tmbnail_jpeg_quality = 80


# hri => HumanitarianResponse.Info
hri_dropbox_url = ""

# maw => MapAction Website
maw_operational_id = 240
maw_qclevel = "Local"
maw_qcname = ""
maw_access = "Public"
glideno = "EQ-2015-000048-NPL"

# kiosk => Kiosk


"""
    dict["title"] = pdf_name
    dict["type"] = "PDF"
    dict["snippet"] = snippet
    dict["description"] = description
    dict["tags"] = tags
    dict["extent"] = extent_string
    dict["spatialReference"] = spatial_reference_from_datafram(mxd)
    dict["accessInformation"] = access_info
    dict["licenseInfo"] = license_info
    dict["culture"] = culture
"""
