#!/usr/bin/env python

def data_type(dt):

	if isinstance(dt, str):         # If dt is of type string
	    return len(dt)
	elif dt is None:      # If dt is of type None
	    return 'no value'
	elif isinstance(dt, bool):      # If dt is of type boolean
	  	return dt
	elif isinstance(dt, int):       # If dt is of type integer
	  	if dt < 100:
	  		return 'less than 100'
	  	elif dt > 100:
	  		return 'more than 100'
	  	return 'equal to 100'
	elif isinstance(dt, list):      # If dt is of type list
		if len(dt) < 3:
			return None
		return dt[2]

	return 0                        # If dt is none of the above
	