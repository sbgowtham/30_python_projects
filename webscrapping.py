import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://codewithgowtham.blogspot.com/2021/03/sqoop-commands.html')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))