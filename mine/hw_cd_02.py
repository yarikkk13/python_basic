import requests
from bs4 import BeautifulSoup

url = "https://google.com.ua/"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
listOfLinks = []
subLinks = []
errors = []
for link in soup.find_all('a'):
    tup = {link.text, link.get('href')}
    listOfLinks.append(tup)
    try:
        req2 = requests.get(link.get('href'))
        soup2 = BeautifulSoup(req2.text, 'html.parser')
    except Exception as e:
        errors.append(e)
    for subLink in soup2.find_all('a'):
        tup2 = {subLink.text, subLink.get('href')}
        subLinks.append(tup2)

print(listOfLinks)
print(errors)
print(subLinks)
