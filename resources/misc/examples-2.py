
"""
Ejemplos Intermedios de Python
===============================
Este archivo cubre strings, entrada/salida, condicionales y bucles while.
"""

# ========================================
# STRINGS Y ENTRADA/SALIDA
# ========================================

# --- Entrada de datos ---
# Descomenta las siguientes líneas para probar la entrada de usuario
# my_name = input("¿Cómo te llamas? ")
# my_age = input("¿Cuántos años tienes cumplidos? ")

# Para este ejemplo, usamos valores fijos
my_name = "David"
my_age = "21"

# --- Diferentes formas de imprimir strings ---

# 1. Concatenación con +
print("Hola, me llamo " + my_name)

# 2. Separación con comas (añade espacios automáticamente)
print("Hola, me llamo", my_name, "y me gusta comer", 30, "fantasmas")

# 3. Conversión de tipos para concatenar
print("Y nací en el año " + str(2025 - int(my_age)))

# --- F-strings (forma moderna y recomendada) ---
my_country = "La Atlántida"
my_year = 1800

print(f"Soy de {my_country} del año {my_year}")
print(f"El doble de mi año sería: {my_year * 2}")


# ========================================
# CONDICIONALES MÚLTIPLES (if-elif-else)
# ========================================

print("\n--- Períodos históricos ---")

# Clasificar el año según períodos históricos
if my_year < 0:
    print(f"El año {my_year}: Antes de Cristo")
elif my_year < 500:
    print(f"El año {my_year}: Época Clásica - Antes de la Caída de Roma")
elif my_year < 1500:
    print(f"El año {my_year}: Edad Media - Antes del Renacimiento")
else:
    print(f"El año {my_year}: Edad Moderna - Después del Renacimiento")


# ========================================
# BUCLE WHILE CON BÚSQUEDA
# ========================================

print("\n--- Búsqueda en lista ---")

# Problema: Encontrar la posición de la primera aparición del número 42
# y dejar de buscar cuando lo encontremos

# 1) Situación inicial
my_number_list = [13, 34, 78, 42, 99, 42]  # El 42 aparece dos veces
found_number = False
i = 0

# 2) Condición de parada: mientras haya números pendientes Y no hayamos encontrado el 42
while i < len(my_number_list) and not found_number:
    # Verificamos si el número actual es 42
    if my_number_list[i] == 42:
        found_number = True  # Bandera (flag) para indicar que lo encontramos
    
    # 3) Cambio de situación: avanzar al siguiente índice
    i += 1

# Mostrar resultado
if found_number:
    print(f"✓ El número 42 está en la posición {i - 1}")  # Restamos 1 porque i ya se incrementó
    print(f"  Lista completa: {my_number_list}")
else:
    print(f"✗ El número 42 no está en la lista")
    print(f"  Lista completa: {my_number_list}")

