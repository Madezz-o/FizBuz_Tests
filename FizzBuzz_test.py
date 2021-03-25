import unittest
from FizzBuzz import FizzBuzz
from FizzBuzz import errorException

class FizzBuzz_Tests(unittest.TestCase):

    def test_renvoie_nombre(self):
        nombre = 8
        nombreRetourne = FizzBuzz.NombreMultiplicateur(nombre)
        self.assertEqual(nombre, nombreRetourne)

    def test_renvoie_Exception_si_nombre_egale_0(self):
        nombre = 0
        with self.assertRaises(errorException):
            FizzBuzz.NombreMultiplicateur(nombre)

    def test_nombre_negatif(self):
        nombre = -5
        with self.assertRaises(errorException):
            FizzBuzz.NombreMultiplicateur(nombre)
