"""
Ejemplos de Lectura y Escritura de Archivos
============================================
Este archivo muestra cómo trabajar con archivos de texto.
"""

import os

def create_file(filename, initial_content=""):
  """Crea un archivo nuevo con contenido inicial opcional."""
  try:
    # Verificar si ya existe
    if os.path.exists(filename):
      print(f"⚠️  El archivo '{filename}' ya existe")
      return False
    
    # Crear el archivo
    my_file = open(filename, "wt")
    if initial_content:
      my_file.write(initial_content)
    my_file.close()
    
    print(f"✓ Archivo '{filename}' creado correctamente")
    return True
    
  except PermissionError:
    print("✗ No hay permisos para crear el fichero")
    return False
  except IOError:
    print("✗ No se ha podido crear el fichero")
    return False


def read_file(filename):
  """Lee y muestra el contenido de un archivo."""
  try:
    # Verificar si existe
    if not os.path.exists(filename):
      print(f"✗ El archivo '{filename}' no existe")
      return None
    
    my_file = open(filename, "rt")
    content = my_file.read()
    print(f"\n--- Contenido de '{filename}' ---")
    print(content)
    my_file.close()
    
    return content
    
  except PermissionError:
    print("✗ No hay permisos para abrir el fichero")
    return None
  except IOError:
    print("✗ No se ha podido abrir o leer el fichero")
    return None


def write_file_from_the_end(filename, new_text):
  """Añade texto al final de un archivo existente."""
  try:
    # Verificar si existe
    if not os.path.exists(filename):
      print(f"✗ El archivo '{filename}' no existe. Créalo primero.")
      return False
    
    my_file = open(filename, "at")
    my_file.write(f"\n{new_text}")
    my_file.close()
    
    print(f"✓ Texto añadido al final de '{filename}'")
    return True
    
  except PermissionError:
    print("✗ No hay permisos para escribir en el fichero")
    return False
  except IOError:
    print("✗ No se ha podido abrir o escribir en el fichero")
    return False


# ========================================
# EJEMPLOS DE USO
# ========================================

if __name__ == "__main__":
  archivo = "thehobbit.txt"
  
  print("=== GESTIÓN DE ARCHIVOS ===\n")
  
  # 1. Intentar leer el archivo (si existe)
  print("1. Intentando leer el archivo...")
  read_file(archivo)
  
  # 2. Añadir texto al archivo
  print("\n2. Añadiendo texto...")
  nuevo_texto = "Y así comenzó una gran aventura."
  write_file_from_the_end(archivo, nuevo_texto)
  
  # 3. Leer de nuevo para ver los cambios
  print("\n3. Leyendo después de añadir texto...")
  read_file(archivo)
  
  # 4. Ejemplo de crear un archivo nuevo
  print("\n4. Creando un archivo nuevo...")
  create_file("prueba.txt", "Este es un archivo de prueba.")
  read_file("prueba.txt")