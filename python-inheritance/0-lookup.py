#!/usr/bin/python3
"""returns the list of available attributes"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes and
        methods of the object.
    """
    return dir(obj)
