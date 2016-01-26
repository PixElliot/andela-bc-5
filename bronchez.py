#!/usr/bin/env python

while True:
    try:
        x = raw_input("What is your name?")
        break
    except ValueError:
        print "Oops! please enter a name."
