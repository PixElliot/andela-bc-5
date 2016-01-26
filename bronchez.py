#!/usr/bin/env python

while True:
    try:
        x = raw_input("What is your name?")
        break   #If user enters a string then the loop breaks (exits)
    except ValueError:
        print "Oops! please enter a name."  #From this point the loop repeats itself
