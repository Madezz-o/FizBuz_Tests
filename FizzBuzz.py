class FizzBuzz :
    def NombreMultiplicateur(nombre):
        if nombre <= 0:
            raise(errorException())
        elif nombre % 3 == 0:
            return "FIZZ"
        return nombre





class errorException(Exception):
    def __init__(self):
        super()