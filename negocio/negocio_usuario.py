import bcrypt
import getpass
import re
from modelos import Usuario
from datos import insertar_objeto,obtener_usuario_nombre


# def registrar_usuario():
#     ingreso_nombre = input('Ingrese Nombre Completo: ')
#     ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
#     ingreso_email = input('Ingrese Correo Electrónico: ')
#     ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')

#     if ingreso_contrasena != '':
#         salt = bcrypt.gensalt()
#         hashed = bcrypt.hashpw(ingreso_contrasena.encode('utf-8'), salt)
#         nuevo_usuario = Usuario(
#             nombre=ingreso_nombre,
#             usuario=ingreso_nombre_usuario,
#             email=ingreso_email,
#             contrasena_hash=hashed,
#             contrasena_salt=salt)

#         try:
#             id_usuario = insertar_objeto(nuevo_usuario)
#             return id_usuario
#         except Exception as error:
#             print(f'Error al guardar al usuario: {error}')


def registrar_usuario():
    try:
        ingreso_nombre = input('Ingrese Nombre Completo: ').strip()
        ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ').strip()
        ingreso_email = input('Ingrese Correo Electrónico: ').strip()
        ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ').strip()

        # Validar campos vacíos
        if not ingreso_nombre:
            print("El nombre no puede estar vacío.")
            return None
            
        if not ingreso_nombre_usuario:
            print("El nombre de usuario no puede estar vacío.")
            return None
            
        if not ingreso_email:
            print("El correo no puede estar vacío.")
            return None

        # Validar formato de correo (regex)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", ingreso_email):
            print("El correo electrónico no es válido.")
            return None

        if not ingreso_contrasena:
            print("La contraseña no puede estar vacía.")
            return None

        # Encriptación:
        try:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(ingreso_contrasena.encode('utf-8'), salt)
        except Exception as error:
            print(f"Error al encriptar contraseña: {error}")
            return None

        # Creación Objeto
        nuevo_usuario = Usuario(
            nombre=ingreso_nombre,
            usuario=ingreso_nombre_usuario,
            email=ingreso_email,
            contrasena_hash=hashed,
            contrasena_salt=salt
        )

        # BD save
        try:
            id_usuario = insertar_objeto(nuevo_usuario)
            print("Usuario registrado correctamente.")
            return id_usuario
        except Exception as error:
            print(f'Error al guardar al usuario: {error}')
            return None

    except Exception as error:
        print(f" Error inesperado: {error}")
        return None


def iniciar_sesion():
    while True:
        ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
        ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')

        usuario=obtener_usuario_nombre(ingreso_nombre_usuario)
        if usuario:
            if bcrypt.checkpw(ingreso_contrasena.encode('utf-8'), usuario.contrasena_hash.encode('utf-8')):
                print('Acceso Concedido!')
                return True
            else:
                print('Contraseña Incorrecta, Intente nuevamente.')
                return False
        else:
            print('Usuario NO encontrado, Intente nuevamente.')