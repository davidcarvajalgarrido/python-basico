# Lección 7 — Soluciones

## Ejercicio 1: Solución: Leer un archivo de texto

```python
def leer_notas(filename):
    """Lee y muestra el contenido de un archivo de notas."""
    try:
        archivo = open(filename, "r", encoding="utf-8")
        contenido = archivo.read()
        print(f"--- Contenido de {filename} ---")
        print(contenido)
        archivo.close()
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe")
        return None
    except IOError:
        print(f"Error: No se pudo leer el archivo '{filename}'")
        return None

# Prueba
leer_notas("notas.txt")
```

## Ejercicio 2: Solución: Escribir en un archivo de texto

```python
def agregar_nota(filename, asignatura, nota):
    """Añade una nueva nota al final del archivo."""
    try:
        archivo = open(filename, "a", encoding="utf-8")
        archivo.write(f"{asignatura}: {nota}\n")
        archivo.close()
        print(f"✓ Nota añadida: {asignatura}: {nota}")
        return True
    except IOError:
        print(f"Error: No se pudo escribir en '{filename}'")
        return False

# Prueba
agregar_nota("notas.txt", "Historia", 8.0)

# Verificar que se añadió
leer_notas("notas.txt")
```

## Ejercicio 3: Solución: Trabajar con archivos JSON

```python
import json

# Crear el diccionario del estudiante
estudiante = {
    "nombre": "Ana García",
    "edad": 20,
    "carrera": "Informática",
    "notas": [8.5, 7.0, 9.0, 8.0]
}

# Guardar en JSON
with open("estudiante.json", "w", encoding="utf-8") as archivo:
    json.dump(estudiante, archivo, ensure_ascii=False, indent=2)

print("✓ Archivo JSON creado")

# Leer desde JSON
with open("estudiante.json", "r", encoding="utf-8") as archivo:
    estudiante_leido = json.load(archivo)

print("\n--- Datos del estudiante ---")
print(f"Nombre: {estudiante_leido['nombre']}")
print(f"Edad: {estudiante_leido['edad']}")
print(f"Carrera: {estudiante_leido['carrera']}")
print(f"Notas: {estudiante_leido['notas']}")

# Calcular promedio
promedio = sum(estudiante_leido['notas']) / len(estudiante_leido['notas'])
print(f"Promedio: {promedio:.2f}")
```

## Ejercicio 4: Solución: Leer y escribir archivos CSV

```python
import csv

# Crear el archivo CSV
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 899.99, "stock": 5},
    {"id": 2, "nombre": "Mouse", "precio": 19.99, "stock": 20},
    {"id": 3, "nombre": "Teclado", "precio": 49.99, "stock": 15},
    {"id": 4, "nombre": "Monitor", "precio": 199.99, "stock": 8}
]

# Escribir en CSV
with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["id", "nombre", "precio", "stock"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    escritor.writeheader()  # Escribir encabezados
    escritor.writerows(productos)  # Escribir todas las filas

print("✓ Archivo CSV creado")

# Leer el CSV y filtrar productos con stock < 10
print("\n--- Productos con stock bajo (< 10) ---")
with open("productos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        stock = int(fila["stock"])
        if stock < 10:
            print(f"{fila['nombre']}: {stock} unidades")

# Calcular valor total del inventario
print("\n--- Valor total del inventario ---")
valor_total = 0

with open("productos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        precio = float(fila["precio"])
        stock = int(fila["stock"])
        valor_producto = precio * stock
        valor_total += valor_producto
        print(f"{fila['nombre']}: {precio}€ × {stock} = {valor_producto:.2f}€")

print(f"\nValor total: {valor_total:.2f}€")
```

## Ejercicio 5: Solución: Sistema de gestión de tareas

```python
import json
import os

def cargar_tareas(filename):
    """Carga las tareas desde un archivo JSON."""
    try:
        if not os.path.exists(filename):
            print(f"Archivo '{filename}' no existe. Creando lista vacía.")
            return []
        
        with open(filename, "r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)
        
        print(f"✓ {len(tareas)} tarea(s) cargada(s)")
        return tareas
    
    except json.JSONDecodeError:
        print(f"Error: El archivo '{filename}' no tiene formato JSON válido")
        return []


def guardar_tareas(filename, tareas):
    """Guarda las tareas en un archivo JSON."""
    try:
        with open(filename, "w", encoding="utf-8") as archivo:
            json.dump(tareas, archivo, ensure_ascii=False, indent=2)
        
        print(f"✓ {len(tareas)} tarea(s) guardada(s) en '{filename}'")
        return True
    
    except IOError:
        print(f"Error: No se pudo guardar en '{filename}'")
        return False


def agregar_tarea(tareas, titulo, prioridad):
    """Añade una nueva tarea a la lista."""
    # Calcular el nuevo ID (máximo actual + 1)
    if tareas:
        nuevo_id = max(tarea["id"] for tarea in tareas) + 1
    else:
        nuevo_id = 1
    
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo,
        "prioridad": prioridad,
        "completada": False
    }
    
    tareas.append(nueva_tarea)
    print(f"✓ Tarea añadida: '{titulo}' (Prioridad: {prioridad})")
    return tareas


def mostrar_tareas(tareas):
    """Muestra todas las tareas en formato legible."""
    if not tareas:
        print("No hay tareas para mostrar")
        return
    
    print("\n=== LISTA DE TAREAS ===")
    for tarea in tareas:
        estado = "✓" if tarea["completada"] else "○"
        print(f"{estado} [{tarea['id']}] {tarea['titulo']} - Prioridad: {tarea['prioridad']}")


# ========================================
# PRUEBA DEL SISTEMA
# ========================================

print("=== SISTEMA DE GESTIÓN DE TAREAS ===\n")

# 1. Cargar tareas existentes (o crear lista vacía)
mis_tareas = cargar_tareas("tareas.json")

# 2. Añadir 3 tareas
agregar_tarea(mis_tareas, "Estudiar Python", "Alta")
agregar_tarea(mis_tareas, "Hacer ejercicios", "Media")
agregar_tarea(mis_tareas, "Revisar apuntes", "Baja")

# 3. Guardar las tareas
guardar_tareas("tareas.json", mis_tareas)

# 4. Mostrar todas las tareas
mostrar_tareas(mis_tareas)
```
