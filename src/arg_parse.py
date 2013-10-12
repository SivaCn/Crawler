#! /usr/bin/python

###############################################################################
##
##
##
###############################################################################

"""

"""

__all__ = ['ArgParse']

__author__ = r"SivaCn (http://www.cnsiva.com)"
__email__ = r"cnsiva.in@gmail.com"

## ------- Built-in Imports ------ ##
from defaults import *
from optparse import OptionParser
## ------- Built-in Imports ------ ##

## ------- Package Imports ------ ##
## ------- Package Imports ------ ##


class ArgParse(object):
    """."""
    def __init__(self):
        """."""
        pass

    def parse(self):
        """."""
        parser = OptionParser()
        parser.add_option("-u", "--url", dest="url",
                          help="Url to start crawl with")
        parser.add_option("-l", "--limit", dest="limit",
                          help="Limit number of url to crawl")

        options, args = parser.parse_args()
        return options

if __name__ == "__main__":
    """First Block of statement."""
    pass
