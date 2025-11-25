import csv
import os


# -------------------------------------------------------------
# MANEJO DEL CSV
# -------------------------------------------------------------
# Módulo: Persistencia CSV
# Estas funciones se encargan de cargar y guardar la lista de países en un archivo CSV
# ubicado en la misma carpeta que este script (.py). Se usa el nombre pasado en `ruta`
# como nombre de archivo relativo a la carpeta del script.
def cargar_csv(ruta):
    paises = []
    ruta_local = os.path.join(os.path.dirname(__file__), ruta)
    try:
        with open(ruta_local, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except Exception:
                    print("ERROR: FORMATO INVALIDO EN EL CSV.")
    except FileNotFoundError:
        # No existe el CSV: se crea uno nuevo (con encabezado) en la misma carpeta del .py
        print("NO SE ENCONTRO EL ARCHIVO. SE CREARA UNO NUEVO EN LA CARPETA DEL SCRIPT.")
        with open(ruta_local, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
    return paises

def guardar_csv(ruta, paises):
    ruta_local = os.path.join(os.path.dirname(__file__), ruta)
    with open(ruta_local, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)
    print(f"GUARDADO: archivo '{ruta_local}' actualizado.")
# -------------------------------------------------------------
# FIN MANEJO DEL CSV
# -------------------------------------------------------------
# -------------------------------------------------------------
# AGREGAR PAIS
# -------------------------------------------------------------
def agregar_pais(paises):
    print("AGREGAR PAIS")
    nombre = input("NOMBRE: ").strip()
    poblacion = input("POBLACION: ").strip()
    superficie = input("SUPERFICIE: ").strip()
    continente = input("CONTINENTE: ").strip()

    if not nombre or not poblacion.isdigit() or not superficie.isdigit() or not continente:
        print("DATOS INVALIDOS.")
        return

    pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }
    paises.append(pais)
    print("PAIS AGREGADO.")
# -------------------------------------------------------------
# FIN AGREGAR PAIS
# -------------------------------------------------------------

# -------------------------------------------------------------
# BUSCAR POR NOMBRE
# -------------------------------------------------------------
def buscar_pais(paises):
    texto = input("INGRESE NOMBRE O PARTE DEL NOMBRE: ").upper()
    encontrados = []

    for pais in paises:
        if texto in pais["nombre"].upper():
            encontrados.append(pais)

    if encontrados:
        print("RESULTADOS:")
        for p in encontrados:
            print(p)
    else:
        print("NO SE ENCONTRARON COINCIDENCIAS.")

# -------------------------------------------------------------
# FILTROS
# -------------------------------------------------------------
def filtrar_por_continente(paises):
    cont = input("INGRESE CONTINENTE: ").upper()
    resultado = [p for p in paises if p["continente"].upper() == cont]

    if resultado:
        for p in resultado:
            print(p)
    else:
        print("NO HAY PAISES EN ESE CONTINENTE.")

def filtrar_por_rango_poblacion(paises):
    try:
        minimo = int(input("POBLACION MINIMA: "))
        maximo = int(input("POBLACION MAXIMA: "))
    except:
        print("VALORES INVALIDOS.")
        return

    resultado = [p for p in paises if minimo <= p["poblacion"] <= maximo]

    if resultado:
        for p in resultado:
            print(p)
    else:
        print("SIN RESULTADOS.")

def filtrar_por_rango_superficie(paises):
    try:
        minimo = int(input("SUPERFICIE MINIMA: "))
        maximo = int(input("SUPERFICIE MAXIMA: "))
    except:
        print("VALORES INVALIDOS.")
        return

    resultado = [p for p in paises if minimo <= p["superficie"] <= maximo]

    if resultado:
        for p in resultado:
            print(p)
    else:
        print("SIN RESULTADOS.")

# -------------------------------------------------------------
# ORDENAMIENTOS
# -------------------------------------------------------------
def ordenar_paises(paises):
    print("1 - ORDENAR POR NOMBRE")
    print("2 - ORDENAR POR POBLACION")
    print("3 - ORDENAR POR SUPERFICIE")
    opc = input("OPCION: ")

    asc = input("ASCENDENTE? (S/N): ").upper() == "S"

    if opc == "1":
        ordenados = sorted(paises, key=lambda x: x["nombre"], reverse=not asc)
    elif opc == "2":
        ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=not asc)
    elif opc == "3":
        ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=not asc)
    else:
        print("OPCION INVALIDA.")
        return

    for p in ordenados:
        print(p)

# -------------------------------------------------------------
# ESTADISTICAS
# -------------------------------------------------------------
def estadisticas(paises):
    if not paises:
        print("NO HAY DATOS.")
        return

    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])
    promedio_poblacion = sum([p["poblacion"] for p in paises]) / len(paises)
    promedio_superficie = sum([p["superficie"] for p in paises]) / len(paises)

    continentes = {}
    for p in paises:
        c = p["continente"]
        continentes[c] = continentes.get(c, 0) + 1

    print("PAIS CON MAYOR POBLACION:", mayor)
    print("PAIS CON MENOR POBLACION:", menor)
    print("PROMEDIO DE POBLACION:", promedio_poblacion)
    print("PROMEDIO DE SUPERFICIE:", promedio_superficie)
    print("CANTIDAD DE PAISES POR CONTINENTE:", continentes)

# -------------------------------------------------------------
# MENU PRINCIPAL
# -------------------------------------------------------------
def menu():
    ruta_csv = "paises.csv"
    paises = cargar_csv(ruta_csv)

    while True:
        print("\nMENU PRINCIPAL")
        print("1 - AGREGAR PAIS")
        print("2 - ACTUALIZAR PAIS")
        print("3 - BUSCAR PAIS")
        print("4 - FILTROS")
        print("5 - ORDENAR")
        print("6 - ESTADISTICAS")
        print("7 - SALIR")

        opcion = input("OPCION: ")

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            print("A - CONTINENTE")
            print("B - RANGO DE POBLACION")
            print("C - RANGO DE SUPERFICIE")
            sub = input("OPCION: ").upper()
            if sub == "A":
                filtrar_por_continente(paises)
            elif sub == "B":
                filtrar_por_rango_poblacion(paises)
            elif sub == "C":
                filtrar_por_rango_superficie(paises)
            else:
                print("OPCION INVALIDA.")
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            estadisticas(paises)
        elif opcion == "7":
            print("GUARDANDO CAMBIOS...")
            guardar_csv(ruta_csv, paises)
            print("HASTA LUEGO.")
            break
        else:
            print("OPCION INVALIDA.")

menu()
