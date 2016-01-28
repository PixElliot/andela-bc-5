#!/usr/bin/env python

def arith_geo(l):
  
  if not l:                               # If array is empty
    return 0

  else:                                   # If array is not empty
    a = l[1] - l[0]
    g = float(l[1]) / float(l[0])
    
    a_list = [l[x] for x in range(len(l) - 1) if (l[x] + a) != l[x + 1]]
    g_list = [l[x] for x in range(len(l) - 1) if (l[x] * g) != l[x + 1]]
    
    if not a_list:                        # If a_list empty then arithmetic                 
      return 'Arithmetic'
    elif not g_list:
      return 'Geometric'                  # If g_list empty then geometric
    
  return -1                               # If neither