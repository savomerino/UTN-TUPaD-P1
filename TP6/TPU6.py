# 1 Imprimir "Hola Mundo"
# --- Definición de la Función ---
def imprimir_hola_mundo():
    """
    Esta función no recibe parámetros e imprime el mensaje 'Hola Mundo!' 
    en la pantalla.
    """
    print("Hola Mundo!")

# --- Programa Principal ---
imprimir_hola_mundo()

# 2 Saludar al Usuario
# --- Definición de la Función ---
def saludar_usuario(nombre):
    """
    Recibe un 'nombre' como parámetro y devuelve un string con un saludo 
    personalizado.
    """
    return f"Hola {nombre}!"

# --- Programa Principal ---
nombre_ingresado = input("Por favor, ingrese su nombre: ")
saludo_personalizado = saludar_usuario(nombre_ingresado)
print(saludo_personalizado)

# 3 Informacion personal 
# --- Definición de la Función ---
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe cuatro parámetros e imprime un mensaje formateado con ellos.
    Esta función no devuelve ningún valor.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# --- Programa Principal ---
nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")
ed = input("Ingrese su edad: ")
res = input("Ingrese su lugar de residencia: ")

informacion_personal(nom, ape, ed, res)

# 4 Área y perímetro de un círculo
import math # Importamos el módulo 'math' para usar el valor de Pi

# --- Definición de Funciones ---
def calcular_area_circulo(radio):
    """Recibe el radio y devuelve el área del círculo."""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Recibe el radio y devuelve el perímetro del círculo."""
    return 2 * math.pi * radio

# --- Programa Principal ---
radio_ingresado = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio_ingresado)
perimetro = calcular_perimetro_circulo(radio_ingresado)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5 Convertir segundos a horas
# --- Definición de la Función ---
def segundos_a_horas(segundos):
    """Recibe una cantidad de segundos y devuelve la cantidad de horas."""
    return segundos / 3600

# --- Programa Principal ---
segundos_ingresados = int(input("Ingrese una cantidad de segundos: "))
horas = segundos_a_horas(segundos_ingresados)

print(f"{segundos_ingresados} segundos equivalen a {horas:.2f} horas.")

#6 Tabla de multiplicar
# --- Definición de la Función ---
def tabla_multiplicar(numero):
    """
    Recibe un número e imprime su tabla de multiplicar del 1 al 10.
    No devuelve ningún valor.
    """
    print(f"--- Tabla de multiplicar del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# --- Programa Principal ---
numero_usuario = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario)

#7 Operaciones básicas
# --- Definición de la Función ---
def operaciones_basicas(a, b):
    """
    Recibe dos números (a, b) y devuelve una tupla con los resultados
    de la suma, resta, multiplicación y división.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

# --- Programa Principal ---
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#8 # --- Definición de la Función ---
def calcular_imc(peso, altura):
    """Recibe peso (kg) y altura (m), y devuelve el IMC."""
    return peso / (altura ** 2)

# --- Programa Principal ---
peso_usuario = float(input("Ingrese su peso en kg (ej: 70.5): "))
altura_usuario = float(input("Ingrese su altura en metros (ej: 1.75): "))

imc = calcular_imc(peso_usuario, altura_usuario)

print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

#9 Convertir Celcius a Fahrenheit
# --- Definición de la Función ---
def celsius_a_fahrenheit(celsius):
    """Recibe grados Celsius y los convierte a Fahrenheit."""
    return (celsius * 9/5) + 32

# --- Programa Principal ---
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C equivale a {temp_fahrenheit:.2f}°F")

#10 Calcular promedio de tres numeros
# --- Definición de la Función ---
def calcular_promedio(a, b, c):
    """Recibe tres números y devuelve su promedio."""
    return (a + b + c) / 3

# --- Programa Principal ---
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {promedio:.2f}")
