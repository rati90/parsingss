import requests 
from bs4 import BeautifulSoup
import re


some_links = []
all_links = []

def get_all_links(data):
    find_all_a = data.find_all("a", href=re.compile("/ka/udzravi-qoneba/iyideba-"))
    for el in find_all_a:
        if el not in some_links:
            some_links.append(el['href'])
        else:
            None

    all_links.append(list(set(some_links)))


def do_parse(soup):
    data = soup.find("div", {"class":"all_page_blocks"})
    
    get_all_links(data)


def get_request(GLOBAL_URL):
    req = requests.get(GLOBAL_URL)
    return BeautifulSoup(req.text, "html.parser")


def all_pages():
    for page in range(1, 2):
        URLstar = "https://ss.ge/ka/udzravi-qoneba/l/bina/iyideba?Page="
        URLfinish = "&RealEstateTypeId=5&RealEstateDealTypeId=4&MunicipalityId=95&CityIdList=95&subdistr=44&StatusField.FieldId=34&StatusField.Type=SingleSelect&StatusField.StandardField=Status&PriceType=false&CurrencyId=1"
        GLOBAL_URL = URLstar + str(page) + URLfinish

        do_parse(get_request(GLOBAL_URL))   



