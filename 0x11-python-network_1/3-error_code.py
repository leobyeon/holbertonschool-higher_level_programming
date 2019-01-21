#!/usr/bin/python3
# takes in URL, sends a request, and displays body
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        data = urllib.request.urlopen(req)
        print(data.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
