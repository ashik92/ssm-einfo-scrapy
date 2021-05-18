import scrapy


class CompanyItem(scrapy.Item):
    given_number = scrapy.Field()
    company_name = scrapy.Field()
    company_brn = scrapy.Field()
