from automation.webdriver import Browser
from automation.websites.sites import WEBSITES
from automation.config import config_browser
from automation.elements.Button import Button, BaseElement
from automation.websites.alta.locators import AltaLocators


class FindBetter:

    @classmethod
    def search(cls):
        browser_i = Browser(config_browser)
        for website in WEBSITES:
            browser_i.driver.get(website)
            if 'alta' in website:
                cls.alta()
                lpt_btn = Button(AltaLocators.LAPTOPS_CATEGORY,
                                 'Laptop Category BTN')
                lpt_btn.do_click_with_action()
            elif 'zoommer' in website:
                cls.zoommer()
            elif 'ultra' in website:
                cls.ultra()
        browser_i.quit()
