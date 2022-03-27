# reques es para hacer el requerimiento al servidor
import requests
from lxml import html # pip install lxml
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

# PARSEO DEL ARBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
parser = html.fromstring(respuesta.text)

# EXTRACCION DE IDIOMA INGLES
ingles = parser.get_element_by_id("js-link-box-en")
print (ingles.text_content())

# EXTRACCION SOLO DEL TEXTO QUE DICE INGLES
ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
print(ingles[0])

# EXTRACCION DE TODOS LOS IDIOMAS POR CLASE
idiomas = parser.find_class('central-featured-lang')
for idioma in idiomas:
  print(idioma.text_content())

# EXTRACCION DE TODOS LOS IDIOMAS POR XPATH
idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
for idioma in idiomas:
  print(idioma)

