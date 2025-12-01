# 02. Tipos de objetos y operaciones básicas

- [Introducción](#introducción)
- [Números y operadores](#números-y-operadores)
- [Librería math](#librería-math)
- [Tipado dinámico](#tipado-dinámico)
- [Cadenas: inmutabilidad y métodos](#cadenas-inmutabilidad-y-métodos)
- [Colecciones: listas, tuplas, diccionarios](#colecciones-listas-tuplas-diccionarios)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Números, cadenas y colecciones. Comprenderás el tipado dinámico, la inmutabilidad y las operaciones fundamentales que usarás en todo el curso.

## Números y operadores
Python soporta enteros de precisión arbitraria, números en coma flotante y booleanos, además de tipos como `Decimal` o `Fraction` en módulos especializados. Las operaciones básicas incluyen suma, resta, multiplicación, división real y entera, módulo y potencia. Es importante distinguir entre `/` (división en coma flotante) y `//` (división entera), y recordar la precedencia de operadores.

Ejemplos:
```
a, b = 7, 3
print(a + b, a - b, a * b)     # 10 4 21
print(a / b, a // b, a % b)    # 2.333... 2 1
print(a ** b)                  # 343
```

## Librería math
El módulo `math` ofrece funciones numéricas de bajo nivel implementadas en C. Conviene importar solo lo que necesitas o el módulo completo según criterio de legibilidad. También expone constantes como `pi` y `e`. Para cálculos que requieren control de precisión decimal, explora `decimal`, y para cálculos racionales exactos, `fractions`.

```
import math

r = 2.5
area = math.pi * r ** 2
raiz = math.sqrt(16)
ang = math.degrees(math.atan2(1, 1))
print(area, raiz, ang)
```

## Tipado dinámico
En Python, el tipo va con el valor, no con el nombre. La misma variable puede referirse a objetos de distintos tipos a lo largo del tiempo. Esto otorga flexibilidad, pero exige disciplina al diseñar funciones y al validar entradas. Para comunicar expectativas, puedes usar anotaciones de tipo; no cambian la ejecución, pero ayudan con linters y editores.

```
x = 10
x = "diez"   # ahora es str
def duplica(n: int) -> int:
    return n * 2
```

## Cadenas: inmutabilidad y métodos
Las cadenas son inmutables: cualquier “cambio” crea una nueva cadena. Esta propiedad simplifica el razonamiento y evita efectos colaterales, pero influye en el rendimiento de concatenaciones repetidas, donde conviene usar `join`. Los métodos cubren búsqueda, recorte, sustitución y transformación de mayúsculas/minúsculas, entre otros. Las f-strings permiten interpolar expresiones de forma legible.

```
s = "  Python  "
t = s.strip().lower().replace("py", "Py")
msg = f"[{t}] tiene {len(t)} caracteres"
partes = ",".join(["a", "b", "c"])
print(msg, partes)
```

## Colecciones: listas, tuplas, diccionarios
Las listas son mutables y ordenadas; las tuplas son inmutables y útiles para agrupar valores heterogéneos; los diccionarios mapean claves a valores y son la base de muchas estructuras. Las operaciones típicas incluyen rebanado, comprensión de listas y acceso seguro a claves con `get`. La elección entre lista y tupla suele depender de si necesitas mutabilidad.

```
nums = [1, 2, 3]
nums.append(4)
cuadrados = [n*n for n in nums]

punto = (10, 20)  # tupla
usuario = {"id": 1, "nombre": "Ada"}
print(usuario.get("email", "n/a"))
```

## Resumen del módulo
Ya conoces los tipos fundamentales y cómo operarlos. La inmutabilidad de cadenas y tuplas te aporta seguridad; las listas y diccionarios ofrecen flexibilidad. Este vocabulario será clave para construir lógica de control en la siguiente lección.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://docs.python.org/3/library/stdtypes.html" target="_blank">Tipos y estructuras de datos</a>
- <a href="https://docs.python.org/3/library/math.html" target="_blank">Módulo math</a>
