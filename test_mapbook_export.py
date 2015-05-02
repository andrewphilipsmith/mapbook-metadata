__author__ = 'asmith'

import unittest
import arcpy

class TestMapBookExport(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_are_ddp_enabled():
        mxd = arcpy.mapping.MapDocument(r"Z:\foxtrot\2015-04-25-Nepal\GIS\3_Mapping\33_MXD_Maps\ma029-mapbookexporttest\ma029_npl_eq_USAR_district_sectors_v2.mxd")
        self.assertTrue()


"""
>>> print mxd.dataDrivenPages.pageNameField.name
DISTRICT


print mxd.dataDrivenPages.currentPageID

for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
    print elm.text


# HR.info headings
Title               <title>
Title:en            <title>
Title:fr            Should we repeat the English title, or just leave blank
Title:es            Should we repeat the English title, or just leave blank
Type                ??? does this refer to Map/Report/Infographic etc. if not something else?
Description         <summary>
Description         ??? Why twice, is there something missing?
File                presumably just the filename?
Language            "English"
Sectors             ??? See below
Clusters/Sectors    ??? See below
Publication Date    <datefield>
Organization        "MapAction"
Coordination hubs   ??? Would we put something like "OSOCC KTM"
Locations           Is this the locations the map refer to?
Fundings            probably not relevant for us?
Themes              ??? See below
Disasters           Just "Nepal Earthquake 2015", or glide number of something else?
Spaces              ??? What is this? Should this be "Nepal"
Post date           ??? Date posted to HR.info? Do we supply this or is this calculated automatically
Author              Always "MapAction"
Path                ??? relative to dropbox root? Does it need to include the filename aswell?

http://www.humanitarianresponse.info/en/help/importing-visuals-mapsinfographics-hrinfo
Title 	            The actual human readable title of the map
Type 	            Reference, Thematic, etc. Note: Use the ‘Map Type’ controlled vocabulary in the site
File 	            The URL of file sitting in the Dropbox folder. Note: remove the www from the URL and put ‘dl’ instead
                    to point to the actual file. Example: dl.dropbpx.com/file_name
Language 	        Language of the file. For English use ‘en’
Publication Date 	Date when the map was published. Use the format, “dd-mmm-yyyy” i.e. “02-Jan-2011”
Thumbnail 	        URL of the thumbnail file for the map. Thumbnail should be png, jpg or gif format. This file for the
                    map should also be available in the same folder where the maps are. Please use the URL
                    ‘dl.dropbox.com’ instead of www.dropbox.com
Source              Full name of the Organization. Note that the organization must be part of the Organization taxonomy
Location            Geographic location where the map belongs to. Please note that the location should already be
                    available in the site ‘Location taxonomy’.
Cluster             Cluster(s) to which the map belongs to. For multiple cluster use ‘;’ e.g. ‘Protection;Emergency
                    Shelter and NFI’ with no space.
Themes              Theme(s) where the person could belongs to. For multiple themes use ‘;’ Example: ‘Age; Early Warning;’
                    with no space.
Coordination Hub 	Full name of the Coordination hub where the map could belong to. This should be already available in
                    the site.
Emergencies 	    Emergency where the person could belong to. For multiple emergencies use ‘;’ Example:
                    ‘Cholera;Floods 2010’ with no space.




Is there a naming convention for the thumbnails (relative to the main file) or is this specified somewhere else?
Are the


"""
