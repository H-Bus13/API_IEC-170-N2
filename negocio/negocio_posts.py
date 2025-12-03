import requests
from prettytable import PrettyTable

def obtener_posts_api(url):
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
