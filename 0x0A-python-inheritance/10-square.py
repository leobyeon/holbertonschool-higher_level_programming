#!/usr/bin/python3
class Square(__import__('9-rectangle').Rectangle):
    """define class square"""

    def __init__(self, size):
        """initialize"""
        super().integer_validator("size", size)
        super().__init__(size, size)
