__author__ = 'asmith'

dataframe = "Main map"
papersize = "A3"
"""
Doesn't include the maXXX map number specific directory)
"""

pdf_resolution = 300
pdf_quality = u'NORMAL'  # BEST, BETTER, NORMAL, FASTER, FASTEST
pdf_jpeg_compression_quality = 80

jpeg_width = 4761
jpeg_hieght = 3369
jpeg_resolution = 300
jpeg_quality = 80

tmbnail_width = 20
tmbnail_hieght = 20
tmbnail_resolution = 15
tmbnail_jpeg_quality = 80


# hri => HumanitarianResponse.Info
# hri_dropbox_url = r"https://www.dropbox.com/sh/emnz6zkrki0d2rx/AACEUSyacvRGDSCH5ZBBJLSza?dl=0"
hri_dropbox_url = r"DROP_BOX_URL"
hri_dropbox_local_path = r"Z:\foxtrot\2015-04-25-Nepal\Dropbox\HR_info_to_publish"
"""
https://www.dropbox.com/sh/emnz6zkrki0d2rx/AABHeQwrOGOsGsISEqqiwa9Ra/MA023?lst=#lh:null-ma029_npl_eq_USAR_district_sectors_v3_Dhading.jpg
https://www.dropbox.com/sh/emnz6zkrki0d2rx/AABHeQwrOGOsGsISEqqiwa9Ra/MA023?lst
https://www.dropbox.com/sh/emnz6zkrki0d2rx/AABHeQwrOGOsGsISEqqiwa9Ra/MA023?lst
https://dl.dropboxusercontent.com/sh/emnz6zkrki0d2rx/AADj3ww7DRQfi8m-gSK0JcYYa/MA023/ma029_npl_eq_USAR_district_sectors_v3_Dhading.jpg
https://dl.dropboxusercontent.com/sh/emnz6zkrki0d2rx/AADj3ww7DRQfi8m-gSK0JcYYa/MA023/ma029_npl_eq_USAR_district_sectors_v3_Dhading.jpg
https://dl.dropboxusercontent.com/sh/emnz6zkrki0d2rx/AADj3ww7DRQfi8m-gSK0JcYYa/MA023/ma029_npl_eq_USAR_district_sectors_v3_Gorkha.jpg
https://api-content.dropbox.com/1/files/auto/MA023/ma029_npl_eq_USAR_district_sectors_v3_Gorkha.jpg
"""

hri_emergencies = "Nepal: Earthquake - Apr 2015"

output_dir = r"D:\work\custom-software-group\code\github\mapbook-metadata\testoutput"
# output_dir = hri_dropbox_local_path

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
