#!/usr/bin/python3

import sys

save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == '__main__':

    try:
        obj_from_json = load_file("add_item.json")

    except:
        obj_from_json = []

    for i in range(1, len(sys.argv)):
        obj_from_json.append(sys.argv[i])
    save_file(obj_from_json, "add_item.json")
