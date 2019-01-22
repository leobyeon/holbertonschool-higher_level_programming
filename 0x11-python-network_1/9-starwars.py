#!/usr/bin/python3
# takes in a string and sends a search req to the Star Wars API
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(
            'https://swapi.co/api/people/?search={}'.format(argv[1]))
    res = r.json()
    count = res['count']
    print("Number of results: {}".format(count))
    for name in res['results']:
        print(name['name'])
