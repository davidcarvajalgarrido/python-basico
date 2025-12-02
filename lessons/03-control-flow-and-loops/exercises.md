# Lección 3 — Ejercicios

## Ejercicio 1: F-strings básicos

1. Crea variables `nombre = "Ana"`, `edad = 25` y `ciudad = "Madrid"`.
2. Usa f-strings para mostrar: "Hola, me llamo Ana, tengo 25 años y vivo en Madrid".
3. Crea una variable `precio = 19.99` y muestra: "El precio es 19.99€" usando f-strings.

## Ejercicio 2: F-strings con operaciones

1. Crea dos variables `base = 5` y `altura = 3`.
2. Usa un f-string para mostrar: "El área del rectángulo es: 15" (calcula base * altura dentro del f-string).
3. Crea `temperatura_celsius = 25` y muestra en un f-string la conversión a Fahrenheit usando la fórmula `F = C * 9/5 + 32`.

## Ejercicio 3: Condicionales simples

1. Crea una variable `edad = 16`.
2. Usa un `if-else` para verificar si la persona es mayor de edad (≥18) y muestra el mensaje apropiado.
3. Crea una variable `nota = 7.5` y comprueba si ha aprobado (≥5).

## Ejercicio 4: Condicionales múltiples - Clasificación de notas

1. Crea una variable `nota` con un valor entre 0 y 10.
2. Usa `if-elif-else` para clasificar la nota:
   - 0-4: "Suspenso"
   - 5-6: "Aprobado"
   - 7-8: "Notable"
   - 9-10: "Sobresaliente"
3. Muestra el resultado por pantalla.

## Ejercicio 5: Condicionales múltiples - Calculadora de descuentos

1. Crea dos variables: `precio = 100` y `cantidad = 15`.
2. Aplica descuentos según la cantidad:
   - Si cantidad < 10: sin descuento
   - Si cantidad entre 10-50: 10% descuento
   - Si cantidad > 50: 20% descuento
3. Calcula y muestra el precio final usando f-strings.

## Ejercicio 6: Bucle while - Contador simple

1. Crea un contador que empiece en 1 y muestre los números del 1 al 10 usando un bucle `while`.
2. Modifica el ejercicio para que solo muestre los números impares del 1 al 20.

## Ejercicio 7: Bucle while - Suma acumulativa

1. Usa un bucle `while` para sumar los números del 1 al 100.
2. Muestra el resultado final (debería ser 5050).
3. Modifica el código para que solo sume los números pares del 1 al 100.

## Ejercicio 8: Bucle while con búsqueda - Primera aparición

1. Dada la lista `numeros = [5, 12, 8, 3, 15, 8, 20]`, busca la primera aparición del número 8.
2. Usa un bucle `while` con una bandera (flag) para detener la búsqueda cuando lo encuentres.
3. Muestra la posición donde se encontró, o un mensaje si no está en la lista.

## Ejercicio 9: Bucle while con validación de entrada

1. Crea un programa que pida al usuario un número entre 1 y 10.
2. Usa un bucle `while` para seguir pidiendo el número hasta que sea válido.
3. Cuando sea válido, muestra: "¡Correcto! Has introducido el número X".
4. **Nota**: Para probar este ejercicio, simula la entrada con una variable en lugar de usar `input()`.

## Ejercicio 10: Práctica integradora - Sistema de login

1. Simula un sistema de login con `usuario_correcto = "admin"` y `password_correcta = "1234"`.
2. Usa una variable `intentos = 0` y un bucle `while` que permita máximo 3 intentos.
3. En cada iteración:
   - Simula que el usuario introduce datos (usa variables en lugar de `input()`)
   - Verifica si son correctos con un `if-else`
   - Si son correctos, muestra "Acceso concedido" y sal del bucle con `break`
   - Si no, incrementa intentos y muestra cuántos le quedan
4. Si se agotan los 3 intentos, muestra "Cuenta bloqueada".

