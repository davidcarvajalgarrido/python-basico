# 05. Control de excepciones

- [Introducción](#introducción)
- [Conceptos y flujo de errores](#conceptos-y-flujo-de-errores)
- [`try/except/else/finally`](#`try/except/else/finally`)
- [Lanzar (`raise`) y excepciones propias](#lanzar-`raise`-y-excepciones-propias)
- [Resumen del módulo](#resumen-del-módulo)
- [Recursos adicionales](#recursos-adicionales)

## Introducción
Comprende el flujo de errores y cómo capturarlos, propagarlos o transformarlos en mensajes útiles.

## Conceptos y flujo de errores
Una excepción interrumpe el flujo normal cuando ocurre una condición inesperada. Si no se captura, el programa termina mostrando un traceback que ayuda a localizar la causa. Decidir si capturar o dejar propagar depende del nivel donde sea más razonable manejar el problema. Capturas demasiado amplias ocultan fallos; capturas específicas con mensajes claros mejoran la experiencia del usuario.

## `try/except/else/finally`
El bloque `try` protege código susceptible de fallar. `except` maneja el error; `else` se ejecuta solo si no hubo excepción; `finally` siempre se ejecuta, haya o no error, y es ideal para liberar recursos. Es recomendable capturar la excepción concreta y registrar el detalle.

```
def lee_entero():
    try:
        n = int(input("Número: "))
    except ValueError as e:
        print("Entrada no válida:", e)
        return None
    else:
        print("OK, gracias")
        return n
    finally:
        print("Fin de la operación")
```

## Lanzar (`raise`) y excepciones propias
Cuando detectas una condición inválida, puedes lanzar una excepción para señalarla. Para casos de dominio, definir una excepción específica documenta mejor la intención y permite a los clientes capturarla de forma diferenciada. Hereda de `Exception` y provee un mensaje claro.

```
class PrecioInvalido(Exception):
    pass

def aplica_descuento(precio, porcentaje):
    if precio < 0 or not (0 <= porcentaje <= 100):
        raise PrecioInvalido("Revisa precio o porcentaje")
    return precio * (1 - porcentaje/100)
```

## Resumen del módulo
Has visto cómo pensar en el flujo de errores y cómo usar `try/except/else/finally` con responsabilidad. Definir excepciones propias te ayuda a comunicar reglas de negocio y a mantener el código robusto.

## Recursos adicionales
> **Enlaces externos**: Los enlaces se abren en la misma pestaña. Usa Ctrl+Click (Windows/Linux) o Cmd+Click (Mac) para abrirlos en pestaña nueva.

- <a href="https://docs.python.org/3/tutorial/errors.html" target="_blank">Excepciones</a>
- <a href="https://docs.python.org/3/library/exceptions.html" target="_blank">Jerarquía de excepciones</a>
