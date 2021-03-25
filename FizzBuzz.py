class FizzBuzz :
    def NombreMultiplicateur(nombre):
        if nombre <= 0:
            raise(errorException())
        elif nombre % 3 == 0 and nombre % 5 == 0 :
            return "FIZZBUZZ" 
        elif nombre % 3 == 0:
            return "FIZZ"
        elif nombre % 5 == 0:
            return "BUZZ"
        return nombre





class errorException(Exception):
    def __init__(self):
        super()