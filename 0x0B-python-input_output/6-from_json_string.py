#!/usr/bin/python3
import json
def from_json_string(my_str):
    """returns a Python object represented by a JSON str"""
    return json.loads(my_str)
