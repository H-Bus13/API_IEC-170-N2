import requests
from datos.sql.obtener_datos import obtener_datos_objetos, obtener_user_por_id
from datos.sql.guardar_datos import insertar_objeto
from auxiliares import normalizar_cadena
from modelos.modelos import User
from prettytable import PrettyTable

def obtener_users_api():
    url = 'https://jsonplaceholder.typicode.com/users'
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
    url = 'https://jsonplaceholder.typicode.com/users'
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


def modificar_user_api():
    user_id = input("ID del usuario a modificar: ")
    url = (f'https://jsonplaceholder.typicode.com/users/{user_id}')

    nombre = input('Nombre: ')
    nomre_usuario = input('Usuario: ')
    correo = input('Correo: ')
    telefono = input('Celular: ')
    web = input('Web: ')
    
    user = {
    "name": nombre,
    "username": nomre_usuario,
    "email": correo,
    "phone": telefono,
    "website": web
    }
    
    respuesta = requests.put(url,data=user)
    print(respuesta.text)

def eliminar_user_api():
    user_id = input("ID del usuario a eliminar: ")
    url = (f'https://jsonplaceholder.typicode.com/users/{user_id}')    
    respuesta = requests.delete(url)
    print("Status code:", respuesta.status_code)
    print("Respuesta:", respuesta.text)

def obtener_users(user):
    listado_users = obtener_datos_objetos(user)
    user_encontrado = None
    if listado_users:
        for user in listado_users:
            if normalizar_cadena(user.id) == normalizar_cadena(user):
                user_encontrado = user
                break
    return user_encontrado

def guardar_user_db():
    while True:
        id_user = int(input("Ingrese id usuario: "))
        id_number = id_user
        if id_user!='':
            user_encontrado = obtener_user_por_id(id_number)
            if user_encontrado == None:
                newname = input('Ingrese nuevo nombre user:')
                newusername = input('Ingrese nuevo username: ')
                newemeail = input('Ingrese nuevo mail: ')
                newphone = int(input('Ingrese nuevo telefono: '))
                newwebsite = input('Ingrese nuevo web site: ')
                adressID = int(input('Ingrese id de adress: '))
                companyID = int(input('Ingrese id de compañia: '))

                if newname!='':
                    new_user = User(
                        id=id_number,
                        name = newname,
                        username = newusername,
                        email=newemeail,
                        phone = newphone,
                        website = newwebsite, 
                        adressId = adressID,
                        companyId = companyID)
                    insertar_objeto(new_user)
                    break
                else:
                    print('Debe ingresar el nombre del user.')
            else:
                print('User YA existe en base de datos.')
        else:
            print('Debe ingresar el id del user.')

def modificar_user_db():
    pass

def eliminar_user_db(url):
    pass

