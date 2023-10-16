# Ejercicio Agenda de Contactos

# Crea un menú con las opciones de agendar contacto y ver información de contacto.
# Para agendar se solicitará al usuario: nombre, apellido, teléfono, dirección.
# Para ver informacion se pedirá el nombre y apellido.
# La información será un listado de diccionarios, donde cada diccionario tendrá como claves
# lo solicitado al usuario y como valor lo que ingrese el usuario.
# A su vez, este listado debe estar guardado en un archivo JSON.

import json

def obtener_agenda():
    try:
        with open(f"agenda.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError as e:
        return []

def agendar():
    agenda = obtener_agenda()
    contacto = {
        "nombre": input("Ingrese su nombre: "),
        "apellido": input("Ingrese su apellido: "),
        "telefono": input("Ingrese su teléfono: "),
        "direccion": input("Ingrese su dirección: "),
    }
    agenda.append(contacto)
    with open(f"agenda.json", "w") as archivo:
        json.dump(agenda, archivo, indent=4)

def ver_contacto():
    nombre_a_buscar = input("Ingrese nombre: ")
    apellido_a_buscar = input("Ingrese apellido: ")
    agenda = obtener_agenda()
    for contacto in agenda:
        if contacto["nombre"] != nombre_a_buscar or contacto["apellido"] != apellido_a_buscar:
            continue
        print(f'''
              Nombre: {contacto["nombre"]}
              Apellido: {contacto["apellido"]}
              Teléfono: {contacto["telefono"]}
              Dirección: {contacto["direccion"]}
              ''')
        break
    else:
        print(f"No se encontró el contacto {nombre_a_buscar} {apellido_a_buscar}")

def menu_agenda():
    print('''Menu
          1. Agendar contacto
          2. Ver contacto
          ''')
    opcion = input("Ingrese opción: ")
    if opcion not in ["1", "2"]:
        print("No existe esa opción")
        return
    if opcion == "1":
        agendar()
    elif opcion == "2":
        ver_contacto()
        