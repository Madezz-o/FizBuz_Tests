class FizzBuzz :
    @staticmethod
    def NombreMultiplicateur(nombre):
        if nombre.isalpha():
            raise(errorException('Entrez un nombre pas de texte'))
        else :
            nombre = int(nombre)
        if nombre <= 0:
            raise(errorException("Le nombre doit être positif"))
        if nombre % 3 == 0 and nombre % 5 == 0 :
            return "FIZZBUZZ" 
        if nombre % 3 == 0:
            return "FIZZ"
        if nombre % 5 == 0:
            return "BUZZ"
        return str(nombre)





class errorException(Exception):
    def __init__(self, texte):
        super()
        self.texte = texte