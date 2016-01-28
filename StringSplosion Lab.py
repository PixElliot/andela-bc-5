#!/usr/bin/env python

class StringSplosion(object):
	def __init__(self, my_str):
		self.my_str = my_str

	def manipulate(self):
		new_str = ""
		for i in range(len(self.my_str)):
			new_str += self.my_str[:i+1]

		return new_str 