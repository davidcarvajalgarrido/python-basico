# 06. Módulos y paquetes

- [Introducción](#introducción)
- [Importación y namespaces](#importación-y-namespaces)
- [Crear módulos y paquetes](#crear-módulos-y-paquetes)
- [Librería estándar: visión general](#librería-estándar-visión-general)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Organiza código en archivos y carpetas, entiende los espacios de nombres y aprende a importar de forma explícita.

## Importación y namespaces
Importar es traer nombres desde un módulo a tu espacio actual. `import modulo` crea un nombre ligado al módulo; `from modulo import nombre` trae el objeto directamente. Prefiere importaciones explícitas y evita `from modulo import *` en código de producción, ya que enturbia el namespace y dificulta la lectura.

```
import math
from pathlib import Path

print(math.pi)
p = Path(".").resolve()
```

## Crear módulos y paquetes
Un módulo es un archivo `.py`. Un paquete es una carpeta con archivos `.py` que actúa como espacio de nombres. En versiones modernas no es obligatorio `__init__.py` para directorios tratados como paquetes, pero incluirlo hace el paquete explícito y facilita herramientas. Divide por responsabilidad y mantén interfaces claras entre módulos.

Estructura mínima:
```
myapp/
  __init__.py
  utils.py
  core/
    __init__.py
    negocio.py
```

## Librería estándar: visión general
La librería estándar ofrece utilidades para rutas (`pathlib`), fechas (`datetime`), colecciones especializadas (`collections`), expresiones regulares (`re`), JSON (`json`) y mucho más. Antes de instalar una dependencia, revisa si ya existe un módulo estándar que cubra tu necesidad; esto reduce riesgos y simplifica mantenimiento.

```
from datetime import date
from collections import Counter
import json

hoy = date.today()
cont = Counter("banana")
print(hoy, cont, json.dumps({"hoy": str(hoy)}))
```

## Resumen del módulo
Entiendes cómo agrupar código en módulos y paquetes, y cuándo preferir importaciones explícitas. Con la librería estándar tendrás soluciones fiables sin añadir dependencias externas.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://docs.python.org/3/tutorial/modules.html" target="_blank">Módulos y paquetes</a>
- <a href="https://docs.python.org/3/library/index.html" target="_blank">Librería estándar (visión general)</a>
