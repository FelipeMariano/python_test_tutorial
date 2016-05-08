# -*- coding: utf-8 -*-

class Quadrado(object):
	def __init__(self):
		self.lado = 0

	def get_area(self):
		return self.lado  ** 2

	def get_perimetro(self):
		return self.lado * 4
