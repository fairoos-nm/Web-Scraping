import requests
from bs4 import BeautifulSoup

url = "https://coreyms.com/"

source_code = requests.get(url).text

soup = BeautifulSoup(source_code, 'lxml')

article =  soup.find("article")
#print(article.prettify())

headline = article.h2.a.text
print(headline)
