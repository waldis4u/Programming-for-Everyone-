from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com.gh/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
