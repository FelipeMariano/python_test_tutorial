# -*- coding: utf-8 -*-

from unittest import TestCase
from python_test.figura_geometrica import FiguraGeometrica

class TestFiguraGeometrica(TestCase):
	#Setando a variável global que usaremos no teste!
	def setUp(self):
		TestCase.setUp(self)
		self.fig = FiguraGeometrica()

		#Retorna um NotImplementedError.
		#O nome do método deve começar com test!
		def test_get_area(self):
			self.assertRaises(NotImplementedError, self.fig.get_area)

		def test_get_perimetro(self):
			self.assertRaises(NotImplementedError, self.fig.get_perimetro)

		#Terei a verificação da execução dos métodos da classe FiguraGeometrica
		#Como será uma classe abstrata, esses métodos serão vazios
		#ou seja, os métodos devem ser implementados nas classes filhas dessa classe!