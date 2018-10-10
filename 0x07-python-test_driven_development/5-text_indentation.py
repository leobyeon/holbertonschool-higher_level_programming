#!/usr/bin/python3
def text_indentation(text):
    """indents text string by .:?"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i, x in enumerate(text):
        if x in ".:?":
            print("{}\n".format(text[:i + 1].lstrip()))
            text_indentation(text[i + 1:])
            return
        print("{}".format(text.lstrip()), end='')

