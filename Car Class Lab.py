#!/usr/bin/env python

class Car(object):
	def __init__(self, name = 'General', model = 'GM', car_type = 'saloon'):
		self.name = name
		self.model = model
		self.car_type = car_type
		self.num_of_doors = 4
		self.num_of_wheels = 4
		self.speed = 0

		if (self.name == 'Koenigsegg') or (self.name == 'Porshe'):
			self.num_of_doors = 2

		if (self.car_type == 'trailer'):
			self.num_of_wheels = 8

	def is_saloon(self):
		if (self.car_type != 'trailer'):
			self.car_type = 'saloon'
		return self.car_type

	def drive(self, drive_speed):	
		if drive_speed == 3:
			self.speed = 1000
		elif drive_speed == 7:
			self.speed = 77

		return self
