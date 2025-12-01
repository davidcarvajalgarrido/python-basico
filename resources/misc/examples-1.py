"""
Ejemplos Básicos de Python
===========================
Este archivo contiene ejemplos introductorios de Python para principiantes.
"""

# ========================================
# VARIABLES Y TIPOS DE DATOS
# ========================================

# Números enteros (int)
number1 = 43
number2 = -17

# Cadenas de texto (str)
number_str = "2"
text1 = "Hoy es 1 de diciembre"

# Booleanos (bool)
is_alive = False

# Conversión de tipos y operaciones
total = number1 + int(number_str)
print(f"Resultado de {number1} + {number_str}: {total}")


# ========================================
# LISTAS
# ========================================

# Crear una lista con varios números
quantities = [12, 45, -78]

# Acceder a elementos por índice (el índice empieza en 0)
print(f"Elemento en posición 1: {quantities[1]}")

# Agregar un nuevo elemento al final
quantities.append(2)

# Ordenar la lista
quantities.sort()

print(f"Lista ordenada: {quantities}")
print(f"Cantidad de elementos: {len(quantities)}")


# ========================================
# ESTRUCTURAS DE CONTROL Y BUCLES
# ========================================

# Ejemplo: Sumar todos los elementos de una lista

print("\n--- Suma de elementos ---")

# Verificar si la lista está vacía
if len(quantities) == 0:
    print("⚠️  La lista no tiene elementos que sumar")
else:
    # Calcular la suma usando un bucle for
    total = 0
    for element in quantities:
        total += element  # Equivalente a: total = total + element
    
    print(f"La suma de {quantities} es: {total}")


# ========================================
# DICCIONARIOS
# ========================================

# Los diccionarios almacenan pares clave-valor
me = {
    "name": "David",
    "age": 21,
    "skills": ["python", "teach", "poetry"]
}

print("\n--- Diccionarios ---")
print(f"Edad actual: {me['age']}")

# Modificar un valor
me["age"] += 1
print(f"Edad después del cumpleaños: {me['age']}")

# Acceder a una lista dentro del diccionario
print(f"Habilidades: {', '.join(me['skills'])}")


# ========================================
# TUPLAS
# ========================================

# Las tuplas son inmutables (no se pueden modificar después de crearlas)
fruits = ("banana", "cherry", "apple")

print("\n--- Tuplas ---")
print(f"Frutas: {fruits}")
print(f"Primera fruta: {fruits[0]}")


# ========================================
# SETS (CONJUNTOS)
# ========================================

# Los sets no permiten elementos duplicados y no tienen orden
days = {12, 6, 21, 21, 27}  # El 21 duplicado se eliminará automáticamente

print("\n--- Sets ---")
print(f"Días del mes: {days}")
print(f"Cantidad de días únicos: {len(days)}")  # Solo contará 4 elementos

