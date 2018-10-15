#!/usr/bin/python3
class MyList(list):
    """MyList class that inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
