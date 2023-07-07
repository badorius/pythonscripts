from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

web_url = 'https://www.habitaclia.com/viviendas-sant_andreu_de_llavaneres.htm'
web_data = urlopen(web_url)
web_html = web_data.read()
web_data.close()
page_soup = soup(web_html, 'html.parser')

print(page_soup)

#print(page_soup.find_all('table', {'class': 'list-items'}))
#print(page_soup.find_all('table', {'class': 'list-items'}))