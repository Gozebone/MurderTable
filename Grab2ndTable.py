from bs4 import BeautifulSoup as bs
import requests
from AppendRows import AppendRows


def SecFindLink(ws, link):
    r = requests.get(link)
    soup = bs(r.text, 'html.parser')
    links = soup.find('div', {'class': 'mw-category'})
    for link in links.find_all('a'):
        ws = FindInfo(ws, 'https://ru.m.wikipedia.org/' + link.get('href'))
    return ws


def FindInfo(ws, link):
    r = requests.get(link)
    soup = bs(r.text, 'html.parser')
    table = soup.find('table', {'class': 'infobox'})

    try:
        name = table.find('th').text
        AppendRows(ws, name, table)

    except Exception:
        print('')
    return ws
