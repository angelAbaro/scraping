"""
OBJETIVO:
    - Extraer informacion sobre los productos en la pagina de Mercado Libre Mascotas
    - Aprender a realizar extracciones verticales y horizontales utilizando reglas
CREADO POR: Angel abaro
ULTIMA VEZ EDITADO: 2022
"""
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class Articulo(Item):
    titulo = Field()
    precio = Field()
    #descripcion = Field()


class MercadoLibreCrawler(CrawlSpider):
    name = 'hiraoka'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
        #'CLOSESPIDER_PAGECOUNT': 3
        # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }

    # Utilizamos 2 dominios permitidos, ya que los articulos utilizan un dominio diferente
    allowed_domains = ['hiraoka.com.pe']

    start_urls = ['https://hiraoka.com.pe/computo-y-tecnologia/accesorios-computo']

    download_delay = 2

    # Tupla de reglas
    rules = (
        Rule(  # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'?p='
                # Patron en donde se utiliza "\d+", expresion que puede tomar el valor de cualquier combinacion de numeros
            ), follow=True),
        Rule(  # REGLA #2 => VERTICALIDAD AL DETALLE DE LOS PRODUCTOS
            LinkExtractor(
                allow=r'/computo-y-tecnologia/accesorios-computo/'
            ), follow=True, callback='parse_items'),
    # Al entrar al detalle de los productos, se llama al callback con la respuesta al requerimiento
    )

    def parse_items(self, response):
        item = ItemLoader(Articulo(), response)

        # Utilizo Map Compose con funciones anonimas
        # PARA INVESTIGAR: Que son las funciones anonimas en Python?
        item.add_xpath('titulo', '//h1/span/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        #item.add_xpath('descripcion', '//div[@class="item-description__text"]/p/text()',
                       #MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))

        soup = BeautifulSoup(response.body)
        precio = soup.find(class_="price")
        precio_completo = precio.text.replace('\n', ' ').replace('\r', ' ').replace(' ', '')  # texto de todos los hijos
        item.add_value('precio', precio_completo)

        yield item.load_item()

# EJECUCION
# scrapy runspider 2_mercadolibre.py -o mercado_libre.json -t json