import requests
import bs4

result = requests.get('https://www.example.com')

soup = bs4.BeautifulSoup(result.text, 'lxml')

titles = soup.select('title')
