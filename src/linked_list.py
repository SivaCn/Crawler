#! /usr/bin/python

###############################################################################
##
##
##
###############################################################################

"""

"""

__all__ = ['LinkedList']

__author__ = r"SivaCn (http://www.cnsiva.com)"
__email__ = r"cnsiva.in@gmail.com"

## ------- Built-in Imports ------ ##
## ------- Built-in Imports ------ ##

## ------- Package Imports ------ ##
## ------- Package Imports ------ ##


class Node(object):
    """Referential Structure used to create new nodes"""
    def __init__(self, data):
        """Constructor."""
        self.data = data
        self.next = None


class Meta(object):
    """A meta class contains info about the List at any
    moment.
    """
    def __init__(self):
        """Constructor."""
        self.count = 0
        self.start = None
        self.end = None


class LinkedList(object):
    """."""
    def __init__(self, start):
        """Constructor."""
        self.list = Meta()
        _start = Node(start)
        self.list.start = _start
        self.list.end = _start
        self.count += 1

    def insert(self, data):
        """Insert a new node at the end of the List.
        """
        if not isinstance(data, list):
            data = [data]

        for data_item in data:
            _temp = Node(data_item)

            walker = self.list.start
            while walker:
                if walker.next:
                    walker = walker.next
                else:
                    break

            walker.next = _temp
            self.list.end = walker.next
            self.count += 1

    def show_list(self):
        """Display the List as it traverses START -> END."""
        walker = self.list.start

        while walker:
            print walker.data, "items"
            walker = walker.next


if __name__ == "__main__":
    """This is the first block of Statements to be executed."""
    pass

