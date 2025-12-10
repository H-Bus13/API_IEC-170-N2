from negocio import obtener_data_publicaciones,listado_publicaciones,registrar_usuario,iniciar_sesion
from negocio.negocio_users import obtener_data_usuarios_api,crear_user_api,modificar_user_api,eliminar_user_api,listado_usuarios_db,crear_usuario_db,buscar_user_name_db
from auxiliares import url_usuarios,url_publicaciones
from interfaces_usuarios import menu_inicial,menu_sesion_iniciada

# obtener_data_usuarios_api(url_usuarios)
# listado_usuarios_db()
# crear_user_api(url_usuarios)
# eliminar_user_api(url_usuarios)
# obtener_data_publicaciones(url_publicaciones)
# listado_publicaciones()
# registrar_usuario()

def app():
    while True:
        menu_inicial()
        
        opcion_inicial = input('Seleccione su opción [0-2]: ')
        if opcion_inicial=='1':
            registrar_usuario()
        elif opcion_inicial=='2':
            inicio_sesion = iniciar_sesion()
            if inicio_sesion:
                while True:
                    menu_sesion_iniciada()

                    opcion_sesion = input('Seleccione su opción [1-8]: ')
                    if opcion_sesion =='1':
                        obtener_data_usuarios_api()
                    elif opcion_sesion =='2':
                        crear_user_api()
                    elif opcion_sesion =='3':
                        modificar_user_api()
                    elif opcion_sesion =='4':
                        eliminar_user_api()
                    elif opcion_sesion =='5':
                        listado_usuarios_db()
                    elif opcion_sesion =='6':
                        crear_usuario_db()
                    elif opcion_sesion =='7':
                        buscar_user_name_db()
                    elif opcion_sesion =='8':
                        print('Adios...')
                        break
                    else:
                        print('Opción incorrecta, vuelva a intentar...')
        elif opcion_inicial=='0':
            print('Saliendo...')
            break
        else:
            print('Opción Incorrecta, vuelva a intentar...')

app()