# 01. Introducción a Python

- [Introducción](#introducción)
- [¿Qué es Python y para qué sirve?](#qué-es-python-y-para-qué-sirve)
- [Instalación y herramientas básicas](#instalación-y-herramientas-básicas)
- [Sintaxis esencial e indentación](#sintaxis-esencial-e-indentación)
- [REPL y primeros scripts](#repl-y-primeros-scripts)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Contexto del lenguaje, instalación de herramientas y primeros pasos en el REPL y con scripts. Al final tendrás tu entorno listo y comprenderás la sintaxis mínima para ejecutar código.

## ¿Qué es Python y para qué sirve?
Python es un lenguaje de alto nivel, interpretado y con tipado dinámico. Esto significa que el intérprete ejecuta el código directamente sin un paso de compilación explícito y que los tipos se asocian a los valores en tiempo de ejecución. Su filosofía prioriza la legibilidad: el uso de indentación para delimitar bloques reduce el ruido visual y favorece un estilo coherente. Se utiliza en desarrollo web, scripting, ciencia de datos, automatización, pruebas y educación, gracias a una librería estándar amplia y a un ecosistema de paquetes muy activo.

Entre sus ventajas destacan la curva de aprendizaje suave, la portabilidad y la enorme comunidad. Entre las desventajas habituales se citan el rendimiento frente a lenguajes compilados y la gestión de entornos/paquetes cuando se mezclan proyectos. En la práctica, combinamos Python con herramientas como entornos virtuales y gestores de paquetes para mantener la productividad sin perder control.

## Instalación y herramientas básicas
Instalar Python desde el sitio oficial garantiza disponer del intérprete `python` y del gestor de paquetes `pip`. Tras la instalación, conviene verificar la versión y preparar un entorno virtual por proyecto para aislar dependencias. Un editor como VS Code o PyCharm aporta resaltado, autocompletado y depuración, lo cual acelera el aprendizaje y evita errores triviales.

Verifica la instalación y crea un entorno:
```
python --version
python -m venv .venv
# Activar el entorno (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
# Activar en macOS/Linux (bash/zsh)
source .venv/bin/activate
python -m pip install --upgrade pip
```

El REPL (Read–Eval–Print Loop) te permite experimentar rápidamente. Inícialo con `python` y prueba expresiones aritméticas o funciones integradas. Cuando una idea merece guardarse, pásala a un archivo `.py` y ejecútalo desde la terminal.

## Sintaxis esencial e indentación
En Python, la estructura del programa se define con la indentación. Cada bloque aumenta su sangría de forma consistente. No se usan llaves para agrupar; los dos puntos introducen bloques. Los nombres de variables siguen el estilo `snake_case` y los comentarios comienzan con `#`. Una línea puede continuar en la siguiente si está dentro de paréntesis o por el carácter `\`, aunque se recomienda lo primero por claridad.

Veamos un ejemplo mínimo que imprime un saludo y realiza una operación sencilla:
```
# hello.py
nombre = "Ada"
veces = 3
if veces > 0:
    print(f"Hola, {nombre}")
    print("!" * veces)
```
Ejecuta con:
```
python hello.py
```

## REPL y primeros scripts
El REPL es ideal para explorar funciones y probar fragmentos. Puedes obtener ayuda con `help(obj)` y ver el tipo de un valor con `type(valor)`. Para pasar del experimento a un script, crea un archivo y utiliza la convención `if __name__ == "__main__":` para separar definiciones de la ejecución directa. De esta forma, el archivo puede importarse como módulo sin ejecutar el bloque principal.

Ejemplo:
```
# app.py
def area_rectangulo(base, altura):
    return base * altura

if __name__ == "__main__":
    b = 5
    h = 2
    print("Área:", area_rectangulo(b, h))
```

## Resumen del módulo
Has instalado Python, probado el REPL y ejecutado tus primeros scripts. Te quedas con dos ideas clave: la indentación define la estructura y el REPL es tu laboratorio personal. A partir de aquí, empezarás a construir con tipos y operaciones para modelar datos de forma precisa.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://www.python.org/downloads/" target="_blank">Descarga e instalación de Python</a>
- <a href="https://docs.python.org/3/using/index.html" target="_blank">Usando Python en distintos sistemas</a>
- <a href="https://docs.python.org/3/tutorial/introduction.html" target="_blank">Tutorial oficial: introducción</a>
