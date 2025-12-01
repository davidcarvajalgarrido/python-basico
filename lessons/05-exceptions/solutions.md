# Lección 5 — Soluciones

## Ejercicio 1: Solución: Conversor robusto

```
def to_int(s):
    try:
        return int(s)
    except ValueError as e:
        print("No entero:", e)
        return None
```

## Ejercicio 2: Solución: Validador de descuentos

```
class DescuentoError(Exception):
    pass

def aplica_descuento(precio, porcentaje):
    if not (0 <= porcentaje <= 100):
        raise DescuentoError("Porcentaje fuera de rango")
    return precio * (1 - porcentaje/100)
```

## Ejercicio 3: Solución: Lectura con finally

```
def demo():
    f = None
    try:
        f = open(__file__, "r", encoding="utf-8")
        return f.readline()
    finally:
        if f:
            print("Cerrando recurso")
            f.close()
```
