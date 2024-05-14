""" Módulo que contiene la clase concreta de un algoritmo de cifrado Atbash
"""


import re
from .algorithm import Algorithm


class AtbashAlgorithm(Algorithm):
    """ Clase concreta de un algoritmo de cifrado Atbash
    """

    alphabet = None
    extraReplaces = None

    def __init__(self, alphabet, extraReplaces={}, caseSensitive=False):
        self.alphabet = alphabet
        self.extraReplaces = extraReplaces
        self.caseSensitive = caseSensitive

    def execute(self, mensaje):
        """ Método para cifrar un mensaje
        """
        mensaje = self.clean_text(mensaje)
        mensaje = self.encrypt(mensaje)
        return mensaje

    def remove_punctuation(self, text):
        """ Método para eliminar espacios y puntuación de un texto
        """
        resultado = ''
        for c in text:
            if (c.lower() in self.alphabet) or c == ' ':
                resultado += c
        return resultado

    def clean_text(self, text):
        """ Método para limpiar un texto
        """
        resultado = ''

        # remove whitespace before and after
        text = text.strip() 
        
         # case sensitive
        if(not self.caseSensitive):
            resultado = resultado.lower()
            
        # Reemplazar letras con tildes por letras básicas
        for c in text:
            resultado += self.extraReplaces.get(c, c)
        
        resultado = self.remove_punctuation(resultado)
        return resultado

    def encrypt(self, message):
        """ Método para encriptar un mensaje utilizando el cifrado Atbash
        """
        encrypted_message = ''
        for char in message:
            if char.lower() in self.alphabet:                
                original_index = self.alphabet.index(char.lower())           
                encrypted_char = self.alphabet[len(self.alphabet) - 1 - original_index]
                
                # case sensitive
                if(self.caseSensitive and char.isupper()):
                    encrypted_message += encrypted_char.upper() 
                else:
                    encrypted_message += encrypted_char
                    
            elif char == ' ':
                encrypted_message += ' '
                
        return encrypted_message
    
 
