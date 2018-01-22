#!/usr/bin/env python

# https://linuxacademy.com/cp/exercises/view/id/652/module/158

# Receive a file_name and line_number as command line parameters

# Print the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line

## Error Cases ##
# File doesn't exist
# File doesn't contain the line_number specified

import sys

file_name = sys.argv[1]
line_number = int(sys.argv[2]) - 1

try:
    with open(file_name, 'r') as reading_file:
        line_list = list(reading_file)
        try:
            print(line_list[line_number])
        except IndexError:
            print("That line is outside the index")
except IOError:
    print("That file don't exist")


