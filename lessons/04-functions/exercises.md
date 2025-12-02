# Lección 4 — Ejercicios

## Ejercicio 1: Función simple - Saludar

1. Crea una función `saludar(nombre)` que reciba un nombre como parámetro.
2. La función debe imprimir: "¡Hola, [nombre]! ¿Cómo estás?".
3. Llama a la función con diferentes nombres.

## Ejercicio 2: Función con return - Operaciones básicas

1. Crea una función `sumar(a, b)` que reciba dos números y retorne su suma.
2. Crea otra función `multiplicar(a, b)` que retorne el producto de dos números.
3. Usa ambas funciones para calcular: `(5 + 3) * 2` y muestra el resultado.

## Ejercicio 3: Función con condicionales - Verificar paridad

1. Crea una función `es_par(numero)` que reciba un número.
2. La función debe retornar `True` si el número es par, `False` si es impar.
3. Prueba la función con varios números y muestra los resultados.

## Ejercicio 4: Función con múltiples condicionales - Calificación

1. Crea una función `obtener_calificacion(nota)` que reciba una nota numérica (0-10).
2. La función debe retornar:
   - "Suspenso" si nota < 5
   - "Aprobado" si nota entre 5-6
   - "Notable" si nota entre 7-8
   - "Sobresaliente" si nota entre 9-10
3. Prueba con diferentes notas.

## Ejercicio 5: Función con strings - Formatear nombre

1. Crea una función `formatear_nombre(nombre, apellido)` que reciba nombre y apellido.
2. La función debe retornar el nombre completo en formato: "Apellido, Nombre" (en mayúsculas).
3. Ejemplo: `formatear_nombre("juan", "pérez")` → `"PÉREZ, JUAN"`.

## Ejercicio 6: Función con listas - Calcular promedio

1. Crea una función `calcular_promedio(numeros)` que reciba una lista de números.
2. La función debe retornar el promedio (suma de todos dividido entre la cantidad).
3. Prueba con la lista `[8, 7.5, 9, 6.5, 8.5]`.

## Ejercicio 7: Función con listas - Filtrar números

1. Crea una función `obtener_pares(lista)` que reciba una lista de números.
2. La función debe retornar una nueva lista solo con los números pares.
3. Prueba con `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.

## Ejercicio 8: Función con diccionarios - Información de persona

1. Crea una función `crear_persona(nombre, edad, ciudad)` que reciba estos tres parámetros.
2. La función debe retornar un diccionario con las claves: `"nombre"`, `"edad"`, `"ciudad"`.
3. Crea varias personas y guárdalas en una lista.

## Ejercicio 9: Función con diccionarios - Buscar por clave

1. Crea una función `obtener_producto_mas_caro(productos)` que reciba una lista de diccionarios.
2. Cada diccionario representa un producto con: `{"nombre": "...", "precio": ...}`.
3. La función debe retornar el diccionario del producto con el precio más alto.
4. Prueba con: `[{"nombre": "Laptop", "precio": 800}, {"nombre": "Mouse", "precio": 20}, {"nombre": "Teclado", "precio": 50}]`.

## Ejercicio 10: Práctica integradora - Sistema de gestión de estudiantes

1. Crea una función `agregar_estudiante(lista_estudiantes, nombre, notas)` que:
   - Reciba una lista de estudiantes, un nombre y una lista de notas
   - Cree un diccionario con: `{"nombre": ..., "notas": ..., "promedio": ...}`
   - Calcule el promedio de las notas
   - Añada el estudiante a la lista
   - Retorne la lista actualizada

2. Crea una función `obtener_mejor_estudiante(lista_estudiantes)` que:
   - Reciba la lista de estudiantes
   - Retorne el diccionario del estudiante con mayor promedio

3. Prueba el sistema:
   - Crea una lista vacía de estudiantes
   - Añade 3 estudiantes con diferentes notas
   - Muestra quién es el mejor estudiante
