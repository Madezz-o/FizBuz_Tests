import unittest
from FizzBuzz import FizzBuzz
from FizzBuzz import errorException

class FizzBuzz_Tests(unittest.TestCase):

    def test_renvoie_nombre(self):
        nombre = "8"
        nombreRetourne = FizzBuzz.NombreMultiplicateur(nombre)
        self.assertEqual(nombre, nombreRetourne)

    def test_renvoie_Exception_si_nombre_egale_0(self):
        nombre = "0"
        with self.assertRaises(errorException):
            FizzBuzz.NombreMultiplicateur(nombre)

    def test_nombre_negatif(self):
        nombre = "-5"
        with self.assertRaises(errorException):
            FizzBuzz.NombreMultiplicateur(nombre)

    def test_renvoie_fizz_nombre_multiple_de_3(self):
        nombre = "9"
        result = "FIZZ"
        nombreRetourne = FizzBuzz.NombreMultiplicateur(nombre)
        self.assertEqual(result, nombreRetourne)

    def test_renvoie_buzz_nombre_multiple_de_5(self) :
        nombre = "10"
        result = "BUZZ"
        nombreRetourne = FizzBuzz.NombreMultiplicateur(nombre)
        self.assertEqual(result, nombreRetourne)

    def test_renvoie_fizzbuzz_si_multiple_de_3_ET_5(self) :
        nombre = "15"
        result = "FIZZBUZZ"
        nombreRetourne = FizzBuzz.NombreMultiplicateur(nombre)
        self.assertEqual(result, nombreRetourne)

    def test_renvoie_erreur_si_texte(self) :
        nombre = "TEST"
        with self.assertRaises(errorException):
            FizzBuzz.NombreMultiplicateur(nombre)

if __name__ == '__main__':
    unittest.main()