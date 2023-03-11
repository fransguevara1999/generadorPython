from scrapy.crawler import CrawlerProcess
from scrapy.item import Field
from scrapy.item import Item
from datetime import datetime
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider

now = datetime.now()
año=now.year
mes=now.month
dia=now.day
class github(Item):
    usado = Field()
    colaboradores = Field()
    lenguajes = Field()
    preguntas=Field()


