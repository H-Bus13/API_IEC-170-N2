import requests
from prettytable import PrettyTable

def obtener_posts_api():
    url = 'https://jsonplaceholder.typicode.com/posts'
    tabla_posts = PrettyTable()
    tabla_posts.field_names=['ID usuario','N°','Titulo','Cuerpo']
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_posts = respuesta.json()
        for post in listado_posts:
            tabla_posts.add_row([
                post['userId'],
                post['id'],
                post['title'],
                post['body']])
    print(tabla_posts)


def crear_posts_api():
    url = 'https://jsonplaceholder.typicode.com/posts'
    id = input('Id: ')
    usuario = input('Usuario Id: ')
    titulo = input('Titulo: ')
    cuerpo = input('Cuerpo: ')
    
    post = {
    "id": id,
    "userId": usuario,
    "title": titulo,
    "body": cuerpo,
    }

    respuesta = requests.post(url,data=post)
    print(respuesta)

def modificar_posts_api():
    id_post = input("ID del post a modificar: ")
    url = (f'https://jsonplaceholder.typicode.com/posts/{id_post}')

    usuario = input('Usuario Id: ')
    titulo = input('Titulo: ')
    cuerpo = input('Cuerpo: ')
    
    post = {
    "id": id,
    "userId": usuario,
    "title": titulo,
    "body": cuerpo,
    }
    
    respuesta = requests.put(url,data=post)
    print(respuesta.text)

def eliminar_post_api():
    user_id = input("ID del post a eliminar: ")
    url = (f'https://jsonplaceholder.typicode.com/posts/{user_id}')    
    respuesta = requests.delete(url)
    print("Status code:", respuesta.status_code)
    print("Respuesta:", respuesta.text)