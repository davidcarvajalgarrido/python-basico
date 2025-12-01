# 04. Funciones

- [Introducción](#introducción)
- [Definición y ámbito](#definición-y-ámbito)
- [Parámetros y valores de retorno](#parámetros-y-valores-de-retorno)
- [Funciones integradas más útiles](#funciones-integradas-más-útiles)
- [Funciones de orden superior y recursión (introducción ligera)](#funciones-de-orden-superior-y-recursión-introducción-ligera)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Define funciones claras, gestiona parámetros y retornos, y conoce el potencial de las funciones como valores.

## Definición y ámbito
Una función encapsula un bloque reutilizable asociado a un nombre. El ámbito local se crea al entrar en la función y se destruye al salir. El intérprete resuelve nombres con la regla LEGB (Local, Enclosing, Global, Builtins). Evita modificar variables globales desde funciones, ya que reduce la claridad y dificulta las pruebas.

```
x = 10  # global

def f(y):
    x = y + 1   # sombra a la global
    return x

print(f(5), x)  # 6 10
```

## Parámetros y valores de retorno
Python admite parámetros posicionales, con nombre, con valores por defecto y empaquetado con `*args` y `**kwargs`. Los argumentos por defecto se evalúan una vez, en la definición; evita usar mutables como valor por defecto. Una función puede retornar múltiples valores mediante tuplas, lo que facilita desempaquetar resultados.

```
def conectar(host, puerto=5432, *, ssl=True):
    return (host, puerto, ssl)

h, p, s = conectar("db.local", ssl=False)
```

## Funciones integradas más útiles
`len`, `sum`, `min`, `max`, `sorted`, `any`, `all`, `range`, `enumerate`, `map`, `filter` y `print` son herramientas diarias. `sorted` acepta una función `key` para personalizar el criterio sin modificar los datos originales. Estas utilidades reducen código repetitivo y mejoran la expresividad.

```
datos = ["Ana", "luis", "Sofía"]
orden = sorted(datos, key=str.lower)
print(orden)
```

## Funciones de orden superior y recursión (introducción ligera)
En Python, las funciones son ciudadanos de primera clase: pueden pasarse como argumentos y devolverse como resultado. Esto permite componer comportamientos. La recursión es una técnica en la que una función se invoca a sí misma, pero debe usarse con criterio y una condición de parada clara. Para problemas de recorrido simple, los bucles suelen ser más directos.

```
def aplica(fn, valores):
    return [fn(v) for v in valores]

def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
```

## Resumen del módulo
Has aprendido a escribir funciones con firmas claras, a elegir parámetros adecuados y a aprovechar funciones integradas. Esta caja de herramientas hará que tu código sea más modular y fácil de probar.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions" target="_blank">Definición de funciones</a>
- <a href="https://docs.python.org/3/library/functions.html" target="_blank">Funciones integradas (builtins)</a>
