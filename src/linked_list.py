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
    def __init__(self, data, number=None):
        """Constructor."""
        self.data = data
        self.next = None
        self.index_number = number


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
        _start = Node(start, 0)
        self.list.start = _start
        self.list.end = _start
        self.list.count += 1

    def insert(self, data):
        """Insert a new node at the end of the List.
        """
        if not isinstance(data, list):
            data = [data]

        for data_item in data:
            _temp = Node(data_item, self.list.count)

            walker = self.list.start

            insert_flag = True

            while walker:
                ## Skip if the list already has the element.            
                if walker.data == data_item:
                    insert_flag = False
                    break
                
                if walker.next:
                    walker = walker.next
                else:
                    break

            if insert_flag:
                walker.next = _temp
                self.list.end = walker.next
                self.list.count += 1

    def show_list(self, limit=None):
        """Display the List as it traverses START -> END."""
        walker = self.list.start

        stop_at = "END"

        if limit:
            stop_at = limit - 1

        while walker:
            print """{})\t{}""".format(walker.index_number + 1, walker.data)

            if walker.index_number >= stop_at:
                break

            walker = walker.next

if __name__ == "__main__":
    """This is the first block of Statements to be executed."""
    pass

