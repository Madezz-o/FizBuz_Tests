import unittest
from FizzBuzz import FizzBuzz

class FizzBuzz_Tests(unittest.TestCase):

    def test_renvoie_nombre(self):
        nombre = 8
        nombreRetourne = FizzBuzz.NombreMultiplicateur(nombre)
        self.assertEqual(nombre, nombreRetourne)
