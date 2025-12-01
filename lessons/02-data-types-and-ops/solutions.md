# Lección 2 — Soluciones

## Ejercicio 1: Solución: Cálculos y redondeo

```
import math
r = 3.1415
area = math.pi * r**2
print(f"{area:.3f}")
print(f"Área: {area:.3f} u²")
```

## Ejercicio 2: Solución: Normalización de texto

```
s = "  PyTHon,básico , CURSO "
normal = s.strip().lower().replace(" ", "")
print(normal)                # "python,básico,curso"
lista = normal.split(",")
print(lista)
```

## Ejercicio 3: Solución: Diccionario de conteos

```
datos = ['rojo','azul','rojo','verde','azul','rojo']
conteos = {}
for color in datos:
    conteos[color] = conteos.get(color, 0) + 1
print(conteos)  # {'rojo': 3, 'azul': 2, 'verde': 1}
```
