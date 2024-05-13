""" Módulo que contiene la clase concreta de un algoritmo de descifrado Vignere
"""


from .algorithm import Algorithm


class VignereAlgorithm(Algorithm):
    """ Clase concreta de un algoritmo de descifrado Vignere
    """
    def __init__(self, clave):
        self.clave = clave

    def execute(self, mensaje):
        """ Método para descifrar un mensaje
        """
        return mensaje[::-1]
