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
        options = ArgParse().parse()

        self.start_url = options.url
        self.limit = int(options.limit)
        self.processed_url = []

    def __call__(self):
        """."""
        grabber_obj = Grabber()

        linked_list_obj = LinkedList(self.start_url)

        _url_list = grabber_obj(self.start_url)

        linked_list_obj.insert(_url_list)
        
        walker = linked_list_obj.list.start

        while walker:
            if linked_list_obj.list.count <= self.limit:
                _url_list = grabber_obj(options.url)
                _url_list = [ele for ele in _url_list \
                             if ele not in self.processed_url]

                linked_list_obj.insert(_url_list)

            walker = walker.next

        linked_list_obj.show_list(self.limit)


if __name__ == "__main__":
    """First Block of statement."""
    Crawler()()

