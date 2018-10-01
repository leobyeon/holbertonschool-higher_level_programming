#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError()
    except:
        print("C is fun")
        raise
