from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from automation.websites.alta.locators import AltaLocators, WAIT_TIME
from automation.webdriver import Browser
from automation.websites.alta.parser import Main
from bs4 import BeautifulSoup

import pandas as pd
import logging
LOGGER = logging.getLogger(__name__)


class AltaProducts:

    @staticmethod
    def _get_value_of_gpu(df, gpu):
        gpu_df = df.loc[df['Model'] == gpu + ' Laptop GPU']
        return 0 if gpu_df.empty else gpu_df.iloc[0]._name

    @classmethod
    def compare_gpus(cls, gpu1, gpu2):
        df = pd.read_csv("automation/Resources/gpus_data.csv")
        # example NVIDIA Geforce RTX 3050 Laptop GPU
        gpu1_val = cls._get_value_of_gpu(df, gpu1)
        gpu2_val = cls._get_value_of_gpu(df, gpu2)
        # gpu1 is given and should be greater than gpu2
        return gpu1_val > gpu2_val

    @classmethod
    def inspect_products(cls, gpu, price):

        WebDriverWait(Browser.getInstance(), WAIT_TIME).until(
            EC.presence_of_element_located(AltaLocators.LAPTOPS_CATEGORY)).click()
        ####################
        soup = BeautifulSoup(
            Browser.getInstance().page_source, 'html.parser')
        products = soup.find_all('div', {'class': 'ty-column3'})
        if not products:
            LOGGER.info('Products not found')
            return {"status": "error"}

        while True:
            for p in products:
                p_price = p.find('span', {'class': 'ty-price-num'}).text
                if int(price) - int(p_price) >= 400:
                    continue
                else:
                    p_url = p.find('a', {'class': 'product-title'}).get('href')
                    Browser.open_link_in_new_tab(p_url)
                    data = Main.parser(Browser.getInstance().page_source)
                    if cls.compare_gpus(data["gpu"], gpu):
                        LOGGER.info("Found Cheaper Product")
                        return {"status": "success", "data": data}
                    Browser.close_current_window()
                    Browser.change_window(id=0)
                    #########
            pagination_next = Browser.getInstance().find_elements(
                *AltaLocators.PAGINATION_NEXT_BTN)
            if pagination_next:
                Browser.scroll_to_element(pagination_next[0])
                pagination_next[0].click()
            else:
                LOGGER.info("Can't find cheaper product")
                return {"status": "not_found"}
