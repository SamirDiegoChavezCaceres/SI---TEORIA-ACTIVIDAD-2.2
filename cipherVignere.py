import re

def clean_text(text):
    # Eliminar signos de puntuación y convertir a minúsculas
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    # Reemplazar letras con tildes por letras básicas
    clean_text = clean_text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u')
    return clean_text

def vigenere_cipher(text, key, alphabet):
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
#------Caso
"""
        alphabet = 'abcdefghijklmnñopqrstuvwxyz'
        mensaje_original = "Hola, ¿cómo estás? aqui mE reporto."
        clave = "llave"
        mensaje_limpio = clean_text(mensaje_original)
        clave_limpia = clean_text(clave)
        mensaje_cifrado = vigenere_cipher(mensaje_limpio, clave_limpia, alphabet)
        print(mensaje_cifrado)
"""
