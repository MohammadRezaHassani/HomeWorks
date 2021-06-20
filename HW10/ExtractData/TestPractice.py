from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from urllib.parse import urljoin

html_text = requests.get('https://www.sampadia.com/forum/').text
soup = BeautifulSoup(html_text, 'lxml')
input_form = soup.find('form')
fields = input_form.find_all('input')

for field in fields:

    print(field)
    print('****************************')
