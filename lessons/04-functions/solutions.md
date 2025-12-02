# Lección 4 — Soluciones

## Ejercicio 1: Solución: Función simple - Saludar

```python
def saludar(nombre):
    print(f"¡Hola, {nombre}! ¿Cómo estás?")

# Pruebas
saludar("Ana")
saludar("Carlos")
saludar("María")
```

## Ejercicio 2: Solución: Función con return - Operaciones básicas

```python
def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

# Calculamos (5 + 3) * 2
resultado_suma = sumar(5, 3)
resultado_final = multiplicar(resultado_suma, 2)

print(f"(5 + 3) * 2 = {resultado_final}")

# O en una sola línea:
print(f"Resultado: {multiplicar(sumar(5, 3), 2)}")
```

## Ejercicio 3: Solución: Función con condicionales - Verificar paridad

```python
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    # Forma más corta: return numero % 2 == 0

# Pruebas
numeros_prueba = [4, 7, 10, 15, 22]

for num in numeros_prueba:
    resultado = es_par(num)
    print(f"¿{num} es par? {resultado}")
```

## Ejercicio 4: Solución: Función con múltiples condicionales - Calificación

```python
def obtener_calificacion(nota):
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"

# Pruebas
notas = [4.5, 6, 7.5, 9.5, 10]

for nota in notas:
    calificacion = obtener_calificacion(nota)
    print(f"Nota {nota}: {calificacion}")
```

## Ejercicio 5: Solución: Función con strings - Formatear nombre

```python
def formatear_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.upper()}"

# Pruebas
print(formatear_nombre("juan", "pérez"))
print(formatear_nombre("ana", "garcía"))
print(formatear_nombre("carlos", "lópez"))
```

## Ejercicio 6: Solución: Función con listas - Calcular promedio

```python
def calcular_promedio(numeros):
    suma = 0
    for num in numeros:
        suma += num
    
    promedio = suma / len(numeros)
    return promedio
    
    # Forma más corta: return sum(numeros) / len(numeros)

# Prueba
notas = [8, 7.5, 9, 6.5, 8.5]
promedio = calcular_promedio(notas)
print(f"El promedio de {notas} es: {promedio}")
```

## Ejercicio 7: Solución: Función con listas - Filtrar números

```python
def obtener_pares(lista):
    pares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    
    return pares

# Prueba
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = obtener_pares(numeros)
print(f"Números originales: {numeros}")
print(f"Números pares: {numeros_pares}")
```

## Ejercicio 8: Solución: Función con diccionarios - Información de persona

```python
def crear_persona(nombre, edad, ciudad):
    persona = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }
    return persona

# Crear varias personas
lista_personas = []

persona1 = crear_persona("Ana", 25, "Madrid")
persona2 = crear_persona("Carlos", 30, "Barcelona")
persona3 = crear_persona("María", 28, "Valencia")

lista_personas.append(persona1)
lista_personas.append(persona2)
lista_personas.append(persona3)

# Mostrar las personas
for persona in lista_personas:
    print(f"{persona['nombre']} tiene {persona['edad']} años y vive en {persona['ciudad']}")
```

## Ejercicio 9: Solución: Función con diccionarios - Buscar por clave

```python
def obtener_producto_mas_caro(productos):
    producto_mas_caro = productos[0]  # Asumimos que el primero es el más caro
    
    for producto in productos:
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
    
    return producto_mas_caro

# Prueba
productos = [
    {"nombre": "Laptop", "precio": 800},
    {"nombre": "Mouse", "precio": 20},
    {"nombre": "Teclado", "precio": 50}
]

mas_caro = obtener_producto_mas_caro(productos)
print(f"El producto más caro es: {mas_caro['nombre']} con precio de {mas_caro['precio']}€")
```

## Ejercicio 10: Solución: Práctica integradora - Sistema de gestión de estudiantes

```python
def agregar_estudiante(lista_estudiantes, nombre, notas):
    # Calcular el promedio
    promedio = sum(notas) / len(notas)
    
    # Crear el diccionario del estudiante
    estudiante = {
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio
    }
    
    # Añadir a la lista
    lista_estudiantes.append(estudiante)
    
    return lista_estudiantes


def obtener_mejor_estudiante(lista_estudiantes):
    mejor_estudiante = lista_estudiantes[0]
    
    for estudiante in lista_estudiantes:
        if estudiante["promedio"] > mejor_estudiante["promedio"]:
            mejor_estudiante = estudiante
    
    return mejor_estudiante


# Probar el sistema
estudiantes = []

# Añadir estudiantes
estudiantes = agregar_estudiante(estudiantes, "Ana", [8, 7.5, 9, 8.5])
estudiantes = agregar_estudiante(estudiantes, "Carlos", [6, 7, 6.5, 7.5])
estudiantes = agregar_estudiante(estudiantes, "María", [9, 9.5, 8.5, 9])

# Mostrar todos los estudiantes
print("=== Lista de estudiantes ===")
for est in estudiantes:
    print(f"{est['nombre']}: Notas {est['notas']}, Promedio: {est['promedio']:.2f}")

# Obtener el mejor estudiante
mejor = obtener_mejor_estudiante(estudiantes)
print(f"\n🏆 El mejor estudiante es: {mejor['nombre']} con promedio de {mejor['promedio']:.2f}")
```
