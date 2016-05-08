# -*- coding: utf-8 -*-

from unittest import TestCase
from python_test.quadrado import quadrado

class TestQuadrado(TestCase):

	def setUp(TestCase):
		TestCase.setUp(self)
		self.fig = Quadrado()

	def test_get_area(self):
		#começo então a verificar se o resultado é o resultado esperado.
		self.fig.lado = 2
		self.assertEqual(self.fig.get_area(), 4)
		self.fig.lado = 5.0
		self.assertEqual(self.fig.get_area(), 25.0)

	def test_get_perimetro(self):
		self.fig.lado = 2
		self.assertEqual(self.fig.get_perimetro(), 4)
		self.fig.lado = 5.0
		self.assertEqual(self.fig.get_perimetro(), 10.0)
		#assertEqual vai comparar o resultado do get_perimetro com 10, tem q ser igual!