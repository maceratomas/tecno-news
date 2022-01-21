from bs4 import BeautifulSoup
import requests

def last_five_tecno_news():
    url = 'https://www.infobae.com/tecno/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tecno_news = soup.find_all('h2', 'nd-feed-list-card-headline-lean')
    last_five_news = []
    quantity = 5  # the limit is 20

    def clean_h2(element):
        characters = str(element)
        acum = ''
        for i in range(44, (len(characters)-5)):
            acum += characters[i]
        
        return acum

    for i in range(quantity):
        last_five_news.append( clean_h2(tecno_news[i]) )
    
    return last_five_news