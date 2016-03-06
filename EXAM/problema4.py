'''
Problem 4

Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings.

This function takes in a string and returns a boolean.
'''

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

def isPalindrome (aString):
    palabra_invertida = inversa (aString)
    indice = 0
    cont = 0
    for i in range (len(aString)):
        if palabra_invertida[indice] == aString[indice]:
            indice += 1
            cont += 1
        else:
            return False

    if cont == len(aString): #Si el contador = a la cantidad de letras de la cadena
        return True