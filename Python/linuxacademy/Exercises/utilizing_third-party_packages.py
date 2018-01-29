#!/usr/bin/env python

# https://linuxacademy.com/cp/exercises/view/id/656/module/158

import requests
from argparse import ArgumentParser

parser = ArgumentParser(description="Tool to output either json or html")
parser.add_argument('url', help='URL to call')
parser.add_argument('--out', help='Output file')
parser.add_argument('--format', help='Format of the output. Either json or html', default='html')

args = parser.parse_args()

url = args.url

response = requests.get(url)

if args.format == 'json':
    response.json()
else:
    response.text
