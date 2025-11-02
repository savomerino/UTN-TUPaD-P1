# Práctico 11 de la UNIDAD 9 - Aplicación de la Recursividad
# Alumno: [Savo Merino]
# Comisión: [08]

# [Ejercicio 1]
# Factorial de un número
import time

def factorial(n):
    """
    Calcula el factorial de n de forma recursiva.
    """
    # Caso base: factorial(0) es 1
    if n == 0:
        return 1
    # Paso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

print("--- Ejercicio 1: Factorial ---")
num_usuario = int(input("Ingrese un número entero para calcular factoriales: "))
for i in range(1, num_usuario + 1):
    print(f"El factorial de {i} es {factorial(i)}")


# [Ejercicio 2]
# Serie de Fibonacci

def fibonacci(n, memo={}):
    """
    Calcula el número de Fibonacci en la posición n de forma recursiva.
    Usa memoización para mejorar el rendimiento.
    """
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print("\n--- Ejercicio 2: Serie de Fibonacci ---")
posicion = int(input("Ingrese una posición para la serie de Fibonacci: "))
print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
print("\n")


# [Ejercicio 3]
# Potencia de un número

def potencia(base, exponente):
    """
    Calcula la potencia de una base elevada a un exponente de forma recursiva.
    """
    if exponente < 0:
        raise ValueError("El exponente debe ser un número no negativo")
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

print("\n--- Ejercicio 3: Potencia ---")
base_num = int(input("Ingrese el número base: "))
exp_num = int(input("Ingrese el exponente: "))
print(f"{base_num} elevado a la {exp_num} es: {potencia(base_num, exp_num)}")


# [Ejercicio 4]
# Conversión de Decimal a Binario

def decimal_a_binario(n):
    """
    Convierte un número decimal a binario de forma recursiva.
    """
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

print("\n--- Ejercicio 4: Decimal a Binario ---")
num_decimal = int(input("Ingrese un número decimal para convertir a binario: "))
binario_str = decimal_a_binario(num_decimal)
print(f"El número {num_decimal} en binario es: {binario_str}")


# [Ejercicio 5]
# Palíndromo

def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo de forma recursiva.
    """
    # Caso base: una palabra de 0 o 1 letra siempre es un palíndromo.
    if len(palabra) <= 1:
        return True
    # Paso recursivo:
    else:
        # Comprueba si la primera y última letra son iguales
        if palabra[0] == palabra[-1]:
            # Si lo son, llama a la función con la palabra "recortada"
            return es_palindromo(palabra[1:-1])
        else:
            # Si no son iguales, no es palíndromo.
            return False

print("\n--- Ejercicio 5: Palíndromo ---")
palabra_usuario = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' SÍ es un palíndromo.")
else:
    print(f"'{palabra_usuario}' NO es un palíndromo.")


# [Ejercicio 6]
# Suma de dígitos

def suma_digitos(n):
    """
    Suma los dígitos de un número entero positivo de forma recursiva.
    """
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print("\n--- Ejercicio 6: Suma de Dígitos ---")
num_para_sumar = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
print(f"La suma de los dígitos de {num_para_sumar} es: {suma_digitos(num_para_sumar)}")


# [Ejercicio 7]
# Pirámide de Bloques

def contar_bloques(n):
    """
    Cuenta el total de bloques en una pirámide de n niveles.
    """
    if n < 1:
        raise ValueError("El número de niveles debe ser positivo")
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print("\n--- Ejercicio 7: Pirámide de Bloques ---")
niveles = int(input("Ingrese el número de bloques de la base de la pirámide: "))
print(f"Una pirámide de {niveles} niveles necesita {contar_bloques(niveles)} bloques.")


# [Ejercicio 8]
# Contar un dígito específico

def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito en un número, de forma recursiva.
    """
    if numero < 0:
        numero = abs(numero)
    if not (0 <= digito <= 9):
        raise ValueError("El dígito debe estar entre 0 y 9")
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

print("\n--- Ejercicio 8: Contar Dígito ---")
num_grande = int(input("Ingrese un número entero positivo: "))
dig_buscar = int(input("Ingrese el dígito que desea contar (0-9): "))
print(f"El dígito {dig_buscar} aparece {contar_digito(num_grande, dig_buscar)} veces en {num_grande}.")
