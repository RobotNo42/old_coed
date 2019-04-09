import requests
from bs4 import BeautifulSoup

ret = requests.get(url='https://messilessblog.com/',headers='')
print(ret.text)