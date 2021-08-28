from bs4 import BeautifulSoup as bs
import requests
from AppendRows import AppendRows


def FirFindLink(ws, link):
    r = requests.get(link)
    soup = bs(r.text, 'html.parser')
    table = soup.find_all('tr')
    for line in table:

        cell = line.find('td')
        try:
            name = cell.find('a')
            link = name.get('href')
            try:
                ws = FindInfo(ws, 'https://en.m.wikipedia.org/' + link)
            except Exception:
                print('nope')
        except Exception:
            continue
    return ws


def FindInfo(ws, link):
    r = requests.get(link)
    soup = bs(r.text, 'html.parser')
    table = soup.find('table', {'class': 'infobox biography vcard'})
    try:
        name = table.find('div', {'class': 'fn'}).text
        ws = AppendRows(ws, name, table)

    except Exception:
        print('')
    return ws
