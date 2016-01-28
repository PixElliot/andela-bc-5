#!/usr/bin/env python

def add(x, y):
	return x + y

y = lambda x, y: x + y #Takes two parameters

print add(10, 2)
print y(10, 2)

def make_incrementor(n):
	def inc(X):
		return x + n
	return inc

def make_inc(n): return lambda x: x + n #Takes one paremeter per time

def is_even(n):
	return n % 2 == 0

l = [2, 10, 4, 5, 6, 11, 12]

new_list = filter(is_even, l)
print new_list