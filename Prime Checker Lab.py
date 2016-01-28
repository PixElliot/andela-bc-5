# #!/usr/bin/env python

# from math import sqrt

# class PrimeChecker(object):
#   def __init__(self, number):
#     self.number = int(number)
    
#   def is_prime(self):
#     if self.number >= 2:
#         for i in range(2, int(sqrt(self.number))):
#             if not (i % 2 == 0):
#                 return False
#     else:
#   	  return False
#     return True

class PrimeChecker(object):
  def __init__(self, number):
    self.number = number

  def is_prime(self):
    if self.number == '':
        return False

    try:
      self.number = int(self.number)
    except:
      self.number = int(float(self.number))

    if self.number >= 2:
        for i in range(2, self.number):
            if not (self.number % i):
                return False
    else:
      return False
    return True