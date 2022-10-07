from bs4 import BeautifulSoup
from tools import remove_spaces


class ParseAlta:

    @staticmethod
    def parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find(
            'div', {'class': 'nj_custom_product_title_product_page'}).text

        price: str = soup.find('span', {'class': 'ty-price-num'}).text

        # get gpu information
        features = soup.find_all(
            'div', {'class': 'ty-product-feature'})

        for f in features:
            label = f.find('span', {'class': 'ty-product-feature__label'}).text
            if label == 'გრაფიკული კონტროლერი:':
                gpu = f.find(
                    'div', {'class': 'ty-product-feature__value'}).text
                break
