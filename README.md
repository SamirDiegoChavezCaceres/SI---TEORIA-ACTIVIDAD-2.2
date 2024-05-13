# Caso de uso de Vignere
alphabet = 'abcdefghijklmnñopqrstuvwxyz'
mensaje_original = "Hola, ¿cómo estás? aqui mE reporto."
clave = "llave"
mensaje_limpio = clean_text(mensaje_original)
clave_limpia = clean_text(clave)
mensaje_cifrado = vigenere_cipher(mensaje_limpio, clave_limpia, alphabet)
print(mensaje_cifrado)