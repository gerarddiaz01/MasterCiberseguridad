import requests

# Enviar solicitud GET
url = "https://es.wikipedia.org/wiki/Ecolog%C3%ADa_evolutiva"
try:
    response = requests.get(url)
except:
    print("Error al abrir la página")   
else:
    if response.status_code == 200:
        print("Contenido de la solicitud GET:")
        print(response.content)
    else:
        print("Error en la solicitud:", response.status_code)