import requests
import bs4

# with select we can select anything with css selectors

result = requests.get('https://www.example.com')

soup = bs4.BeautifulSoup(result.text, 'lxml')

title = soup.select('title')[0].getText()
first_site_paragraph = soup.select('p')[0].getText()

print(title, '\n', first_site_paragraph)
