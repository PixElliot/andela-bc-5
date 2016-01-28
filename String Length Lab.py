#!/usr/bin/env python

def string_length(my_str):
  
  if isinstance(my_str, str):
    return [len(my_str)]
  elif isinstance(my_str, list):
    return [len(i) for i in my_str]
    
  return 0