# Lección 8 — Soluciones

## Ejercicio 1: Solución: Crear tu primer DataFrame

```python
import pandas as pd

# Crear el DataFrame
productos = pd.DataFrame({
    "nombre": ["Laptop", "Mouse", "Teclado", "Monitor", "Webcam"],
    "categoria": ["Ordenadores", "Periféricos", "Periféricos", "Monitores", "Periféricos"],
    "precio": [899.99, 19.99, 49.99, 199.99, 79.99],
    "stock": [5, 25, 18, 8, 12]
})

# Mostrar el DataFrame completo
print("=== DataFrame completo ===")
print(productos)

# Mostrar primeras 3 filas
print("\n=== Primeras 3 filas ===")
print(productos.head(3))

# Mostrar información
print("\n=== Información del DataFrame ===")
print(productos.info())
```

## Ejercicio 2: Solución: Seleccionar y filtrar datos

```python
import pandas as pd

# Crear el DataFrame (mismo del ejercicio anterior)
productos = pd.DataFrame({
    "nombre": ["Laptop", "Mouse", "Teclado", "Monitor", "Webcam"],
    "categoria": ["Ordenadores", "Periféricos", "Periféricos", "Monitores", "Periféricos"],
    "precio": [899.99, 19.99, 49.99, 199.99, 79.99],
    "stock": [5, 25, 18, 8, 12]
})

# Seleccionar solo la columna 'nombre'
print("=== Solo nombres ===")
print(productos["nombre"])

# Seleccionar columnas 'nombre' y 'precio'
print("\n=== Nombre y precio ===")
print(productos[["nombre", "precio"]])

# Filtrar productos con precio > 50
print("\n=== Productos con precio > 50€ ===")
print(productos[productos["precio"] > 50])

# Filtrar periféricos con stock < 15
print("\n=== Periféricos con stock < 15 ===")
filtro = (productos["categoria"] == "Periféricos") & (productos["stock"] < 15)
print(productos[filtro])
```

## Ejercicio 3: Solución: Leer y escribir archivos CSV

```python
import pandas as pd

# Crear el archivo CSV con datos de ejemplo
ventas_datos = {
    "fecha": ["2024-01-15", "2024-01-15", "2024-01-16", "2024-01-16", "2024-01-17"],
    "producto": ["Laptop", "Mouse", "Teclado", "Laptop", "Monitor"],
    "cantidad": [2, 5, 3, 1, 2],
    "precio_unitario": [899.99, 19.99, 49.99, 899.99, 199.99]
}

ventas_df = pd.DataFrame(ventas_datos)
ventas_df.to_csv("ventas.csv", index=False)
print("✓ Archivo ventas.csv creado")

# Leer el archivo CSV
ventas = pd.read_csv("ventas.csv")

print("\n=== Primeras filas de ventas ===")
print(ventas.head())

# Crear columna 'total'
ventas["total"] = ventas["cantidad"] * ventas["precio_unitario"]

print("\n=== DataFrame con columna 'total' ===")
print(ventas)

# Guardar el archivo modificado
ventas.to_csv("ventas_con_total.csv", index=False)
print("\n✓ Archivo ventas_con_total.csv guardado")
```

## Ejercicio 4: Solución: Estadísticas y operaciones básicas

```python
import pandas as pd

# Leer el archivo con la columna total
ventas = pd.read_csv("ventas_con_total.csv")

print("=== ESTADÍSTICAS ===\n")

# Suma total
suma_total = ventas["total"].sum()
print(f"Suma total de ventas: {suma_total:.2f}€")

# Promedio de precio unitario
promedio_precio = ventas["precio_unitario"].mean()
print(f"Precio unitario promedio: {promedio_precio:.2f}€")

# Máximo y mínimo de cantidad
max_cantidad = ventas["cantidad"].max()
min_cantidad = ventas["cantidad"].min()
print(f"Cantidad máxima: {max_cantidad}")
print(f"Cantidad mínima: {min_cantidad}")

# Estadísticas descriptivas
print("\n=== Estadísticas descriptivas ===")
print(ventas.describe())

# Contar ventas por producto
print("\n=== Ventas por producto ===")
print(ventas["producto"].value_counts())
```

## Ejercicio 5: Solución: Agrupación y análisis

```python
import pandas as pd

# Crear el DataFrame de estudiantes
estudiantes = pd.DataFrame({
    "nombre": ["Ana", "Carlos", "María", "Juan", "Ana", "Carlos", "María", "Juan"],
    "curso": ["1º", "1º", "2º", "2º", "1º", "2º", "1º", "2º"],
    "asignatura": ["Matemáticas", "Matemáticas", "Matemáticas", "Matemáticas", 
                   "Física", "Física", "Física", "Física"],
    "nota": [8.5, 7.0, 9.0, 6.5, 7.5, 8.0, 8.5, 7.0]
})

print("=== DataFrame de estudiantes ===")
print(estudiantes)

# Agrupar por curso y calcular nota media
print("\n=== Nota media por curso ===")
media_por_curso = estudiantes.groupby("curso")["nota"].mean()
print(media_por_curso)

# Agrupar por asignatura con múltiples estadísticas
print("\n=== Estadísticas por asignatura ===")
stats_asignatura = estudiantes.groupby("asignatura")["nota"].agg([
    ("media", "mean"),
    ("maxima", "max"),
    ("cantidad", "count")
])
print(stats_asignatura)

# Encontrar el estudiante con la nota más alta
print("\n=== Estudiante con nota más alta ===")
idx_max = estudiantes["nota"].idxmax()
mejor_estudiante = estudiantes.loc[idx_max]
print(f"Estudiante: {mejor_estudiante['nombre']}")
print(f"Asignatura: {mejor_estudiante['asignatura']}")
print(f"Nota: {mejor_estudiante['nota']}")

# Guardar en JSON
estudiantes.to_json("estudiantes.json", orient="records", indent=2, force_ascii=False)
print("\n✓ DataFrame guardado en estudiantes.json")
```

**Contenido de `estudiantes.json` generado:**
```json
[
  {
    "nombre": "Ana",
    "curso": "1º",
    "asignatura": "Matemáticas",
    "nota": 8.5
  },
  {
    "nombre": "Carlos",
    "curso": "1º",
    "asignatura": "Matemáticas",
    "nota": 7.0
  },
  ...
]
```
