#!/usr/bin/env python

# https://linuxacademy.com/cp/exercises/view/id/653/module/158

# Take port_number as only argument

# call lsof to determine if there is a process listening on that port
    # If there is, kill the process and inform the user
    # If there is no process, prkint that there was noprocess running on that port

import subprocess
import argparse
import sys

parser = argparse.ArgumentParser(description='Kill any process listening on PORT')
parser.add_argument('--port', help='port to free up')
args = parser.parse_args()

try:
    port_taken = subprocess.check_output(['lsof', '-n', ('-i4TCP:%s' % args.port)], stderr=subprocess.STDOUT)
    proc = port_taken.split()
except subprocess.CalledProcessError:
    print("Process not taken")
    sys.exit(1)
else:
    subprocess.check_output(['kill', '-9', proc[10]])
    print("Killed %s" % proc[1])

