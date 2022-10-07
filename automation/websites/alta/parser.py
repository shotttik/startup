from bs4 import BeautifulSoup
from tools import remove_spaces


class Main:

    @staticmethod
    def parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        # image
        image = soup.find('div', {'class': 'ty-product-img'}).img['src']
        # title
        title = soup.find(
            'div', {'class': 'nj_custom_product_title_product_page'}).text
        # price
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

        return {'image': image, 'title': title, 'price': price, 'gpu': gpu}
