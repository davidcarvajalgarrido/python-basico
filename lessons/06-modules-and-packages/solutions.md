# Lección 6 — Soluciones

## Ejercicio 1: Solución: Tu primer paquete

```
# calc/__init__.py  (puede estar vacío)
# calc/arit.py
def suma(a, b): return a + b
def resta(a, b): return a - b

# main.py
from calc import arit
print(arit.suma(2,3), arit.resta(5,1))
```

## Ejercicio 2: Solución: Uso de pathlib

```
from pathlib import Path
for p in Path(".").glob("*.py"):
    print(p.name)
```

## Ejercicio 3: Solución: Counter en acción

```
from collections import Counter
texto = "abracadabra"
top3 = Counter(texto).most_common(3)
print(top3)
```
