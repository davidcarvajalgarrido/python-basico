# Lección 6 — Soluciones

## Ejercicio 1: Solución: Crear y usar tu propio módulo

**Archivo: `operaciones.py`**
```python
def cuadrado(n):
    """Retorna el cuadrado de n."""
    return n * n


def cubo(n):
    """Retorna el cubo de n."""
    return n * n * n
```

**Archivo: `main.py`**
```python
import operaciones

numero = 5

resultado_cuadrado = operaciones.cuadrado(numero)
resultado_cubo = operaciones.cubo(numero)

print(f"El cuadrado de {numero} es: {resultado_cuadrado}")
print(f"El cubo de {numero} es: {resultado_cubo}")
```

## Ejercicio 2: Solución: Importar la calculadora

**Archivo: `usar_calculadora.py`**
```python
# Asumiendo que calculator.py está en resources/misc/
# Puedes copiar calculator.py al mismo directorio o ajustar el import

from calculator import sumar, restar, multiplicar, dividir

num1 = 20
num2 = 4

print(f"=== Calculadora con {num1} y {num2} ===")
print(f"Suma:           {num1} + {num2} = {sumar(num1, num2)}")
print(f"Resta:          {num1} - {num2} = {restar(num1, num2)}")
print(f"Multiplicación: {num1} × {num2} = {multiplicar(num1, num2)}")
print(f"División:       {num1} ÷ {num2} = {dividir(num1, num2)}")
```

## Ejercicio 3: Solución: Módulos estándar - random

**Archivo: `juego_dados.py`**
```python
import random

def lanzar_dado():
    """Retorna un número aleatorio entre 1 y 6."""
    return random.randint(1, 6)


def jugar_ronda():
    """Simula una ronda del juego de dados."""
    dado_jugador = lanzar_dado()
    dado_computadora = lanzar_dado()
    
    print(f"\n🎲 Jugador: {dado_jugador} | Computadora: {dado_computadora}")
    
    if dado_jugador > dado_computadora:
        print("✓ ¡Ganaste!")
    elif dado_jugador < dado_computadora:
        print("✗ Ganó la computadora")
    else:
        print("➖ Empate")


# Jugar 3 rondas
print("=== JUEGO DE DADOS ===")
for i in range(1, 4):
    print(f"\n--- Ronda {i} ---")
    jugar_ronda()
```

## Ejercicio 4: Solución: Módulos estándar - datetime

**Archivo: `info_fecha.py`**
```python
from datetime import datetime

def mostrar_info_fecha():
    """Muestra información detallada de la fecha y hora actual."""
    ahora = datetime.now()
    
    print("=== INFORMACIÓN DE FECHA Y HORA ===")
    print(f"Fecha: {ahora.day}/{ahora.month}/{ahora.year}")
    print(f"Hora: {ahora.hour}:{ahora.minute}:{ahora.second}")
    
    # Días de la semana
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia_num = ahora.weekday()
    print(f"Día de la semana: {dias_semana[dia_num]}")


def dias_hasta_fin_de_ano():
    """Calcula cuántos días faltan hasta el 31 de diciembre."""
    hoy = datetime.now()
    fin_de_ano = datetime(hoy.year, 12, 31)
    
    diferencia = fin_de_ano - hoy
    dias_restantes = diferencia.days
    
    print(f"\nFaltan {dias_restantes} días para fin de año")
    return dias_restantes


# Ejecutar las funciones
mostrar_info_fecha()
dias_hasta_fin_de_ano()
```

## Ejercicio 5: Solución: Crear un paquete simple

**Estructura de archivos:**
```
mi_paquete/
├── __init__.py
├── matematicas.py
└── textos.py
```

**Archivo: `mi_paquete/matematicas.py`**
```python
def es_par(n):
    """Retorna True si n es par."""
    return n % 2 == 0


def factorial(n):
    """Calcula el factorial de n."""
    if n <= 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado
```

**Archivo: `mi_paquete/textos.py`**
```python
def contar_vocales(texto):
    """Cuenta cuántas vocales tiene el texto."""
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    
    for letra in texto:
        if letra in vocales:
            contador += 1
    
    return contador


def invertir(texto):
    """Retorna el texto al revés."""
    return texto[::-1]
```

**Archivo: `mi_paquete/__init__.py`**
```python
# Importar todas las funciones para que estén disponibles desde el paquete
from .matematicas import es_par, factorial
from .textos import contar_vocales, invertir

# Opcional: definir qué se exporta cuando se hace "from mi_paquete import *"
__all__ = ['es_par', 'factorial', 'contar_vocales', 'invertir']
```

**Archivo: `test_paquete.py` (fuera del paquete)**
```python
import mi_paquete

print("=== PROBANDO EL PAQUETE ===\n")

# Probar funciones de matemáticas
print("--- Matemáticas ---")
print(f"¿Es 8 par? {mi_paquete.es_par(8)}")
print(f"¿Es 7 par? {mi_paquete.es_par(7)}")
print(f"Factorial de 5: {mi_paquete.factorial(5)}")
print(f"Factorial de 0: {mi_paquete.factorial(0)}")

# Probar funciones de textos
print("\n--- Textos ---")
texto = "Hola Python"
print(f"Texto: '{texto}'")
print(f"Vocales: {mi_paquete.contar_vocales(texto)}")
print(f"Invertido: '{mi_paquete.invertir(texto)}'")

texto2 = "Programación"
print(f"\nTexto: '{texto2}'")
print(f"Vocales: {mi_paquete.contar_vocales(texto2)}")
print(f"Invertido: '{mi_paquete.invertir(texto2)}'")
```

**Forma alternativa de importar (en `test_paquete.py`):**
```python
from mi_paquete import es_par, factorial, contar_vocales, invertir

# Ahora puedes usar las funciones directamente sin el prefijo mi_paquete.
print(es_par(10))
print(factorial(4))
print(contar_vocales("Hola"))
print(invertir("Python"))
```
