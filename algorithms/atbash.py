""" Módulo que contiene la clase concreta de un algoritmo de cifrado Atbash
"""


import re
from .algorithm import Algorithm


class AtbashAlgorithm(Algorithm):
    """ Clase concreta de un algoritmo de cifrado Atbash
    """

    alphabet = None

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def execute(self, mensaje):
        """ Método para cifrar un mensaje
        """
        mensaje = self.clean_text(mensaje)
        return mensaje[::-1]

    def clean_text(self, text):
        """ Método para limpiar un texto
        """
        tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
        resultado = ''

        # Eliminar signos de puntuación y convertir a minúsculas
        clean_text = re.sub(r'[^\w\s]', '', text.lower())
        # Reemplazar letras con tildes por letras básicas
        for c in clean_text:
            resultado += tildes.get(c, c)
        return resultado.strip().replace(" ", "")
