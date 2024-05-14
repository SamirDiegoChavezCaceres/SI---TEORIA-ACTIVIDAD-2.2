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
        mensaje = self.encrypt(mensaje)
        return mensaje

    def eliminar_espacios_puntuacion(self, text):
        """ Método para eliminar espacios y puntuación de un texto
        """
        resultado = ''
        for c in text:
            if ('a' <= c <= 'z') or c == 'ñ':
                resultado += c
        return resultado

    def clean_text(self, text):
        """ Método para limpiar un texto
        """
        tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
        resultado = ''

        # Reemplazar letras con tildes por letras básicas
        for c in text:
            resultado += tildes.get(c, c)
        resultado = self.eliminar_espacios_puntuacion(resultado.lower())
        return resultado.strip().replace(" ", "")

    def encrypt(self, message):
        """ Método para encriptar un mensaje utilizando el cifrado Atbash
        """
        encrypted_message = ''
        for char in message:
            if char in self.alphabet:
                original_index = self.alphabet.index(char)
                encrypted_char = self.alphabet[len(self.alphabet) - 1 - original_index]
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message
