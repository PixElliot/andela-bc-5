#!/usr/bin/env python

# def min(list):
  
# 	temp = list[0]
# 	new_l = []
	
# 	for i in list[1:]:
# 		if i < temp:            
# 		    temp = i 
	
# 	new_l.append(temp)
# 	temp = list[0]
	
# 	for i in list[1:]:
# 		if i > temp:            
# 		    temp = i
	
# 	new_l.append(temp)
	
# 	return new_l

def find_min_max(l):
    
    if min(l) != max(l):
    	return [min(l), max(l)]

    return [len(l)]

	
	