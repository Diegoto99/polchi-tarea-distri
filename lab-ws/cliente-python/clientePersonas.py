import sys
import datetime
import configparser
import requests
from requests.structures import CaseInsensitiveDict
import datetime
from datetime import timedelta


# Variables globales para verificación
api_personas_url_base = None
archivo_config = 'ConfigFile.properties'

def cargar_variables():
    config = configparser.RawConfigParser()
    config.read(archivo_config)

    global api_personas_url_listar, api_personas_url_crear, api_personas_url_base
    api_personas_url_listar = config.get('SeccionApi', 'api_personas_url_listar')
    api_personas_url_crear = config.get('SeccionApi', 'api_personas_url_crear')
    api_personas_url_base = config.get('SeccionApi', 'api_personas_url_base')  # Cargar la URL base


def listar():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    r = requests.get(api_personas_url_listar, headers=headers)
    if r.status_code == 200:
        listado = r.json()
        for item in listado:
            print("      " + str(item))
    else:
        print("Error " + str(r.status_code))


def crear(cedula: int, nombre: str, apellido: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'cedula': cedula, 'nombre': nombre, 'apellido': apellido}
    
    r = requests.post(api_personas_url_crear, headers=headers, json=datos)
    if r.status_code >= 200 and r.status_code < 300:
        print("Persona creada con éxito")
    else:
        print("Error " + str(r.status_code))
        print(str(r.json()))


def actualizar(cedula: int, nombre: str, apellido: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'nombre': nombre, 'apellido': apellido}

    url_actualizar = f"{api_personas_url_base}/actualizar/{cedula}"
    r = requests.put(url_actualizar, headers=headers, json=datos)
    
    if r.status_code == 200:
        print("Persona actualizada con éxito")
    else:
        print(f"Error {r.status_code}: {r.json()}")


def borrar(cedula: int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    url_borrar = f"{api_personas_url_base}/borrar/{cedula}"
    r = requests.delete(url_borrar, headers=headers)
    
    if r.status_code == 200:
        print("Persona eliminada con éxito")
    else:
        print(f"Error {r.status_code}: {r.json()}")


#######################################################
######  Menú principal
#######################################################
def menu():
    print("\n----- Menú -----")
    print("1. Listar personas")
    print("2. Crear nueva persona")
    print("3. Actualizar persona")
    print("4. Eliminar persona")
    print("5. Salir")
    return input("Seleccione una opción: ")

def procesar_opciones():
    while True:
        opcion = menu()

        if opcion == "1":
            print("Listando personas...")
            listar()

        elif opcion == "2":
            print("Crear nueva persona:")
            cedula = int(input("Ingrese cédula: "))
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            crear(cedula, nombre, apellido)

        elif opcion == "3":
            print("Actualizar persona:")
            cedula = int(input("Ingrese cédula de la persona a actualizar: "))
            nombre = input("Ingrese nuevo nombre: ")
            apellido = input("Ingrese nuevo apellido: ")
            actualizar(cedula, nombre, apellido)

        elif opcion == "4":
            print("Eliminar persona:")
            cedula = int(input("Ingrese cédula de la persona a eliminar: "))
            borrar(cedula)

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

#######################################################
######  Procesamiento principal
#######################################################
print("Iniciando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
cargar_variables()

# Ejecutar el menú
procesar_opciones()

print("Finalizando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
