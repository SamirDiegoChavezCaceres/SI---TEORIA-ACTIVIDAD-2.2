""" Módulo que contiene la clase concreta de un algoritmo de descifrado Vignere
"""


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
        mensaje = self.vigenere_decoder(mensaje, self.key)
        return mensaje

    def vigenere_decoder(self, text, key):
        """ Método para descifrar un texto """
        alphabet = self.alphabet
        decrypted_text = ''
        key_index = 0
        for char in text:
            char_index = alphabet.find(char)
            if char_index != -1:
                key_char = key[key_index % len(key)]
                key_index += 1
                key_char_index = alphabet.find(key_char) + 1
                decrypted_index = (char_index - key_char_index) % len(alphabet)
                decrypted_text += alphabet[decrypted_index]
            else:
                decrypted_text += char
        return decrypted_text
