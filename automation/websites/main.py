from automation.webdriver import Browser
from automation.websites.sites import WEBSITES
from automation.config import config_browser


class FindBetter:

    @classmethod
    def search():
        browser_i = Browser(config_browser)
