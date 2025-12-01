import requests

def obtener_usuarios_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print(respuesta.text)

