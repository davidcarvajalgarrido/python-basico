# Lección 2 — Soluciones

## Ejercicio 1: Variables y tipos básicos

```python
nombre = "Ana"
edad = 25
altura = 1.68

print(type(nombre))   # <class 'str'>
print(type(edad))     # <class 'int'>
print(type(altura))   # <class 'float'>

mensaje = nombre + " tiene " + str(edad) + " años"
print(mensaje)
```

## Ejercicio 2: Operadores aritméticos

```python
a = 17
b = 5

print("Suma:", a + b)              # 22
print("Resta:", a - b)             # 12
print("Multiplicación:", a * b)    # 85
print("División:", a / b)          # 3.4
print("División entera:", a // b)  # 3
print("Módulo:", a % b)            # 2
print("Potencia:", a ** b)         # 1419857
```

## Ejercicio 3: Trabajando con strings

```python
texto = "  PYTHON es Genial  "

# Normalizar
texto_limpio = texto.strip().lower()
print(texto_limpio)  # "python es genial"

# Reemplazar
texto_nuevo = texto_limpio.replace("genial", "increíble")
print(texto_nuevo)  # "python es increíble"

# Dividir
palabras = texto_nuevo.split(" ")
print(palabras)  # ['python', 'es', 'increíble']
```

## Ejercicio 4: Listas - operaciones básicas

```python
frutas = ["manzana", "pera", "plátano"]

frutas.append("naranja")
print(frutas)  # ['manzana', 'pera', 'plátano', 'naranja']

frutas.insert(1, "fresa")
print(frutas)  # ['manzana', 'fresa', 'pera', 'plátano', 'naranja']

frutas.remove("pera")
print(frutas)  # ['manzana', 'fresa', 'plátano', 'naranja']

print("Tercer elemento:", frutas[2])  # plátano
print("Longitud:", len(frutas))       # 4
```

## Ejercicio 5: Diccionarios - gestión de datos

```python
alumno = {
    "nombre": "Carlos",
    "edad": 20,
    "curso": "Python Básico"
}

alumno["nota"] = 8.5
print(alumno)

alumno["edad"] = alumno["edad"] + 1
print(alumno["edad"])  # 21

print("Claves:", alumno.keys())
# dict_keys(['nombre', 'edad', 'curso', 'nota'])

print("¿Existe email?", "email" in alumno)  # False
```

## Ejercicio 6: Tuplas - datos inmutables

```python
coordenadas = (10.5, 20.3, 5.8)

print("Coordenada Y:", coordenadas[1])  # 20.3

# coordenadas[0] = 15  # TypeError: 'tuple' object does not support item assignment

x, y, z = coordenadas
print("x=", x, "y=", y, "z=", z)
```

## Ejercicio 7: Conjuntos - elementos únicos

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Unión:", a | b)          # {1, 2, 3, 4, 5, 6, 7, 8}
print("Intersección:", a & b)   # {4, 5}
print("Diferencia:", a - b)     # {1, 2, 3}

a.add(9)
a.remove(1)
print(a)  # {2, 3, 4, 5, 9}
```

## Ejercicio 8: Conversión entre tipos

```python
lista_original = [1, 2, 2, 3, 3, 3]
conjunto_unicos = set(lista_original)
print(conjunto_unicos)  # {1, 2, 3}

lista_ordenada = sorted(list(conjunto_unicos))
print(lista_ordenada)  # [1, 2, 3]

claves = ["a", "b", "c"]
valores = [1, 2, 3]
diccionario = dict(zip(claves, valores))
print(diccionario)  # {'a': 1, 'b': 2, 'c': 3}
```

## Ejercicio 9: Operadores de comparación y lógicos

```python
x = 10
y = 20

print(x > y)                      # False
print(x > 5 and x < 15)          # True
print(y == 20 or x < 5)          # True
```

## Ejercicio 10: Práctica integradora

```python
productos = [
    {"nombre": "Teclado", "precio": 25.50, "stock": 10},
    {"nombre": "Ratón", "precio": 12.00, "stock": 25},
    {"nombre": "Monitor", "precio": 150.00, "stock": 5}
]

productos.append({"nombre": "Webcam", "precio": 45.00, "stock": 8})

nombres = []
for producto in productos:
    nombres.append(producto["nombre"])
print("Productos:", nombres)

total = 0
for producto in productos:
    total = total + producto["precio"]
print("Precio total:", total)  # 232.5
```
