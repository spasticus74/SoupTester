#! /usr/bin/python

# Simple Soup10 agent example,
# implements the required interface
# Intended as an example/starting point for further development

import getopt, sys, random

version = '0.0.1'
author = "Your Name|your_email@your_domain.com"

random.seed()

actions = ["EAT", "UL", "U", "UR", "L", "R", "DL", "D", "DR"]

# Ignore the input, and move in a random direction
def getMove(environment):
    act = actions[random.randrange(0,9)]
    print act + "|" + actions[random.randrange(0,9)]

# Returns the author string defined above
def getAuthor():
    print author

# Returns the version string defined above
def getVersion():
    print version

# Process the args provided
options, remainder = getopt.getopt(sys.argv[1:], 'avm:', ['author', 'version', 'move=',])

for opt, arg in options:
    if opt in ('-a', '--author'):
        getAuthor()
    elif opt in ('-v', '--version'):
        getVersion()
    elif opt in ('-m', '--move'):
        getMove(arg)
