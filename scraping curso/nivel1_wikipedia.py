# reques es para hacer el requerimiento al servidor
import requests
# User Agents // esto para que no nos identifique coo robot
# Es una cadena de texto con la cual se puede identificar el navegador y el sistema operativo del cliente. Por defecto es: ROBOT

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

# url semilla
url = "https://www.wikipedia.org/"

#hacemos el requerimiento a la url y guardamos lo que devuelva la funcion en Respuesta
# en respuesta tengo el arbol html
#aqui tambien le pasamos encabezados a travez del parametro headers
respuesta = requests.get(url, headers=encabezados)

print(respuesta.text)

