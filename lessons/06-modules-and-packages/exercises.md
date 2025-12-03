# Lección 6 — Ejercicios

## Ejercicio 1: Crear y usar tu propio módulo

1. Crea un archivo llamado `operaciones.py` con dos funciones:
   - `cuadrado(n)`: retorna `n * n`
   - `cubo(n)`: retorna `n * n * n`
2. Crea otro archivo `main.py` que:
   - Importe el módulo `operaciones`
   - Use ambas funciones para calcular el cuadrado y cubo de 5
   - Muestre los resultados

## Ejercicio 2: Importar la calculadora

1. Usa el módulo `calculator.py` (que ya tienes en `resources/misc/`) desde otro archivo.
2. Crea un archivo `usar_calculadora.py` que:
   - Importe las funciones: `sumar`, `restar`, `multiplicar`, `dividir`
   - Realice las 4 operaciones con los números 20 y 4
   - Muestre todos los resultados

## Ejercicio 3: Módulos estándar - random

1. Crea un archivo `juego_dados.py` que use el módulo `random`.
2. Implementa una función `lanzar_dado()` que retorne un número aleatorio entre 1 y 6.
3. Implementa una función `jugar_ronda()` que:
   - Lance dos dados (uno para el jugador, otro para la computadora)
   - Determine quién ganó
   - Muestre el resultado
4. Llama a `jugar_ronda()` tres veces para simular 3 rondas.

## Ejercicio 4: Módulos estándar - datetime

1. Crea un archivo `info_fecha.py` que use el módulo `datetime`.
2. Crea una función `mostrar_info_fecha()` que:
   - Obtenga la fecha y hora actual
   - Muestre el día, mes, año
   - Muestre la hora, minutos, segundos
   - Calcule y muestre qué día de la semana es (0=Lunes, 6=Domingo)
3. Crea una función `dias_hasta_fin_de_ano()` que calcule cuántos días faltan para el 31 de diciembre.

## Ejercicio 5: Crear un paquete simple

1. Crea la siguiente estructura de directorios y archivos:
   ```
   mi_paquete/
   ├── __init__.py
   ├── matematicas.py
   └── textos.py
   ```

2. En `matematicas.py` crea:
   - `es_par(n)`: retorna `True` si n es par
   - `factorial(n)`: retorna el factorial de n

3. En `textos.py` crea:
   - `contar_vocales(texto)`: cuenta cuántas vocales tiene un texto
   - `invertir(texto)`: retorna el texto al revés

4. En `__init__.py` importa todas las funciones para que estén disponibles directamente desde `mi_paquete`.

5. Crea un archivo `test_paquete.py` fuera del paquete que:
   - Importe y use todas las funciones del paquete
   - Pruebe cada función con diferentes valores
