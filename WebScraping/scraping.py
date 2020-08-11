
import requests
from bs4 import BeautifulSoup


def scrap():
    url = "https://www.zalando.no/salg/?sale=true"
    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, 'html.parser')
    all = soup.select('z-navicat-header_navSectionContainer')
    for a in all:
        print(a)


if __name__ == '__main__':
    scrap()