from prettytable import PrettyTable
import requests
import json
from modelos import User
from datos import insertar_objeto, obtener_listado_objetos, obtener_user_name
from negocio import crear_geolocalizacion, crear_direccion, crear_compania


def obtener_data_usuarios_api():
    url = 'https://jsonplaceholder.typicode.com/users'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data Users...")
        usuarios = respuesta.json()
        for user in usuarios:
            id_geo = crear_geolocalizacion(
                user['address']['geo']['lat'],
                user['address']['geo']['lng']
            )

            id_direccion = crear_direccion(
                user['address']['street'],
                user['address']['suite'],
                user['address']['city'],
                user['address']['zipcode'],
                id_geo
            )

            id_compania = crear_compania(
                user['company']['name'],
                user['company']['catchPhrase'],
                user['company']['bs']
            )

            crear_usuario_db(
                user['name'],
                user['username'],
                user['email'],
                user['phone'],
                user['website'],
                id_direccion,
                id_compania
            )

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")


def crear_user_api():
    url = 'https://jsonplaceholder.typicode.com/users/'
    name = input('Ingrese su nombre: ')
    username = input('Ingrese nombre usuario: ')
    email = input('Ingrese correo: ')
    phone = input('Ingrese celular: ')
    website = input('Ingrese página web: ')
    user = {
        'name': name,
        'username': username,
        'email': email,
        'phone': phone,
        'website': website
    }
    respuesta = requests.post(url, data=user)
    if respuesta.status_code==201:
        print(respuesta.text)


def modificar_user_api():
    id_user = input('Ingrese ID usuario: ')
    url = f'https://jsonplaceholder.typicode.com/users/{id_user}'
    try:
        id_user=int(id_user)
    except:
        print('Ingrese un número entero...')
    name = input('Ingrese su nombre: ')
    username = input('Ingrese nombre usuario: ')
    email = input('Ingrese correo: ')
    phone = input('Ingrese celular: ')
    website = input('Ingrese página web: ')
    user = {
        'name': name,
        'username': username,
        'email': email,
        'phone': phone,
        'website': website
    }
    url = f'{url}'
    respuesta = requests.put(url, data=user)
    if respuesta.status_code==200:
        print(respuesta.text)


def eliminar_user_api():
    while True:
        id_user = input("Ingrese ID de usuario a eliminar: ").strip()

        if not id_user.isdigit():
            print(" Debe ingresar un número entero.\n")
            continue

        id_user = int(id_user)
        break

    url = f"https://jsonplaceholder.typicode.com/users/{id_user}"

    respuesta = requests.delete(url)

    print(f"Código de respuesta: {respuesta.status_code}")
    print("Respuesta del servidor:")
    print(respuesta.text)



def buscar_user_name_db(nombre):
   if nombre != '':
       user = obtener_user_name(nombre)
       if user != None:
           return user

# def buscar_user_name_db():
#     nombre = input('Ingrese el nombre del user: ')
    
#     if not nombre:
#         print("Debe ingresar un nombre.")
#         return
    
#     user = obtener_user_name(nombre)

#     if user is None:
#         print("Usuario no encontrado.")
#     else:
#         print("Usuario encontrado:", user)
#         return user


def listado_usuarios_db():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = [
        'N°', 'Nombre', 'Usuario', 'Correo', 'Teléfono', 'Sitio Web']
    listado_usuarios = obtener_listado_objetos(User)

    if listado_usuarios:
        for usuario in listado_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.name, usuario.username, usuario.email, usuario.phone, usuario.website])
        print(tabla_usuarios)


def pedir_obligatorio(mensaje, validacion=None, mensaje_error="Dato inválido, inténtalo de nuevo."):
    while True:
        valor = input(mensaje).strip()

        # Si el usuario presiona Enter sin escribir nada → cancelar
        if valor == "":
            print("Operación cancelada por el usuario.")
            return None

        # Si no se requiere validación extra
        if validacion is None:
            return valor

        # Validación adicional proporcionada
        if validacion(valor):
            return valor

        print(mensaje_error)


def pedir_entero_obligatorio(mensaje):
    """Pide un número entero obligatorio, con opción a cancelar."""
    while True:
        valor = input(mensaje).strip()

        if valor == "":
            print("Operación cancelada por el usuario.")
            return None

        if valor.isdigit():
            return int(valor)

        print("Debe ingresar un número válido.\n")


def pedir_entero_opcional(mensaje):
    """Pide un número entero opcional (permite Enter)."""
    while True:
        valor = input(mensaje).strip()

        if valor == "":
            return None

        if valor.isdigit():
            return int(valor)

        print("Debe ingresar un número válido o presionar ENTER para omitir.\n")


def validar_correo(correo):
    return "@" in correo and "." in correo and len(correo) >= 5


def pedir_correo_obligatorio():
    """Pide correo obligatorio con opción de cancelar."""
    while True:
        correo = input("Correo (obligatorio, ENTER para cancelar): ").strip()

        if correo == "":
            print("Operación cancelada por el usuario.")
            return None

        if validar_correo(correo):
            return correo

        print("Correo inválido.")
        opcion = input("¿Desea intentar nuevamente? ('s' para sí, otra tecla para cancelar): ")

        if opcion.lower() != "s":
            print("Registro cancelado por el usuario.")
            return None


def crear_usuario_db():

    print("\n=== Crear nuevo usuario ===")

    # -------- CAMPOS OBLIGATORIOS --------
    nombre = pedir_obligatorio("Nombre (obligatorio, ENTER para cancelar): ")
    if nombre is None:
        return

    nombre_usuario = pedir_obligatorio("Username (obligatorio, ENTER para cancelar): ")
    if nombre_usuario is None:
        return

    correo = pedir_correo_obligatorio()
    if correo is None:
        return

    # -------- CAMPOS OPCIONALES --------
    telefono = input("Teléfono (ENTER para omitir): ").strip()
    sitio_web = input("Sitio Web (ENTER para omitir): ").strip()

    # -------- ID OBLIGATORIOS --------
    id_direccion = pedir_entero_obligatorio("ID dirección (obligatorio, ENTER para cancelar): ")
    if id_direccion is None:
        return

    id_compania = pedir_entero_obligatorio("ID compañía (obligatorio, ENTER para cancelar): ")
    if id_compania is None:
        return

    # -------- VERIFICAR EXISTENCIA --------
    user = buscar_user_name_db(nombre)

    if user:
        print("Usuario ya existe, no será agregado.")
        return

    # -------- CREAR OBJETO --------
    usuario = User(
        name=nombre,
        username=nombre_usuario,
        email=correo,
        phone=telefono if telefono else None,
        website=sitio_web if sitio_web else None,
        addressId=id_direccion,
        companyId=id_compania
    )

    try:
        id_usuario = insertar_objeto(usuario)
        print("Usuario creado con éxito.")
        return id_usuario

    except Exception as error:
        print(f"Error al guardar el usuario: {error}")