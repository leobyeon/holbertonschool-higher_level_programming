#!/usr/bin/python3
# takes in a letter and sends a post request
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    val = {'q': q}

    r = requests.post('http://0.0.0.0:5000/search_user', data=val)
    try:
        res = r.json()
        if res:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
