""" Módulo que contiene la clase concreta de un algoritmo de descifrado Vignere
"""


import re


from .algorithm import Algorithm


class VignereAlgorithm(Algorithm):
    """ Clase concreta de un algoritmo de descifrado Vignere
    """

    alphabet = None
    key = None

    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key

    def execute(self, mensaje):
        """ Método para descifrar un mensaje
        """
        mensaje = self.clean_text(mensaje)
        mensaje = self.vigenere_cipher(mensaje, self.key)
        return mensaje

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

    def vigenere_cipher(self, text, key):
        """ Método para cifrar un texto
        """
        alphabet = self.alphabet
        encrypted_text = ''
        key_index = 0
        for char in text:
            if char == ' ':
                encrypted_text += ' ' #Cuando es espacio ya no hace mas, pasa
                continue
            char_index = alphabet.find(char)
            if char_index != -1:
                key_char = key[key_index % len(key)]
                key_index += 1
                key_char_index = alphabet.find(key_char)
                encrypted_index = (char_index + key_char_index) % len(alphabet)
                encrypted_text += alphabet[encrypted_index]
            else:
                encrypted_text += char
        return encrypted_text