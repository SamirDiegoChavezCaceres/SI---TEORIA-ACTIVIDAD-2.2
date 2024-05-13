""" Módulo que contiene la clase concreta de un algoritmo de cifrado Atbash
"""


from .algorithm import Algorithm


class AtbashAlgorithm(Algorithm):
    """ Clase concreta de un algoritmo de cifrado Atbash
    """

    def execute(self, mensaje):
        """ Método para cifrar un mensaje
        """
        return mensaje[::-1]
