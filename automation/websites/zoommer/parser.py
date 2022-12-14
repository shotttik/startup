from bs4 import BeautifulSoup
import re
from tools import remove_spaces


class Main:

    @staticmethod
    def parser(html):
        soup = BeautifulSoup(html, 'html.parser').find(
            'div', {'class': 'body'})

        # image
        image = soup.find('div', {'class': 'current-image'}).img['src']
        # title
        t = soup.find('h1', {'class': 'n-product-title-text'}).text
        title = remove_spaces(t)

        p = soup.find('div', {'class': 'price'}).text
        # removing unciode characters
        clean_p = p.encode("ascii", "ignore").decode()
        # removing spaces and price character 'ლ'
        price: str = remove_spaces(clean_p)[:-1]

        # GPU
        rows = soup.find('div', {'id': 'n-prod-spec'}
                         ).find_all('div', {'class': 'row'})
        gpu = None
        for row in rows:
            cols = row.find_all('div', {'class': 'column'})
            if 'ვიდეობარათის მოდელი:' in cols[0].text:
                gpu = remove_spaces(cols[1].text)
                break
                # @TODO need to scrape gpu list and give gpu value

        return {'image': image, 'title': title, 'price': price, 'gpu': gpu}
