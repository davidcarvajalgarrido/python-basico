# Lección 3 — Soluciones

## Ejercicio 1: Solución: F-strings básicos

```python
nombre = "Ana"
edad = 25
ciudad = "Madrid"

print(f"Hola, me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

precio = 19.99
print(f"El precio es {precio}€")
```

## Ejercicio 2: Solución: F-strings con operaciones

```python
base = 5
altura = 3

print(f"El área del rectángulo es: {base * altura}")

temperatura_celsius = 25
print(f"{temperatura_celsius}°C equivalen a {temperatura_celsius * 9/5 + 32}°F")
```

## Ejercicio 3: Solución: Condicionales simples

```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

nota = 7.5

if nota >= 5:
    print("Has aprobado")
else:
    print("Has suspendido")
```

## Ejercicio 4: Solución: Condicionales múltiples - Clasificación de notas

```python
nota = 8.5

if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
```

## Ejercicio 5: Solución: Condicionales múltiples - Calculadora de descuentos

```python
precio = 100
cantidad = 15

if cantidad < 10:
    descuento = 0
elif cantidad <= 50:
    descuento = 0.10
else:
    descuento = 0.20

precio_final = precio * cantidad * (1 - descuento)
print(f"Precio final: {precio_final}€ (descuento del {descuento * 100}%)")
```

## Ejercicio 6: Solución: Bucle while - Contador simple

```python
# Números del 1 al 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Solo números impares del 1 al 20
contador = 1
while contador <= 20:
    if contador % 2 != 0:
        print(contador)
    contador += 1
```

## Ejercicio 7: Solución: Bucle while - Suma acumulativa

```python
# Suma del 1 al 100
total = 0
numero = 1

while numero <= 100:
    total += numero
    numero += 1

print(f"La suma de 1 a 100 es: {total}")

# Solo números pares
total_pares = 0
numero = 2

while numero <= 100:
    total_pares += numero
    numero += 2  # Saltamos de 2 en 2

print(f"La suma de números pares de 1 a 100 es: {total_pares}")
```

## Ejercicio 8: Solución: Bucle while con búsqueda - Primera aparición

```python
numeros = [5, 12, 8, 3, 15, 8, 20]
buscar = 8
encontrado = False
indice = 0

while indice < len(numeros) and not encontrado:
    if numeros[indice] == buscar:
        encontrado = True
    indice += 1

if encontrado:
    print(f"El número {buscar} está en la posición {indice - 1}")
else:
    print(f"El número {buscar} no está en la lista")
```

## Ejercicio 9: Solución: Bucle while con validación de entrada

```python
# Simulamos la entrada del usuario
numero_usuario = 15  # Primera entrada inválida
valido = False

while not valido:
    if 1 <= numero_usuario <= 10:
        valido = True
        print(f"¡Correcto! Has introducido el número {numero_usuario}")
    else:
        print(f"Error: {numero_usuario} no está entre 1 y 10. Intenta de nuevo.")
        numero_usuario = 7  # Simulamos una nueva entrada válida
```

## Ejercicio 10: Solución: Práctica integradora - Sistema de login

```python
usuario_correcto = "admin"
password_correcta = "1234"
intentos = 0
max_intentos = 3

# Simulamos los intentos del usuario
intentos_simulados = [
    ("admin", "wrong"),  # Primer intento: contraseña incorrecta
    ("user", "1234"),    # Segundo intento: usuario incorrecto
    ("admin", "1234")    # Tercer intento: correcto
]

intento_actual = 0

while intentos < max_intentos:
    # Simulamos la entrada del usuario
    usuario = intentos_simulados[intento_actual][0]
    password = intentos_simulados[intento_actual][1]
    intento_actual += 1
    
    print(f"\nIntento {intentos + 1}:")
    print(f"Usuario: {usuario}, Password: {password}")
    
    if usuario == usuario_correcto and password == password_correcta:
        print("✓ Acceso concedido")
        break
    else:
        intentos += 1
        if intentos < max_intentos:
            print(f"✗ Credenciales incorrectas. Te quedan {max_intentos - intentos} intentos")
        else:
            print("✗ Cuenta bloqueada. Has agotado los 3 intentos")
```
