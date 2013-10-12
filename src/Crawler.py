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
from grabber import Grabber
from arg_parse import ArgParse
from linked_list import LinkedList
## ------- Package Imports ------ ##


class Crawler(ArgParse, LinkedList):
    def __init__(self):
        """."""
        self.count_parsed_url = 0

    def __call__(self):
        """."""
        options = ArgParse().parse()
        grabber_obj = Grabber()

        url_list = []

        ll_obj = LinkedList(options.url)

        ## Start Looping here...
        if self.count_parsed_url >= options.limit:
            pass

        _url_list = grabber_obj(options.url)

        ll_obj.insert(_url_list)

        ll_obj.show_list()

        url_list.extend(_url_list)

        self.count_parsed_url += len(url_list)
        print self.count_parsed_url

if __name__ == "__main__":
    """First Block of statement."""
    Crawler()()

