from urllib.request import urlopen
from bs4 import BeautifulSoup

def geturlText(url):
    page=urlopen(url).read()
    # print(page)
    soup=BeautifulSoup(page, 'lxml')
    fetched_text=' '.join(map(lambda p: p.text, soup.find_all('p')))
    # print(fetched_text)
    return fetched_text