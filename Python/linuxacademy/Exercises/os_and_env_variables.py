#!/usr/bin/env python

import os
import math

# https://linuxacademy.com/cp/exercises/view/id/650/module/158

# Print the first ten digits of Pi to the screen

# Accpet an optional environment variable called DIGITS. If present, the script will print that many digits of Pi instead of 10.

digits = int((os.getenv("DIGITS") or 10))

pie = math.pi

print("%.*f" % (digits, math.pi))
