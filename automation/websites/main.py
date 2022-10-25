from automation.webdriver import Browser
from automation.websites.sites import WEBSITES
from automation.config import config_browser
from automation.elements.Button import Button, BaseElement
from automation.websites.alta.locators import AltaLocators
from automation.websites.alta.product import AltaProducts
from logger import CustomLogger

LOGGER = CustomLogger.get_logger(__name__)


class FindBetter:

    @classmethod
    def search(cls, gpu, price) -> dict:
        browser_i = Browser(config_browser())
        browser_i.driver.get(WEBSITES[0])
        data = None
        data = AltaProducts.inspect_products(gpu, price)
        return data
        try:
            data = AltaProducts.inspect_products(gpu, price)
        except Exception as e:
            LOGGER.info(e)
        finally:
            browser_i.quit()
            return data
        # @TODO find cheaper product in other supported websites
        # for website in WEBSITES:
        #     browser_i.driver.get(website)
        #     if 'alta' in website:
        #         data = AltaProducts.inspect_products(gpu, price)
        #     elif 'zoommer' in website:
        #         cls.zoommer()
        #     elif 'ultra' in website:
        #         cls.ultra()
