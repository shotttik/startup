from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from automation.websites.alta.locators import AltaLocators, WAIT_TIME
from automation.webdriver import Browser
from automation.websites.alta.parser import Main
from bs4 import BeautifulSoup
import time

import pandas as pd
import logging
LOGGER = logging.getLogger(__name__)


class AltaProducts:

    DF = pd.read_csv("automation/Resources/gpus_data.csv")

    @staticmethod
    def _get_value_of_gpu(df, gpu):
        gpu_df = df.loc[df['Model'] == gpu]
        return 0 if gpu_df.empty else gpu_df.iloc[0]._name

    @classmethod
    def compare_gpus(cls, gpu1, gpu2):
        # example NVIDIA Geforce RTX 3050 Laptop GPU
        gpu1_val = cls._get_value_of_gpu(cls.DF, gpu1)
        gpu2_val = cls._get_value_of_gpu(cls.DF, gpu2)
        # gpu1 is given and should be less than gpu2
        return gpu1_val < gpu2_val

    @classmethod
    def inspect_products(cls, gpu, price):

        Browser.wait_to_element_located(AltaLocators.LAPTOPS_CATEGORY).click()

        Browser.wait_to_element_located(AltaLocators.COOKIE_OK).click()
        while True:
            soup = BeautifulSoup(
                Browser.getInstance().page_source, 'html.parser')

            products = soup.find_all('div', {'class': 'ty-column3'})
            if not products:
                LOGGER.info('Products not found')
                return {"status": "error"}
            for p in products:
                p_price = p.find('span', {'class': 'ty-price-num'})
                if p_price is None:
                    continue
                diff = int(price) - int(p_price.text)
                if not (diff <= 400 and diff >= -100):
                    continue
                else:
                    p_url = p.find('a', {'class': 'product-title'}).get('href')
                    print(p_url)
                    Browser.open_link_in_new_tab(p_url)
                    data = Main.parser(Browser.getInstance().page_source)
                    if cls.compare_gpus(data["gpu"], gpu):
                        LOGGER.info("Found Cheaper Product")
                        return {"status": "success", "data": data}
                    Browser.close_current_window()
                    Browser.change_window(id=0)
            pagination_next = Browser.getInstance().find_elements(
                *AltaLocators.PAGINATION_NEXT_BTN)
            if pagination_next:
                Browser.getInstance().execute_script("window.scrollTo(0, 1350)")
                Browser.wait_to_element_located(
                    AltaLocators.PAGINATION_NEXT_BTN)
                Browser.wait_element_to_be_clickable(
                    AltaLocators.PAGINATION_NEXT_BTN).click()
            else:
                LOGGER.info("Can't find cheaper product")
                return {"status": "not_found"}

            Browser.wait_to_change_url()
