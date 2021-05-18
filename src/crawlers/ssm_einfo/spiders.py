import logging
import scrapy
from . import harvesters as har
import json

logger = logging.getLogger(__name__)

URL_TEMPLATE = "https://www.ssm-einfo.my/member/index.php?id=uni"


class ExampleScrapySpider(scrapy.Spider):
    name = 'ssm_einfo'
    allowed_domains = ['www.ssm-einfo.my']

    def parse(self, response):
        payload = {'search_number': '1',
                   'Submit': 'Search'}
        yield scrapy.FormRequest(
            URL_TEMPLATE,
            formdata=payload,
            callback=self.parserr
        )

    def parserr(self, response):
        yield har.extract_company_details(response)
