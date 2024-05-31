import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')


soup = bs4.BeautifulSoup(result.text, 'lxml')


table_of_contents = soup.select('.vector-toc-contents')


print(table_of_contents)
