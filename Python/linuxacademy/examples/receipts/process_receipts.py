#!/usr/bin/env python

import glob
import os
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
receipts = glob.glob('./new/receipt-[0-9]*.json')

subtotal = 0.0

# Iterate over the receipts
    # read content and tally a subtotal
    # mv the file to the processed directory
    # print that we processed the file
for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # Get the last element separated by '/'. (the file name)
    name = path.split('/')[-1]
    # Create the location + filename to which the file will be moved 
    destination = "./processed/%s" % name
    # Move the file
    shutil.move(path, destination)
    print("Moved '%s' to '%s'" % (path, destination))

# Print the subtotal of all processed receipts
print("Receipt subtotal: $%.2f" % subtotal)





