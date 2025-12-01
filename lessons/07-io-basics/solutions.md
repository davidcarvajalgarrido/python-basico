# Lección 7 — Soluciones

## Ejercicio 1: Solución: Exporta e importa JSON

```
import json
datos = [{"id":1,"ok":True},{"id":2,"ok":False}]
with open("items.json","w",encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)
with open("items.json","r",encoding="utf-8") as f:
    cargado = json.load(f)
print(cargado)
```

## Ejercicio 2: Solución: CSV con cabecera

```
import csv
filas = [
    {"id":1,"nombre":"Teclado","precio":19.9},
    {"id":2,"nombre":"Ratón","precio":9.5},
    {"id":3,"nombre":"Monitor","precio":129.0},
]
with open("productos.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id","nombre","precio"])
    w.writeheader()
    w.writerows(filas)

with open("productos.csv","r",encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        print(row["nombre"])
```

## Ejercicio 3: Solución: Reporte formateado

```
total = 1234.567
print(f"Total a pagar: {total:.2f} €")
```
