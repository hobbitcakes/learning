#!/usr/bin/env python

import os

# https://linuxacademy.com/cp/exercises/view/id/649/module/158

# Prompt the user for a message to echo
message = str(raw_input("What is your message?\n"))

# Prompt the user fo rthe nubmer of times to repeat the message. If no response is given, then count sould default to 1
count = int(raw_input("How many times should we echo this message?\n"))

if count is None:
    count = 1

#Defines a function that takes a message and count, then prints the message that many times
def echo(message, count):
    for iterations in range(0, count):
        print(message)

echo(message, count)
