""" Crear una clase abstracta de un algoritmo de cifrado y descifrado
"""


from abc import ABC, abstractmethod


class Algorithm(ABC):
    """ Clase abstracta de un algoritmo de cifrado y descifrado
    """

    @abstractmethod
    def execute(self, mensaje):
        """ Método abstracto para ejecutar el algoritmo
        """
