import requests
from prettytable import PrettyTable

def obtener_users_api(url):
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names=['N°','Nombre','Nombre Usuario','Correo','Teléfono','Web','Latitud','Longitud']
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_usuarios = respuesta.json()
        for usuario in listado_usuarios:
            tabla_usuarios.add_row([
                usuario['id'],
                usuario['name'],
                usuario['username'],
                usuario['email'],
                usuario['phone'],
                usuario['website'],
                usuario['address']['geo']['lat'],
                usuario['address']['geo']['lng']])
    print(tabla_usuarios)

def crear_user_api():
    url = 'https://jsonplaceholder.typicode.com/posts'
    nombre = input('Nombre: ')
    nombre_usuario = input('Usuario: ')
    correo = input('Correo: ')
    telefono = input('Celular: ')
    sitio_web = input('Web: ')

    user = {
    "name": nombre,
    "username": nombre_usuario,
    "email": correo,
    "phone": telefono,
    "website": sitio_web,
    }

    respuesta = requests.post(url,data=user)
    print(respuesta)


def guardar_user_db(url):
    pass

def modificar_user_db(url):
    pass

def eliminar_user_db(url):
    pass

