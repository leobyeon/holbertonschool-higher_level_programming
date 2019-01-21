#!/usr/bin/python3
# takes in URL and email, sends POST request,
# and displays the body of response
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))
