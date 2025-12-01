# 03. Estructuras de control e iteración

- [Introducción](#introducción)
- [Condicional if y operadores lógicos](#condicional-if-y-operadores-lógicos)
- [Bucles while y for](#bucles-while-y-for)
- [Iteradores y recorrido de colecciones](#iteradores-y-recorrido-de-colecciones)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Construye lógica con condicionales y bucles, y recorre colecciones de forma segura y expresiva.

## Condicional if y operadores lógicos
El condicional `if` dirige el flujo según condiciones booleanas, combinadas con `and`, `or` y `not`. Las comparaciones encadenadas como `0 < x < 10` mejoran la legibilidad. Recuerda que valores vacíos (`""`, `0`, `[]`, `{}`) se evalúan como falsos.

```
edad = 17
if 0 < edad < 18:
    print("Menor de edad")
elif edad >= 65:
    print("Mayor")
else:
    print("Adulto")
```

## Bucles while y for
Usa `for` para iterar sobre colecciones y `while` cuando la condición de parada no depende de un iterable fijo. `break` interrumpe el bucle y `continue` salta a la siguiente iteración. El bloque `else` en bucles se ejecuta si no hubo `break`, útil para búsquedas.

```
objetivo = 7
for n in [1, 3, 5, 7, 9]:
    if n == objetivo:
        print("Encontrado")
        break
else:
    print("No encontrado")
```

## Iteradores y recorrido de colecciones
Un iterable produce elementos; un iterador recuerda su posición. Muchas APIs aceptan cualquier iterable, lo que permite componer generadores y comprensiones. Funciones como `enumerate` y `range` enriquecen el recorrido, y la comprensión de listas permite transformar y filtrar de forma concisa, manteniendo la claridad cuando la expresión es corta.

```
letras = ["a", "b", "c"]
for i, ch in enumerate(letras, start=1):
    print(i, ch)

pares = [n for n in range(10) if n % 2 == 0]
```

## Resumen del módulo
Dominas la toma de decisiones y los patrones de iteración más frecuentes. El siguiente paso es encapsular lógica repetida en funciones con firmas claras.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://docs.python.org/3/tutorial/controlflow.html" target="_blank">Flujo de control</a>
- <a href="https://docs.python.org/3/library/stdtypes.html#iterator-types" target="_blank">Iteradores e iterables</a>
