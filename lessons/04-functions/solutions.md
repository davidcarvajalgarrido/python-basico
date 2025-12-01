# Lección 4 — Soluciones

## Ejercicio 1: Solución: Normalizador

```
def normaliza(texto, *, lower=True, trim=True):
    if trim:
        texto = texto.strip()
    if lower:
        texto = texto.lower()
    return texto

print(normaliza("  Hola PYTHON  "))
print(normaliza("  Hola PYTHON  ", lower=False))
```

## Ejercicio 2: Solución: Orden personalizado

```
datos = [("Ana", 30), ("luis", 20), ("Sofía", 20)]
datos_orden = sorted(datos, key=lambda t: (t[1], t[0].lower()))
print(datos_orden)
```

## Ejercicio 3: Solución: Factorial con validación

```
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser ≥ 0")
    return 1 if n <= 1 else n * factorial(n-1)

print(factorial(5))  # 120
```
