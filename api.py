from negocio import obtener_data_publicaciones,listado_publicaciones,registrar_usuario,iniciar_sesion
from negocio.negocio_users import obtener_data_usuarios_api,crear_user_api,modificar_user_api,eliminar_user_api,listado_usuarios_db,usuario_existe,buscar_user_name_db,crear_usuario_db_interactivo
from auxiliares import url_usuarios,url_publicaciones
from interfaces_usuarios import menu_inicial,menu_sesion_iniciada


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

                    opcion_sesion = input('Seleccione su opción [1-7]: ')
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
                        crear_usuario_db_interactivo()
                    elif opcion_sesion =='7':
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