import requests 
from bs4 import BeautifulSoup
import re

import get_links
from get_links import all_links, get_request
from parss_links import inside_do_parse
from csvsave import csv_save



get_links.all_pages()
final_links = sum(all_links, [])

def main():
    n = 0
    while len(final_links) > n:
        inside_link = "https://ss.ge" + final_links[n]
        title, price, area, floor = inside_do_parse(get_request(inside_link))
        csv_save(title, price, area, floor)
        
        n += 1



if __name__ == "__main__":
    main()