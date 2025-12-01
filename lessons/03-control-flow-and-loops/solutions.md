# Lección 3 — Soluciones

## Ejercicio 1: Solución: Validación de contraseñas

```
while True:
    pwd = input("Contraseña: ")
    if len(pwd) >= 8 and any(ch.isdigit() for ch in pwd):
        print("OK")
        break
    else:
        print("Debe tener ≥8 y al menos un dígito.")
```

## Ejercicio 2: Solución: Suma de pares

```
total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total += n
print(total)  # 2550
```

## Ejercicio 3: Solución: Búsqueda con else

```
nombres = ["Ana","Luis","Sofía"]
objetivo = "Carlos"
for n in nombres:
    if n == objetivo:
        print("Encontrado")
        break
else:
    print("No encontrado")
```
