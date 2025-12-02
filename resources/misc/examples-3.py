"""
Ejemplos de Funciones en Python
================================
Este archivo cubre funciones, parámetros, return y funciones lambda.
"""

# ========================================
# FUNCIONES CON PARÁMETROS
# ========================================

# Listas de ejemplo para trabajar
my_number_list1 = [12, 13, 14]
my_number_list2 = [31, 32, 33]


# --- Función 1: Identificar números pares e impares ---

# Input: Una lista de números
# Process: Recorrer la lista y verificar si cada número es par o impar
# Output: Imprime por consola el resultado de cada número

def odd_or_even(number_list):
    """Identifica y muestra qué números son pares y cuáles impares."""
    for x in number_list:
        if x % 2 == 0:  # El operador % da el resto de la división
            print(f"  {x} es par")
        else:
            print(f"  {x} es impar")


print("--- Números pares e impares ---")
print("Lista 1:")
odd_or_even(my_number_list1)

print("\nLista 2:")
odd_or_even(my_number_list2)


# ========================================
# FUNCIONES CON RETURN
# ========================================

# --- Función 2: Sumar todos los números de una lista ---

# Input: Una lista de números
# Process: Recorrer la lista y acumular cada número en una variable total
# Output: Retorna el total acumulado

def sum_numbers(number_list):
    """Calcula y retorna la suma de todos los números en la lista."""
    total = 0
    
    for x in number_list:
        total += x
    
    return total


print("\n--- Suma de números ---")
my_sum1 = sum_numbers(my_number_list1)
my_sum2 = sum_numbers(my_number_list2)

print(f"Suma de lista 1: {my_sum1}")
print(f"Suma de lista 2: {my_sum2}")
print(f"Suma total de ambas listas: {sum_numbers(my_number_list1) + sum_numbers(my_number_list2)}")


# ========================================
# FUNCIONES LAMBDA (ANÓNIMAS)
# ========================================

print("\n--- Funciones Lambda ---")

# Función tradicional
def add_ten_to_number(number):
    """Función tradicional que suma 10 a un número."""
    return number + 10


# Función lambda (función anónima de una sola línea)
# Sintaxis: lambda parámetros : expresión
add_ten_to_number_lambda = lambda number: number + 10

# Ambas funciones hacen exactamente lo mismo
test_number = 27
print(f"Función tradicional: {test_number} + 10 = {add_ten_to_number(test_number)}")
print(f"Función lambda:      {test_number} + 10 = {add_ten_to_number_lambda(test_number)}")

# Las funciones lambda son útiles para operaciones simples y rápidas
# Ejemplo adicional: multiplicar por 2
multiply_by_two = lambda x: x * 2
print(f"\nMultiplicar por 2:   {test_number} × 2 = {multiply_by_two(test_number)}")
