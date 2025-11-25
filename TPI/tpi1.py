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