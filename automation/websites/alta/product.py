from automation.websites.alta.locators import AltaLocators, WAIT_TIME
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from automation.webdriver import Browser
import logging
LOGGER = logging.getLogger(__name__)


class AltaProducts:
    @classmethod
    def compare_products(price):
        products = WebDriverWait(Browser.getInstance(), WAIT_TIME).until(
            EC.presence_of_all_elements_located(AltaLocators.PRODUCT_COL))
        if not products:
            LOGGER.info('Products not found')

        for product in products:
            if int(product.find_element(*AltaLocators.PRODUCT_PRICE).text) - int(price) <= 300:
                product.find_element(*AltaLocators.PRODUCT_TITLE).click()
