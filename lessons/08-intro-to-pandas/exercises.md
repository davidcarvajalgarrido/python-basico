# Lección 8 — Ejercicios

## Ejercicio 1: Crear tu primer DataFrame

1. Importa pandas como `pd`.
2. Crea un DataFrame con información de 5 productos:
   - Columnas: `nombre`, `categoria`, `precio`, `stock`
   - Ejemplo de productos: Laptop, Mouse, Teclado, Monitor, Webcam
3. Muestra el DataFrame completo.
4. Muestra solo las primeras 3 filas usando `.head(3)`.
5. Muestra información básica del DataFrame con `.info()`.

## Ejercicio 2: Seleccionar y filtrar datos

1. Usa el DataFrame del ejercicio anterior.
2. Selecciona y muestra solo la columna `nombre`.
3. Selecciona y muestra las columnas `nombre` y `precio` juntas.
4. Filtra y muestra solo los productos con `precio > 50`.
5. Filtra y muestra los productos de la categoría "Periféricos" con `stock < 15`.

## Ejercicio 3: Leer y escribir archivos CSV

1. Crea un archivo CSV llamado `ventas.csv` con las siguientes columnas: `fecha`, `producto`, `cantidad`, `precio_unitario`.
2. Añade al menos 5 registros de ventas (puedes crear el archivo manualmente o con código).
3. Lee el archivo CSV con pandas: `pd.read_csv("ventas.csv")`.
4. Muestra las primeras filas del DataFrame.
5. Crea una nueva columna `total` que sea `cantidad * precio_unitario`.
6. Guarda el DataFrame modificado en un nuevo archivo `ventas_con_total.csv`.

## Ejercicio 4: Estadísticas y operaciones básicas

1. Usa el DataFrame de ventas del ejercicio anterior.
2. Calcula y muestra:
   - La suma total de la columna `total`
   - El promedio de `precio_unitario`
   - El valor máximo y mínimo de `cantidad`
3. Usa `.describe()` para ver estadísticas descriptivas de todas las columnas numéricas.
4. Cuenta cuántas ventas hay de cada producto usando `.value_counts()` en la columna `producto`.

## Ejercicio 5: Agrupación y análisis

1. Crea un DataFrame con información de estudiantes:
   - Columnas: `nombre`, `curso`, `asignatura`, `nota`
   - Al menos 8 registros con diferentes estudiantes, cursos y asignaturas
2. Agrupa por `curso` y calcula la nota media de cada curso.
3. Agrupa por `asignatura` y calcula:
   - La nota media
   - La nota máxima
   - La cantidad de estudiantes
4. Encuentra qué estudiante tiene la nota más alta y en qué asignatura.
5. Guarda el DataFrame completo en formato JSON (`estudiantes.json`).
