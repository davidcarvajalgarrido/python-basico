# Lección 5 — Ejercicios

## Ejercicio 1: División segura

1. Crea una función `dividir_seguro(a, b)` que intente dividir `a` entre `b`.
2. Si `b` es cero, captura la excepción `ZeroDivisionError` y retorna `None`.
3. Si la división es exitosa, retorna el resultado.
4. Prueba la función con: `dividir_seguro(10, 2)` y `dividir_seguro(10, 0)`.

## Ejercicio 2: Conversión de tipos con excepciones

1. Crea una función `sumar_numeros(texto1, texto2)` que intente convertir dos strings a enteros y sumarlos.
2. Usa `try-except` para capturar `ValueError` si alguno de los textos no es un número válido.
3. Si hay error, muestra un mensaje y retorna `None`.
4. Prueba con: `sumar_numeros("5", "10")` y `sumar_numeros("5", "abc")`.

## Ejercicio 3: Acceso seguro a listas y diccionarios

1. Crea una función `obtener_dato(estructura, clave_o_indice)` que:
   - Intente acceder a un elemento de una lista (por índice) o diccionario (por clave)
   - Capture tanto `IndexError` como `KeyError`
   - Retorne el valor si existe, o `None` si no
2. Prueba con: 
   - Una lista: `[10, 20, 30]` con índice `1` y con índice `10`
   - Un diccionario: `{"nombre": "Ana", "edad": 25}` con clave `"nombre"` y con clave `"email"`

## Ejercicio 4: Uso de else y finally

1. Crea una función `procesar_archivo(nombre_archivo)` que simule el procesamiento de un archivo.
2. Usa una estructura `try-except-else-finally`:
   - En el `try`: verifica que el nombre del archivo termine en `.txt`, si no lanza un `ValueError`
   - En el `except`: captura el `ValueError` y muestra "Error: El archivo debe ser .txt"
   - En el `else`: muestra "Archivo procesado correctamente"
   - En el `finally`: muestra "Operación finalizada"
3. Prueba con: `"datos.txt"` y `"imagen.png"`.

## Ejercicio 5: Validación con excepciones propias

1. Crea una función `calcular_descuento(precio, porcentaje_descuento)` que:
   - Verifique que el precio sea positivo, si no lanza `ValueError("El precio debe ser positivo")`
   - Verifique que el porcentaje esté entre 0 y 100, si no lanza `ValueError("El descuento debe estar entre 0 y 100")`
   - Si todo es correcto, calcule y retorne el precio final: `precio * (1 - porcentaje_descuento / 100)`
2. Envuelve la llamada en un `try-except` para capturar los errores y mostrarlos.
3. Prueba con:
   - `calcular_descuento(100, 20)` → debe funcionar
   - `calcular_descuento(-50, 20)` → error de precio negativo
   - `calcular_descuento(100, 150)` → error de porcentaje inválido
