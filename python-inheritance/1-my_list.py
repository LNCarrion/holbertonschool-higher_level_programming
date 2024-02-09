#!/usr/bin/python3
"""
This module defines the class my_List.
"""


class MyList(list):
    """creating a my list class"""

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
