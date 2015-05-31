#-------------------------------------------------------------------------------
# Name:        mapbook-metadata
# Purpose:     Export "Map Book" i.e a Single or Multipage MXD to PDF and upload 
#              to MapAction website.
#
# Owner:      MapAction
# Contributors: Matthew Lewis, Andy Smith
#
# Created:     29/05/2015
# Updated:     29/05/2015
#
# Version:     1.2
# Version Notes 1.1: Intial draft create by andy
# Version Notes 1.2: drafting structure
#
# Copyright:   by permison of Map Action
# Licence:     GPL
#-------------------------------------------------------------------------------

# Inbuilt Modules

import arcpy # ArcGIS
import logging # Logging module

# Custom Modules


# Custom Exception Class

""" A custom map book exception for specifc errors """
class MapBookException(Exception):
    pass


# MapBook Class

class  MapBook:

    def __init__(self):
        '''***************************************************************
        @description: Constructor function to set initial variables 
                      for class

        @params
            self: the MapBook class instance.

        @return
        ******************************************************************'''
        
        self.logger = self.initiate_logger()
        pass

    # end def


    def initiate_logger(self):

        '''***************************************************************
            @description: A function that builders a log for this class.

            @params
                self: the MapBook class instance.

            @return
                a logger object to be used with the MapBook instance.

        ******************************************************************'''

        ## Todo: Add unique ID to logger
        ##       Set local file for logs
        ##       initiate raise in exception
        ##       include tracebacks

        try:
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)

            # create a file handler

            handler = logging.FileHandler('logs.log')
            handler.setLevel(logging.DEBUG)

            # create a logging format

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            # add the handlers to the logger

            logger.addHandler(handler)
        
            logger.info('Logger Intialised')

        except Exception as e:
            MapBookException(e.message)
            pass

    # end def

    

    def run_export(self,params):

        '''***************************************************************
        @description: Constructor function to set initial variables 
                      for class

        @params


        @return


        ******************************************************************'''



        pass

    # end def

    def export_data_driven_pages(self,mxd, rootfilename, map_theme, hri_theme, 
                                 export_path, ma_web_csv_writer, hri_csv_writer,
                                 cluster):
        '''***************************************************************
        @description: Constructor function to set initial variables 
                      for class

        @params


        @return


        ******************************************************************'''

        
        pass
    
    # end def

    
    def export_single_page(self,mxd, rootfilename, location, map_theme, hri_theme,
                           export_path, ma_web_csv_writer, hri_csv_writer, cluster,
                           first_page=True):

        '''***************************************************************
        @description: Constructor function to set initial variables 
                      for class

        @params


        @return


        ******************************************************************'''


        pass
    # end def

    


    def remove_newline_char(self,some_text):

        '''***************************************************************
        @description: Constructor function to set initial variables 
                      for class

        @params


        @return


        ******************************************************************'''

        pass
   
    # end def

   

    def export_kiosk_metadata(self,mxd):

        '''***************************************************************
        @description: Constructor function to set initial variables 
                      for class

        @params


        @return


        ******************************************************************'''
        
        pass

    # end def




    def export_mapaction_website_metadata(self,mxd, jpgfilename, pdffilename, 
                                          location, map_theme):

        '''***************************************************************
        @description: Constructor function to set initial variables 
                      for class

        @params


        @return


        ******************************************************************'''

        pass

    # end def

     
    def export_hr_info_metadata(self,mxd, location, map_theme, hri_theme, coord_hub,
                                pdf_full_path, cluster, thumbnail):

        '''***************************************************************
        @description: A function that

        @params


        @return


        ******************************************************************'''

        pass

    # end def
    

    def get_mxd(self,mxdfile):

        '''***************************************************************
        @description: A function that allocates an MXD as either a
                    current mxd object or a file location. If no object
                    is found an error is returned

        @params
            self: the MapBook class instance.
            mxdfile: the location to the MXD file on disk.

        @return
            An arcpy MapDocument Object. 

        ******************************************************************'''

        # Check for file or current MXD. if not return error

        try:
            if mxdfile is None:
                return arcpy.mapping.MapDocument("current")
            else:
                return arcpy.mapping.MapDocument(mxdfile)
        except:
            return

    # end def


if __name__ == '__main__':
    pass