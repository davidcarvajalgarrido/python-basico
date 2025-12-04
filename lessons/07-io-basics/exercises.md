# Lección 7 — Ejercicios

## Ejercicio 1: Leer un archivo de texto

1. Crea un archivo llamado `notas.txt` con el siguiente contenido (puedes crearlo manualmente):
   ```
   Matemáticas: 8.5
   Física: 7.0
   Química: 9.0
   ```
2. Escribe una función `leer_notas(filename)` que:
   - Abra el archivo en modo lectura
   - Lea todo el contenido
   - Muestre el contenido por pantalla
   - Cierre el archivo
3. Usa `try-except` para manejar el caso de que el archivo no exista.

## Ejercicio 2: Escribir en un archivo de texto

1. Crea una función `agregar_nota(filename, asignatura, nota)` que:
   - Abra el archivo en modo "append" (añadir al final)
   - Escriba una nueva línea con formato: `"Asignatura: nota"`
   - Cierre el archivo
2. Usa la función para añadir: `"Historia: 8.0"` al archivo `notas.txt`.
3. Lee el archivo de nuevo para verificar que se añadió correctamente.

## Ejercicio 3: Trabajar con archivos JSON

1. Crea un diccionario con información de un estudiante:
   ```python
   estudiante = {
       "nombre": "Ana García",
       "edad": 20,
       "carrera": "Informática",
       "notas": [8.5, 7.0, 9.0, 8.0]
   }
   ```
2. Usa el módulo `json` para:
   - Guardar el diccionario en un archivo `estudiante.json` con `json.dump()`
   - Leer el archivo con `json.load()`
   - Mostrar el contenido leído
3. Calcula y muestra el promedio de las notas del estudiante.

## Ejercicio 4: Leer y escribir archivos CSV

1. Usa el módulo `csv` para crear un archivo `productos.csv` con las siguientes columnas: `id`, `nombre`, `precio`, `stock`.
2. Escribe al menos 4 productos de ejemplo:
   ```
   1,Laptop,899.99,5
   2,Mouse,19.99,20
   3,Teclado,49.99,15
   4,Monitor,199.99,8
   ```
3. Lee el archivo CSV y muestra solo los productos con `stock < 10`.
4. Calcula y muestra el valor total del inventario (suma de `precio * stock` de todos los productos).

## Ejercicio 5: Sistema de gestión de tareas

1. Crea un sistema para gestionar tareas usando archivos JSON.
2. Implementa las siguientes funciones:
   
   **`cargar_tareas(filename)`:**
   - Lee las tareas desde un archivo JSON
   - Si el archivo no existe, retorna una lista vacía
   
   **`guardar_tareas(filename, tareas)`:**
   - Guarda la lista de tareas en un archivo JSON con formato legible
   
   **`agregar_tarea(tareas, titulo, prioridad)`:**
   - Añade una nueva tarea con estructura: `{"id": ..., "titulo": ..., "prioridad": ..., "completada": False}`
   - El id debe ser autoincrementado
   
   **`mostrar_tareas(tareas)`:**
   - Muestra todas las tareas en formato legible
   
3. Prueba el sistema:
   - Carga las tareas (o crea lista vacía)
   - Añade 3 tareas con diferentes prioridades
   - Guarda en `tareas.json`
   - Muestra todas las tareas
