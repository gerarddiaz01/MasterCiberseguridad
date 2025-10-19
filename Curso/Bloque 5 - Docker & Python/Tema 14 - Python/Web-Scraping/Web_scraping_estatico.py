import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Ecolog%C3%ADa_evolutiva"

# Obtener el texto en html con requests
response = requests.get(url)

# Tragarse la información de requests para luego poder acceder a ella
soup = BeautifulSoup(response.content, "html.parser")

# Buscar el primer elemento <title>
title = soup.find("title")
print(soup.title.string)

print("\n--------")

# Extraer todos los enlaces (<a>)
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

print("\n--------")

# Supongamos que queremos obtener el href del primer link
first_link = soup.find("a")
href = first_link["href"]
print(href)

print("\n--------")

# Tambien existe el metodo.get que es seguro si el atributo no existe
href = first_link.get("href")
print("href")

print("\n--------")

# Podemos navegar por la estructura del documento usándo relaciones como parent, next_sibling, previous_sibling o children
# Acceder al padre de un elemento
parent = first_link.parent
print(parent.name)

# Iterar sobre todos los hijos de un elemento
for child in parent.children:
    print(child)

# Acceder al siguiente y anterior elemento hermano
next_sibling = first_link.next_sibling
previous_sibling = first_link.previous_sibling

# Extraer todo el texto de un elemento
# print(first_link.text)