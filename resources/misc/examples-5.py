"""
Ejemplos de Excepciones en Python
==================================
Este archivo muestra cómo manejar errores con try-except.
"""

# ========================================
# EJEMPLO 1: División por cero
# ========================================

print("--- Ejemplo 1: División por cero ---")

def dividir(a, b):
  """Divide dos números manejando el caso de división por cero."""

  try:
    resultado = a / b # Esto puede generar excepción
    
    return resultado
  except ZeroDivisionError:
    return None
  finally:
    print("Todo ha terminado")

result = dividir(10, 0)
if result != None:
  print(result)
else:
  print("Has llamado a la función pasándole un cero")

# ========================================
# EJEMPLO 2: Conversión de tipos
# ========================================

print("\n--- Ejemplo 2: Conversión de tipos ---")

def convertir_a_numero(texto):
  """Intenta convertir un texto a número."""
  try:
    numero = int(texto)
    print(f"Conversión exitosa: '{texto}' → {numero}")
    return numero
  except ValueError:
    print(f"Error: '{texto}' no es un número válido")
    return None

convertir_a_numero("42")
convertir_a_numero("abc")

# ========================================
# EJEMPLO 3: Acceso a listas
# ========================================

print("\n--- Ejemplo 3: Acceso a índices ---")

def obtener_elemento(lista, indice):
  """Obtiene un elemento de la lista manejando índices inválidos."""
  try:
    elemento = lista[indice]
    print(f"Elemento en posición {indice}: {elemento}")
    return elemento
  except IndexError:
    print(f"Error: El índice {indice} está fuera de rango")
    return None

frutas = ["manzana", "pera", "plátano"]
obtener_elemento(frutas, 1)
obtener_elemento(frutas, 10)

# ========================================
# EJEMPLO 4: Múltiples excepciones
# ========================================

print("\n--- Ejemplo 4: Múltiples excepciones ---")

def operacion_segura(a, b, operacion):
  """Realiza operaciones manejando varios tipos de errores."""
  try:
    if operacion == "dividir":
      resultado = a / b
    elif operacion == "convertir":
      resultado = int(a) + int(b)
    else:
      resultado = None
    
    print(f"Resultado: {resultado}")
    return resultado
  
  except ZeroDivisionError:
    print("Error: División por cero")
  except ValueError:
    print("Error: Valor no válido para conversión")
  except TypeError:
    print("Error: Tipo de dato incorrecto")

operacion_segura(10, 2, "dividir")
operacion_segura(10, 0, "dividir")
operacion_segura("5", "abc", "convertir")

# ========================================
# EJEMPLO 5: try-except-else-finally
# ========================================

print("\n--- Ejemplo 5: Estructura completa ---")

def procesar_numero(texto):
  """Demuestra el uso completo de try-except-else-finally."""
  print(f"\nProcesando: '{texto}'")
  
  try:
    numero = int(texto)
    resultado = 100 / numero
  except ValueError:
    print("  ✗ Error: No es un número")
  except ZeroDivisionError:
    print("  ✗ Error: El número es cero")
  else:
    # Se ejecuta solo si NO hubo excepciones
    print(f"  ✓ Éxito: 100 / {numero} = {resultado}")
  finally:
    # Se ejecuta SIEMPRE, haya o no excepción
    print("  → Proceso finalizado")

procesar_numero("20")
procesar_numero("abc")
procesar_numero("0")

# ========================================
# EJEMPLO 6: Lanzar excepciones propias
# ========================================

print("\n--- Ejemplo 6: Lanzar excepciones ---")

def validar_edad(edad):
  """Valida que la edad sea un valor positivo razonable."""
  try:
    if edad < 0:
      raise ValueError("La edad no puede ser negativa")
    if edad > 150:
      raise ValueError("La edad no es realista")
    
    print(f"Edad válida: {edad} años")
    return True
  
  except ValueError as e:
    print(f"Error de validación: {e}")
    return False

validar_edad(25)
validar_edad(-5)
validar_edad(200)
