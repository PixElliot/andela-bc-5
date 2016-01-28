#!/usr/bin/env python

def fizz_buzz(num):
  if (num % 3 == 0) and (num % 5 == 0):     # If num divisible by 3 & 5
      return 'FizzBuzz'
  elif num % 3 == 0:                        # If num divisible by 3
      return 'Fizz'
  elif num % 5 == 0:                        # If num divisible by 5
      return 'Buzz'
  else:										# If num  not divisible by 3 & 5 
      return num