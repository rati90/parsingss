import requests 
from bs4 import BeautifulSoup

def inside_do_parse(soup):
    title = soup.find("div", {"class":"article_in_title"}).find('h1').text
    try:
        price = soup.find("div", {"class":"article_right_price price"}).text.strip()
    except AttributeError:
        price = "ფასი შეთანხმებით"

    area = soup.find("div", {"class":"EAchParamsBlocks WholeFartBlock"}).find("div", {"class":"ParamsHdBlk"}).text.strip()
    try:
        rooms = soup.find("div", {"class":"EAchParamsBlocks RoomsParBlock"}).find("div", {"class":"ParamsHdBlk"}).text.strip()
    except AttributeError:
        rooms = "N/A"

    return (title, price, area, rooms)