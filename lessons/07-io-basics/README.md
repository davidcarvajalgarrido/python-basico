# 07. Entrada y salida de datos

- [Introducción](#introducción)
- [Formateo de salida: str, repr y f-strings](#formateo-de-salida-str-repr-y-f-strings)
- [Archivos: modos, lectura, escritura y cursores](#archivos-modos-lectura-escritura-y-cursores)
- [CSV y JSON como formatos de intercambio](#csv-y-json-como-formatos-de-intercambio)
- [Nota responsable sobre `pickle`](#nota-responsable-sobre-`pickle`)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Formatea salidas legibles, lee y escribe archivos de texto y trabaja con formatos abiertos como CSV y JSON. Nota responsable sobre `pickle`.

## Formateo de salida: str, repr y f-strings
`str(obj)` produce una representación amigable para usuarios; `repr(obj)` intenta ser inequívoca para desarrolladores. Las f-strings interpolan expresiones con control de formato. Elegir entre `str` y `repr` depende del público y del contexto: logs, interfaces de línea de comandos o mensajes de error.

```
from datetime import datetime
ahora = datetime.now()
print(str(ahora))
print(repr(ahora))
valor = 12.3456
print(f"{valor:.2f}")
```

## Archivos: modos, lectura, escritura y cursores
Abre archivos con `with` para garantizar el cierre automático. Los modos comunes son `'r'` lectura, `'w'` escritura truncando, y `'a'` anexado. El cursor avanza a medida que lees; `seek` permite reposicionarlo. Especifica siempre la codificación al trabajar con texto para evitar sorpresas entre plataformas.

```
ruta = "datos.txt"
with open(ruta, "w", encoding="utf-8") as f:
    f.write("línea 1\nlínea 2\n")

with open(ruta, "r", encoding="utf-8") as f:
    print(f.readline().strip())
    f.seek(0)
    print(f.read())
```

## CSV y JSON como formatos de intercambio
CSV representa tablas en texto plano; JSON representa estructuras de diccionarios y listas. Son formatos abiertos, legibles y compatibles con múltiples herramientas. El módulo `csv` maneja delimitadores y comillas; `json` convierte entre objetos de Python y cadenas JSON.

```
import csv, json

filas = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Luis"},
]

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id","nombre"])
    w.writeheader()
    w.writerows(filas)

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(filas, f, ensure_ascii=False, indent=2)
```

## Nota responsable sobre `pickle`
`pickle` serializa objetos de Python de forma binaria y específica de versión. No debe usarse con datos no confiables: cargar un `pickle` puede ejecutar código arbitrario. Prefiere formatos abiertos para intercambio y reserva `pickle` para estados internos controlados dentro de una aplicación.

```
import pickle
datos = {"secreto": 42}
b = pickle.dumps(datos)
# Solo cargar si confías plenamente en la fuente:
_ = pickle.loads(b)
```

## Resumen del módulo
Sabes formatear salidas, trabajar con archivos de texto y usar CSV/JSON para intercambiar datos. `pickle` queda como herramienta de nicho bajo control estricto.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://docs.python.org/3/tutorial/inputoutput.html" target="_blank">Entrada/Salida</a>
- <a href="https://docs.python.org/3/library/json.html" target="_blank">Módulo `json`</a>
- <a href="https://docs.python.org/3/library/csv.html" target="_blank">Módulo `csv`</a>
