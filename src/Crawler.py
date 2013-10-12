#! /usr/bin/python

###############################################################################
##
##
##
###############################################################################

"""

"""

__all__ = ['Crawler']

__author__ = r"SivaCn (http://www.cnsiva.com)"
__email__ = r"cnsiva.in@gmail.com"

## ------- Built-in Imports ------ ##
from defaults import *
## ------- Built-in Imports ------ ##

## ------- Package Imports ------ ##
from arg_parse import ArgParse
## ------- Package Imports ------ ##


class Crawler(ArgParse):
    def __init__(self):
        """."""
        pass

    def __call__(self):
        """."""
        options = ArgParse().parse()
        print options.url
        print options.limit

if __name__ == "__main__":
    """First Block of statement."""
    Crawler()()
