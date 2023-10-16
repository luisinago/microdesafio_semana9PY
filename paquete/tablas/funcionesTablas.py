# Ejercicio Tablas + Otra Opción

# Crear una función que pida un número entero, lea el fichero tabla-n.txt con la tabla de multiplicar
# de ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe,
# debe mostrar un mensaje por pantalla informando de ello.

# Estas 2 funciones deben ser seleccionadas por el usuario dentro de un menú.

def generar(numero):
    archivo_datos = open(f'tabla-{numero}.txt', 'w')
    for i in range(1,11):
        archivo_datos.write(f'{numero} x {i} = {numero*i}\n')
    archivo_datos.close()

def mostrar(numero):
    try:
        archivo_datos = open(f'tabla-{numero}.txt', 'r')
    except FileNotFoundError as e:
        print('No se encontró el archivo')
    print(archivo_datos.read())
    archivo_datos.close()

def buscar_linea(numero):
    linea = int(input("Ingrese número del 1 al 10 según la línea que desee ver: "))
    try:
        archivo_datos = open(f'tabla-{numero}.txt', 'r')
        lineas = archivo_datos.readlines()
        print(lineas[linea-1])
        archivo_datos.close()
    except FileNotFoundError as e:
        print('No se encontró el archivo')
        confirmacion = input("Desea generar la tabla? ('si' para confirmar)").lower()
        if confirmacion == "si":
            generar(numero)
            buscar_linea(numero)

def menu_tablas():
    while True:
        print('''Menu
              1. Generar tabla de multiplicar
              2. Mostrar tabla de multiplicar
              3. Mostrar linea de tabla de multiplicar
              4. Salir
              ''')
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion not in [1,2,3,4]:
                print("Esa opción no existe. Intente nuevamente.")
                continue
            if opcion == 1:
                num = int(input("Ingrese número a operar: "))
                generar(num)
            elif opcion == 2:
                num = int(input("Ingrese número a operar: "))
                mostrar(num)
            elif opcion == 3:
                num = int(input("Ingrese número a operar: "))
                buscar_linea(num)
            elif opcion == 4:
                break
        except ValueError as e:
            print("Error. Debe ingresar un número")

menu_tablas()