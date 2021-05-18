from .items import CompanyItem


def extract_company_details(response, given_brn):
    try:
        company_brn = ''.join(response.xpath(
            "//td")[25].xpath(".//text()").getall()).strip()
        company_name = ''.join(response.xpath(
            "//td")[26].xpath(".//text()").getall()).strip()
    except:
        company_brn = None
        company_name = None

    return CompanyItem(company_name=company_name, company_brn=company_brn, given_number=given_brn)
