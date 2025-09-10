# TP 3 - Estructuras Condicionales
# Alumno: [Savo Merino]
# Comisión: [08]


# [Ejercicio 1]
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")



# [Ejercicio 2]
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")



# [Ejercicio 3]
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")



# [Ejercicio 4]
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("ingrese su edad: "))

if edad < 12:
    print("Niño/a") 
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")



# [Ejercicio 5]
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 



# [Ejercicio 6]
# El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

## importaciones
import random
from statistics import mode, median, mean

## defino la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print(f"Lista de numeros aleatorios: {numeros_aleatorios}")

## cálculo para la moda, mediana y media
## uso el bloque "try" para intentar el codigo por si no hay una moda única en la lista de números. si falla ejecuta "except"
try:
    media = mean(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    moda = mode(numeros_aleatorios)

    print(f"\nMedia: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")

## comparo los parámetros para determinar el sesgo
    if media > mediana and mediana > moda:
        print("Hay sesgo positivo")
    elif  media < mediana and mediana < moda:
        print("Hay sesgo negativo")
    else:
        print("No hay sesgo")
except Exception as e:
    print(f"\nNo se puede determinar el sesgo")




# [Ejercicio 7] 
# Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("ingrese una frase o palabra: ")
vocales = ["a", "e", "i", "o", "u"]

if frase[-1] in vocales:
    frase = frase + "!"
    print(frase)
else:
    print(frase)    




# [Ejercicio 8]
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("ingrese su nombre: ")
opcion = int(input("ingrese la opcion 1 para escribir en MAYUSCULAS, 2 en Minúsculas o 3 Título: "))
nombre_transformado = ""

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("opcion invalida")

    if nombre_transformado:
        print(f"Su nombre transformado es: {nombre_transformado}")
    else:
        print("No se pudo transformar el nombre")




# [Ejercicio 9]
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
#   ● Menor que 3: "Muy leve" (imperceptible).
#   ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#   ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#   ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#   ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#   ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto: "))

# clasificación de la categoría
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud < 4:
    # magnitud NO es < 3 (o sea, si es >= 3)
    categoria = "Leve (ligeramente perceptible)"
elif magnitud < 5:
    #  magnitud NO es < 4 
    categoria = "Moderado"
elif magnitud < 6:
    #  magnitud NO es < 5 
    categoria = "Fuerte"
elif magnitud < 7:
    # magnitud NO es < 6 
    categoria = "Muy Fuerte"
else:
    # si ninguna de las condiciones anteriores fue verdadera, la magnitud es >= 7
    categoria = "Extremo"

# imprimir el resultado
print(f"Un terremoto de magnitud {magnitud} se clasifica como: {categoria}")




# [Ejercicio 10]
#Utilizando la información aportada en la siguiente tabla sobre las estaciones del año


#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
#+------------------------------------------+------------------------+---------------------+
#|             Periodo del Año              |   Hemisferio Norte     |   Hemisferio Sur    |
#+==========================================+========================+=====================+
#| Desde el 21 de dic hasta el 20 de mar    |        Invierno        |        Verano       |
#+------------------------------------------+------------------------+---------------------+
#| Desde el 21 de mar hasta el 20 de jun    |        Primavera       |        Otoño        |
#+------------------------------------------+------------------------+---------------------+
#| Desde el 21 de jun hasta el 20 de sep    |         Verano         |       Invierno      |
#+------------------------------------------+------------------------+---------------------+
#| Desde el 21 de sep hasta el 20 de dic    |         Otoño          |       Primavera     |
#+------------------------------------------+------------------------+---------------------+
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

# [Ejercicio 10]
#Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#+------------------------------------------+------------------------+---------------------+
#|             Periodo del Año              |   Hemisferio Norte     |   Hemisferio Sur    |
#+==========================================+========================+=====================+
#| Desde el 21 de dic hasta el 20 de mar    |        Invierno        |        Verano       |
#+------------------------------------------+------------------------+---------------------+
#| Desde el 21 de mar hasta el 20 de jun    |        Primavera       |        Otoño        |
#+------------------------------------------+------------------------+---------------------+
#| Desde el 21 de jun hasta el 20 de sep    |         Verano         |       Invierno      |
#+------------------------------------------+------------------------+---------------------+
#| Desde el 21 de sep hasta el 20 de dic    |         Otoño          |       Primavera     |
#+------------------------------------------+------------------------+---------------------+
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

# pido los datos al usuario y se estandariza
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes_str = input("¿Qué mes del año es? (nombre o número): ").lower()
dia = int(input("¿Qué día del mes es?: "))

# diccionario para convertir el nombre del mes a número de mes 
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

# permitir la entrada por número o nombre
if mes_str.isdigit():
    mes = int(mes_str)
else:
    mes = meses.get(mes_str)
    if mes is None:
        print("Mes no válido. Ingrese el nombre completo o el número del mes.")
        exit()

# estructura condicional principal para el hemisferio
if hemisferio == "N":
    # lógica Hemisferio Norte
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else: # cubre el resto, que es el invierno
        estacion = "Invierno"

elif hemisferio == "S":
    # lógica Hemisferio Sur
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else: # cubre el resto, que es el verano
        estacion = "Verano"
else:
    estacion = "no válido. Por favor, ingrese N o S para el hemisferio."

# imprime el resultado
print(f"La estación del año es: {estacion}")