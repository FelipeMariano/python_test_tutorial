# -*- coding: utf-8 -*-

import math
from python_test.figura_geometrica import FiguraGeometrica

class Circulo(object):

	def __init__(self):
		self.raio = 0

	def get_area(self):
		return math.pi * self.raio**2

	def get_perimetro(self):
		return 2 * math.pi * self.raio