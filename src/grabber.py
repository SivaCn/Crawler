#! /usr/bin/python

###############################################################################
##
##
##
###############################################################################

"""

"""

__all__ = ['Grabber']

__author__ = r"SivaCn (http://www.cnsiva.com)"
__email__ = r"cnsiva.in@gmail.com"

## ------- Built-in Imports ------ ##
import re
import os
import sys
import urllib
import BeautifulSoup
from urlparse import urlparse
## ------- Built-in Imports ------ ##

## ------- Package Imports ------ ##
## ------- Package Imports ------ ##


class Grabber(object):
    """."""
    def __init__(self):
        """."""
        pass

    def __call__(self, url):
        """."""
        url_content = urllib.urlopen(url).read()
        soup = BeautifulSoup.BeautifulSoup(url_content)

        parsed_base_url = urlparse(url)

        all_href = [ele.get('href') for ele in soup.findAll('a')]
        return [self._normalizeUrl(ele, parsed_base_url) for ele in all_href]

    def _normalizeUrl(self, partial_url, parsed_base_url):
        """."""
        parsed = urlparse(partial_url)

        if not parsed.netloc:
            partial_url = u"{}{}{}".format(parsed_base_url.netloc, \
                                                  '', \
                                                  parsed.path.lstrip('../').lstrip('/'))

        return partial_url


if __name__ == "__main__":
    """First Block of statement."""
    pass
