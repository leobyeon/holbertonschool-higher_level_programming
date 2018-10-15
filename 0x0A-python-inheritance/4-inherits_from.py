#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class
    that inherited from the specified class
    """
    return isinstance(obj, a_class) and not type(obj) == a_class
