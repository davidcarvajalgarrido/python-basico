# 08. (Introducción) Manipulación de datos con pandas

- [Introducción](#introducción)
- [Instalación y conceptos: Series y DataFrame](#instalación-y-conceptos-series-y-dataframe)
- [Carga y guardado de datos](#carga-y-guardado-de-datos)
- [Exploración, filtrado, selección y agrupamiento](#exploración-filtrado-selección-y-agrupamiento)
- [Visualización básica](#visualización-básica)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Primera toma de contacto con pandas: instalación, objetos básicos, carga/guardado y operaciones esenciales. Enfoque introductorio y opcional.

## Instalación y conceptos: Series y DataFrame
pandas es una librería orientada a análisis de datos tabulares. Una `Series` es una secuencia unidimensional con índice; un `DataFrame` es una tabla bidimensional con columnas etiquetadas. Trabajarás con ellos para limpiar, transformar y resumir datos. Instala en tu entorno virtual y verifica la versión para reproducibilidad.

```
# Instalación en un entorno activo
python -m pip install pandas

import pandas as pd
s = pd.Series([10, 20, 30], name="valores")
df = pd.DataFrame({"nombre":["Ana","Luis"], "edad":[30,20]})
print(s)
print(df)
```

## Carga y guardado de datos
Cargar desde CSV y JSON es directo con `read_csv` y `read_json`. Controla la codificación, el separador y los tipos de columnas para evitar sorpresas. Guardar resultados con `to_csv` y `to_json` permite encadenar procesos. La elección de índice y la inferencia de tipos son decisiones tempranas que facilitan operaciones posteriores.

```
import pandas as pd
df = pd.read_csv("productos.csv", encoding="utf-8")
df.to_json("productos.json", orient="records", force_ascii=False)
```

## Exploración, filtrado, selección y agrupamiento
Explorar con `head`, `info` y `describe` te da una visión rápida de la estructura. Seleccionar columnas por etiqueta y filtrar filas por condiciones booleanas son operaciones diarias. `groupby` permite agregar por categorías y `agg` combina estadísticas múltiples. La clave es construir expresiones legibles y evitar mutaciones confusas encadenadas.

```
# Supón df con columnas: nombre, precio, categoria
print(df.head())
caros = df[df["precio"] > 50][["nombre","precio"]]
resumen = df.groupby("categoria")["precio"].agg(["count","mean","min","max"])
print(resumen)
```

## Visualización básica
pandas integra un interfaz simple hacia Matplotlib para gráficos rápidos. Aunque no reemplaza librerías específicas de visualización, es suficiente para inspecciones iniciales. Asegúrate de que los ejes y etiquetas comuniquen la idea y evita conclusiones sin verificar los datos subyacentes.

```
# Requiere matplotlib instalado
ax = df["precio"].plot(kind="hist", bins=10, title="Distribución de precios")
fig = ax.get_figure()
fig.tight_layout()
```

## Resumen del módulo
Has probado la mecánica esencial de pandas: crear objetos, cargar/guardar y operar con filtros y agrupamientos. Es suficiente para explorar datasets pequeños y preparar el terreno para análisis más profundos.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://pandas.pydata.org/docs/" target="_blank">Documentación de pandas</a>
- <a href="https://pandas.pydata.org/docs/user_guide/10min.html" target="_blank">Guía de inicio rápido</a>
- <a href="https://pandas.pydata.org/docs/reference/index.html" target="_blank">Referencia API</a>
