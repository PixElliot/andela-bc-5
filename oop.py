#!/usr/bin/env python

class Vehicle(object):
	def __init__(self, engine_type, **kwargs):
		self.engine_type = engine_type
		for i in kwargs:
			setattr(self, i, kwargs[i])

	def set_color(self, color):
		self.color = color

	def set_speed(self, speed):
		self.speed = speed

class Car(Vehicle):
	def __init__(self, engine_type, car_category, **kwargs):
		super(self.__class__, self).__init__(engine_type, **kwargs)
		self.car_category = car_category
		self.doors = 5
		self.wheels = 4

my_car = Car("VT120", "Saloon", engine_cc = 1500, color = 120, max_speed = 120)
print my_car.max_speed
