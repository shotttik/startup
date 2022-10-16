from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Browser():

    instance = None

    def __new__(cls, config_browser, url=None):

        if cls.instance is None:
            cls.__instance = super(Browser, cls).__new__(cls)
            cls.browser = config_browser["browser"]
            cls.wait_time = config_browser["wait_time"]
            chrome_options = webdriver.ChromeOptions()

            [
                chrome_options.add_argument(option)
                for option in config_browser["options"]
            ]

            if config_browser["browser"] == 'chrome':
                cls.driver = webdriver.Chrome(service=Service(
                    ChromeDriverManager().install()), options=chrome_options)
            elif config_browser["browser"] == 'firefox':
                cls.driver = webdriver.Firefox(service=Service(
                    GeckoDriverManager().install()), options=chrome_options)
            else:
                assert ("Support for Firefox or Chrome only!")
            if url:
                cls.driver.get(url)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        return cls.__instance.driver

    @classmethod
    def change_window(cls, id):
        cls.__instance.driver.switch_to.window(
            cls.__instance.driver.window_handles[id])

    @classmethod
    def quit(cls):
        return cls.__instance.driver.quit()
