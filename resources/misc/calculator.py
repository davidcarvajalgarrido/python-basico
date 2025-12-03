"""
Calculadora Simple en Python
=============================
Funciones básicas de una calculadora.
"""

def sumar(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

def restar(a, b):
    """Resta dos números y retorna el resultado."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números y retorna el resultado."""
    return a * b

def dividir(a, b):
    """
    Divide dos números y retorna el resultado.
    Si el divisor es 0, retorna None y muestra un error.
    """
    if b == 0:
        print("Error: No se puede dividir entre 0")
        return None
    return a / b
