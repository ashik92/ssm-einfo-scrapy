# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    company_brn = scrapy.Field()