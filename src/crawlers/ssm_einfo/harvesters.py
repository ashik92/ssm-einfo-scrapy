from .items import CompanyItem


def extract_company_details(response):
    company_brn = response.xpath(
        "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[2]/tbody/tr/td/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/text()").get()
    company_name = response.xpath(
        "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[2]/tbody/tr/td/div/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/text()").get()

    return CompanyItem(company_name=company_name, company_brn=company_brn)
