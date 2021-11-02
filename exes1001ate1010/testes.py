from unittest import TestCase
from exe_1000 import speak
from exe_1001 import soma
from exe_1002 import area
from exe_1003 import product
from exe_1004 import simple_product
from exe_1006 import average2


class Testes(TestCase):
    def test_speak(self):
        self.assertEqual(speak(), print("Hello World!"))

    def test_soma(self):
        self.assertEqual(soma(10, 9), 19)
        self.assertEqual(soma(-10, 4), -6)
        self.assertEqual(soma(15, -7), 8)

    def test_area(self):
        self.assertEqual(area(2.00), 12.5664)
        self.assertEqual(area(100.64), 31819.3103)
        self.assertEqual(area(150.00), 70685.7750)

    def test_product(self):
        self.assertEqual(product(3, 9), 27)
        self.assertEqual(product(-30, 10), -300)
        self.assertEqual(product(0, 9), 0)

    def test_average2(self):
        self.assertEqual(average2(5.0, 6.0, 7.0), 6.3)
        self.assertEqual(average2(5.0, 10.0, 10.0), 9.0)
        self.assertEqual(average2(10.0, 10.0, 5.0), 7.5)

    def test_simple_product(self):
        self.assertEqual(simple_product(3, 9), 27)
        self.assertEqual(simple_product(-30, 10), -300)
        self.assertEqual(simple_product(0, 9), 0)
