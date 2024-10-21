import sys
import datetime
import configparser
import requests
from requests.structures import CaseInsensitiveDict
import datetime
from datetime import timedelta


#Variables globales para verificacion
api_personas_url_base = None
archivo_config = 'ConfigFile.properties'

def cargar_variables():
    config = configparser.RawConfigParser()
    config.read(archivo_config)

    global api_personas_url_listar, api_personas_url_crear
    api_personas_url_listar = config.get('SeccionApi', 'api_personas_url_listar')
    api_personas_url_crear = config.get('SeccionApi', 'api_personas_url_crear')


def listar():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = { }
    
    
    r = requests.get(api_personas_url_listar, headers=headers, json=datos)
    if (r.status_code == 200):
        # Validar response
        listado = r.json()
        for item in listado:
            print( "      " + str(item) )
    else:
        print( "Error " + str(r.status_code))


def crear(cedula: int, nombre: str, apellido: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'cedula': cedula, 
             'nombre' : nombre,
             'apellido' : apellido
            }
    
    r = requests.post(api_personas_url_crear, headers=headers, json=datos)
    if (r.status_code >= 200 and r.status_code < 300):
        # Validar response
        print(r)
        
    else:
        print( "Error " + str(r.status_code))
        print(str(r.json()))


#######################################################
######  Procesamiento principal
#######################################################
print("Iniciando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
cargar_variables()

print("Primer listado de personas:")
listar()
print("________________")


print("Crear nueva persona:")
cedula = int(input("Ingrese cedula: "))
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
crear(cedula, nombre, apellido)


print("________________")
print("Segundo listado de personas:")
listar()

print("Finalizando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))