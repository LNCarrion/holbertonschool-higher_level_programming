#!/usr/bin/python3
"""check if an object is an instance"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of,
    or is derived from, a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of, or is derived from,
        the specified class.
        False otherwise.
    """

    return isinstance(obj, a_class)
