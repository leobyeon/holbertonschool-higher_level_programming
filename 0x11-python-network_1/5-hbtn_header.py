#!/usr/bin/python3
# takes in URL, sends request,
# and displays value of variable 'X-Request-Id'
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
