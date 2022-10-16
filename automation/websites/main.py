from automation.webdriver import Browser
from automation.websites.sites import WEBSITES
from automation.config import config_browser
from automation.elements.Button import Button, BaseElement
from automation.websites.alta.locators import AltaLocators


class FindBetter:

    @staticmethod
    def zoommer():
        pass

    @staticmethod
    def alta(price, gpu):
        lpt_btn = Button(AltaLocators.LAPTOPS_CATEGORY, 'Laptop Category BTN')
        lpt_btn.do_click_with_action()
        Browser.getInstance()
        # this for to get competitive products only
        product_columns = BaseElement(
            AltaLocators.PRODUCT_COL, 'Product column')
        products = product_columns.get_multiple_elements()

    @classmethod
    def search(cls):
        browser_i = Browser(config_browser)
        for website in WEBSITES:
            browser_i.driver.get(website)
            if 'alta' in website:
                cls.alta()
            elif 'zoommer' in website:
                cls.zoommer()
            elif 'ultra' in website:
                cls.ultra()
        browser_i.quit()