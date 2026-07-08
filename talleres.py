import os
os.system('cls')

def menu():
    print('''========== MENÚ PRINCIPAL ==========
1. Agregar taller
2. Buscar taller
3. Eliminar taller
4. Actualizar disponibilidad
5. Mostrar talleres
6. Salir''')

def valNombre(nombre):
    return nombre.strip().lower() != ""

def valCuposPositivo(cupos):
    return cupos >= 0

def valPrecioTaller(precioTaller):
    return precioTaller > 0.0

def leerOpcion():
    try:
        opc = int(input("Seleccione una opción del 1 al 6: "))
        if opc in range(1, 7):
            return opc
    except ValueError:
        return 

def valCodigo(codigo):
    return codigo.strip().lower() != ""

def agregarTaller(talleres):
    while True:
        codigo = input("Ingrese código del taller: ")
        if not valCodigo(codigo):
            print('Error. El código no puede estar vacío ni contener solo espacios.')
        else:
            break
    while True:
            nombre = input("Ingrese nombre del taller: ")
            if not valNombre(nombre):
                print('Error. El nombre no puede estar vacío ni contener solo espacios.')
            else:
                break
    while True:
        try:
            cupos = int(input(f'Ingrese la cantidad de cupos del taller {nombre}: '))
            if not valCuposPositivo(cupos):
                print('Error. Se debe ingresar un número entero positivo.')
            else:
                break
        except:
            pass
    while True:
        try:
            precioTaller = float(input(f"Ingrese el precio del taller {nombre}: "))
            if not valPrecioTaller(precioTaller):
                print("Error. El precio del taller debe ser mayor a Cero. ")
            else:
                break
        except:
            pass
    
    nuevoTaller = {"codigo": codigo, "nombre": nombre, "cupos": cupos, "precio": precioTaller, "disponible": False}
    talleres.append(nuevoTaller)

def buscarTaller(talleres, codigoBuscado):
    for x in range(len(talleres)):
        if talleres[x]["codigo"].lower() == codigoBuscado.strip().lower():
            return x
    return -1

def eliminarTaller(talleres):
    tallerAEliminar = input("Ingrese el codigo del taller que desea eliminar: ")
    posicion = buscarTaller(talleres, tallerAEliminar)
    if posicion != -1:
        talleres.pop(posicion)
        print(f"El taller con codigo {tallerAEliminar} ha sido eliminado con éxito.")
    else:
        print(f"No existe ningún taller de codigo {tallerAEliminar} registrado en nuestr base de datos.")

def actualizarDisponibilidad(talleres):
    for x in range(len(talleres)):
        if talleres[x]["cupos"] > 0:
            talleres[x]["disponible"] = True
        else:
            talleres[x]["disponible"] = False

def mostrarTalleres(talleres):
    actualizarDisponibilidad(talleres)
    if (len(talleres)) == 0:
        print("No hay talleres registrados.")
    else:
        print("=== LISTA DE TALLERES ===")
        for x in range(len(talleres)):
            if talleres[x]['disponible'] == True:
                estado = "Disponible"
            else:
                estado = "No hay cupos"
            print(f"\nNombre: {talleres[x]['nombre']} \nCodigo: {talleres[x]['codigo']}\nCupos: {talleres[x]['cupos']}\nPrecio: {talleres[x]['precio']}\nEstado: {estado}")
            print("===" *30)

def main():
    talleres = []
    while True:
        menu()
        opc = leerOpcion()
        if opc == 1:
            agregarTaller(talleres)
            print("Taller creado con éxito.")
        elif opc == 2:
            codigoBuscado = input("Ingrese el código del taller a buscar.").lower().strip()
            posicion = buscarTaller(talleres, codigoBuscado)
            if posicion != -1:
                taller = talleres[posicion]
                estado = "Disponible" if taller['disponible'] else "No hay cupos"
                print(f"Taller encontrado!\nNombre: {taller['nombre']}\nCodigo: {taller['codigo']}\nCupos: {taller['cupos']}\nPrecio: {taller['precio']}\nEstado: {estado}")
            else:
                print("El taller no se encuentra registrado.")
        elif opc == 3:
            eliminarTaller(talleres)
        elif opc == 4:
            actualizarDisponibilidad(talleres)
            print("Estado de lso talleres actualizado con éxito")
        elif opc == 5:
            mostrarTalleres(talleres)
        elif opc == 6:
            print("Gracias. Vuelva pronto.")
            break
main()
            
