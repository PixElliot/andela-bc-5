#!/usr/bin/env python

def find_missing(l1, l2):

  if not l1 or not l2:      # If either list is empty
      return 0
  elif l1 == l2:          	# If lists are exactly the same
      return 0
    
  # If lists not similar
  #return [i for i in (l1 + l2) if (i not in l1) or (i not in l2)]

  for i in list(set(l1) ^ set(l2)):
  	return i
