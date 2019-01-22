#!/usr/bin/python3
# takes in URL, sends request, and displays body of response
import requests
from sys import argv


if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
