#!/usr/bin/env python

def my_sol(num):
	ls = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	nl = []
	for i in str(num):
			nl.append(ls[int(i)])
	return " ".join(nl)
