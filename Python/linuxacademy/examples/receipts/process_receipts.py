#!/usr/bin/env python

import glob
import os
import shutil
import json
import re
import math

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
#receipts = glob.glob('./new/receipt-[0-9]*.json')

# Use a list comprenesion
receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') 
        if re.match('./new/receipt-[0-9]*[02468].json', f)]

subtotal = 0.0

# Iterate over the receipts
    # read content and tally a subtotal
    # mv the file to the processed directory
    # print that we processed the file
for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # Create the location + filename to which the file will be moved 
    destination = path.replace('new', "processed")
    # Move the file
    shutil.move(path, destination)
    print("Moved '%s' to '%s'" % (path, destination))

# Print the subtotal of all processed receipts
print("Receipt subtotal: $%s" % round(subtotal, 2))
