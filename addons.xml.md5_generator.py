""" addons.xml generator """

import re
import os
import md5
import StringIO

class Generator:
    """
        Generates a new addons.xml.md5 hash file. Must be run from the root of
        the checked-out repo. Only handles single depth folder structure.
    """
    def __init__( self ):
        # generate files
        self._generate_md5_file()
        # notify user
        print "Finished updating md5 file"

    def _generate_md5_file( self ):
        try:
            # create a new md5 hash
            m = md5.new( open( "addons.xml" ).read() ).hexdigest()
            # save file
            self._save_file( m, file="addons.xml.md5" )
        except Exception, e:
            # oops
            print "An error occurred creating addons.xml.md5 file!\n%s" % ( e, )

    def _save_file( self, data, file ):
        try:
            # write data to the file
            open( file, "w" ).write( data )
        except Exception, e:
            # oops
            print "An error occurred saving %s file!\n%s" % ( file, e, )


if ( __name__ == "__main__" ):
    # start
    Generator()