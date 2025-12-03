# Lección 5 — Soluciones

## Ejercicio 1: Solución: División segura

```python
def dividir_seguro(a, b):
    """Divide dos números manejando la división por cero."""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print(f"Error: No se puede dividir {a} entre 0")
        return None

# Pruebas
print(dividir_seguro(10, 2))   # 5.0
print(dividir_seguro(10, 0))   # Error y None
```

## Ejercicio 2: Solución: Conversión de tipos con excepciones

```python
def sumar_numeros(texto1, texto2):
    """Convierte dos strings a números y los suma."""
    try:
        num1 = int(texto1)
        num2 = int(texto2)
        resultado = num1 + num2
        return resultado
    except ValueError:
        print(f"Error: '{texto1}' o '{texto2}' no son números válidos")
        return None

# Pruebas
print(sumar_numeros("5", "10"))    # 15
print(sumar_numeros("5", "abc"))   # Error y None
```

## Ejercicio 3: Solución: Acceso seguro a listas y diccionarios

```python
def obtener_dato(estructura, clave_o_indice):
    """Accede de forma segura a elementos de listas o diccionarios."""
    try:
        valor = estructura[clave_o_indice]
        return valor
    except (IndexError, KeyError):
        print(f"Error: No se encontró '{clave_o_indice}' en la estructura")
        return None

# Pruebas con lista
mi_lista = [10, 20, 30]
print(obtener_dato(mi_lista, 1))    # 20
print(obtener_dato(mi_lista, 10))   # Error y None

# Pruebas con diccionario
mi_dict = {"nombre": "Ana", "edad": 25}
print(obtener_dato(mi_dict, "nombre"))   # "Ana"
print(obtener_dato(mi_dict, "email"))    # Error y None
```

## Ejercicio 4: Solución: Uso de else y finally

```python
def procesar_archivo(nombre_archivo):
    """Simula el procesamiento de un archivo con manejo completo de excepciones."""
    print(f"\nProcesando: {nombre_archivo}")
    
    try:
        if not nombre_archivo.endswith(".txt"):
            raise ValueError("El archivo debe tener extensión .txt")
        
        # Aquí iría el procesamiento real del archivo
        
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    else:
        # Solo se ejecuta si NO hubo excepción
        print("✓ Archivo procesado correctamente")
    
    finally:
        # Siempre se ejecuta
        print("→ Operación finalizada")

# Pruebas
procesar_archivo("datos.txt")
procesar_archivo("imagen.png")
```

## Ejercicio 5: Solución: Validación con excepciones propias

```python
def calcular_descuento(precio, porcentaje_descuento):
    """Calcula el precio final aplicando un descuento con validaciones."""
    # Validar precio
    if precio < 0:
        raise ValueError("El precio debe ser positivo")
    
    # Validar porcentaje
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    
    # Calcular precio final
    precio_final = precio * (1 - porcentaje_descuento / 100)
    return precio_final


# Pruebas con manejo de excepciones
print("--- Caso 1: Válido ---")
try:
    resultado = calcular_descuento(100, 20)
    print(f"Precio final: {resultado}€")
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Caso 2: Precio negativo ---")
try:
    resultado = calcular_descuento(-50, 20)
    print(f"Precio final: {resultado}€")
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Caso 3: Porcentaje inválido ---")
try:
    resultado = calcular_descuento(100, 150)
    print(f"Precio final: {resultado}€")
except ValueError as e:
    print(f"Error: {e}")
```
