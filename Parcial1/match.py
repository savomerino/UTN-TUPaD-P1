legajos = [101, 102, 103]
nombres = ["Ana", "Luis", "Mara"]
edades = [19, 21, 20]
promedios = [8.5, 6.7, 9.1]

opcion = ""
while opcion != "6":
    print("\n==============MENU ALUMNOS==============")
    print("1) Listar")
    print("2) Alta")
    print("3) Actualizar promedio")
    print("4) Buscar por nombre")
    print("5) Buscar por legajo")
    print("6) Salir")
    opcion = input("Ingrese una opcion: ").strip()

    match opcion:
        case "1":
            print("Opción Listar seleccionada")
            for i in range(len(legajos)):
                print(f"Legajo: {legajos[i]}, Nombre: {nombres[i]}, Edad: {edades[i]}, Promedio: {promedios[i]}")
        case "2":
            print("Opción Alta seleccionada")
            #legajo
            while True:
                legajo_ingresado = input("Legajo (entero): ").strip()
                if not legajo_ingresado.isdigit():
                    print("Legajo inválido.")
                    continue
                leg = int(legajo_ingresado)
                if leg in legajos:
                    print("Ya existe un alumno con ese legajo.")
                    continue
                break
            #nombre
            while True:
                nombre_ingresado = input("Nombre: ").strip()
                if len(nombre_ingresado) == 0 or not nombre_ingresado.replace(" ", "").isalpha():
                    print("Nombre inválido.")
                    continue
                break
            #edad
            while True:
                edad_str = input("Edad (entero): ").strip()
                if not edad_str.isdigit():
                    print("Edad inválida.")
                    continue
                edad = int(edad_str)
                if edad < 0 or edad > 120:
                    print("Edad fuera de rango.")
                    continue
                break
            #promedio
            while True:
                prom_str = input("Promedio (0 a 10): ").strip()
                if prom_str.replace(".", "", 1).isdigit():
                    prom = float(prom_str)
                    if prom <= 0 or prom <= 10:
                        break
                print("Promedio fuera de rango.")
            
            #agregar alumno
            legajos.append(leg)
            nombres.append(nombre_ingresado)
            edades.append(edad)
            promedios.append(prom)
            print("Alumno agregado correctamente.")

        case "3":
            print("Opción Actualizar promedio seleccionada")
        case "4":
            print("Opción Buscar por nombre seleccionada")
        case "5":
            print("Opción Buscar por legajo seleccionada")
        case "6":
            print("Saliendo...")
        case _:
            print("Opción inválida. Elegí entre 1-6")