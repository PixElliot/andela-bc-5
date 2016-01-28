#!/usr/bin/env python

def words(my_string):

	ls = my_string.split()
	new_dict = {}
	count = 0
		  
	for i in ls:
		count = 0
		for j in ls:
			if i == j:
				count += 1
		
		try:
			if type(int(i)) == int:
				new_dict [int(i)] = count
		except ValueError:
			new_dict [i] = count

						
	return new_dict