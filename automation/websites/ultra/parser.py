from bs4 import BeautifulSoup
from tools import remove_spaces, remove_characters
import re


class ParseUltra:

    @staticmethod
    def parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        right_info = soup.find(
            'div', {'class': 'col-sm-6 right_info'})
        title_soup = right_info.find(
            'ul', {'class': 'list-unstyled'}).find('h4')

        title = re.sub(r"^\S+\s", "", title_soup.text)

        price_soup = right_info.find('span', {'class': 'pro_price'})
        # '3,340.00ლ' get '3,340.'
        p = re.match(r'(.*\.+)', price_soup.text).group()
        price: str = remove_characters(p)

        description_rows = soup.find(
            'div', {'class': 'cpt_product_description'}).find_all('tr')
        for row in description_rows:
            if row.td.text == 'ვიდეო დაფის მოდელი':
                gpu = row.find_all('td')[1].text
                break
