import logging
import scrapy
from . import harvesters as har

logger = logging.getLogger(__name__)
BASE_URL = "https://www.ssm-einfo.my/member/index.php?id=uni"


class SSMSpider(scrapy.Spider):
    name = 'ssm_einfo'
    allowed_domains = ['www.ssm-einfo.my']

    def start_requests(self):

        for i in range(202002000001, 202002000100):
            payload = {'search_number': str(i),
                       'Submit': 'Search'}
            yield scrapy.FormRequest(
                BASE_URL,
                formdata=payload,
                callback=self.company_detail_parser
            )

    def company_detail_parser(self, response):
        given_brn = int(response.request.body.decode(
            'utf-8').split('&')[0].split('=')[-1])
        yield har.extract_company_details(response, given_brn)
