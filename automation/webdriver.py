from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from automation.websites.alta.locators import AltaLocators, WAIT_TIME
from selenium.webdriver.common.action_chains import ActionChains


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
    def close_current_window(cls):
        cls.__instance.driver.close()

    @classmethod
    def open_link_in_new_tab(cls, url):
        cls.__instance.driver.execute_script(f"window.open('{url}');")
        cls.change_window(1)

    @classmethod
    def scroll_to_element(cls, el):
        cls.__instance.driver.execute_script(
            "arguments[0].scrollIntoView(true);", el)

    @classmethod
    def wait_to_element_located(cls, selector):
        return WebDriverWait(cls.__instance.driver, WAIT_TIME).until(
            EC.presence_of_element_located(selector))

    @classmethod
    def wait_to_change_url(cls):
        return WebDriverWait(cls.__instance.driver, WAIT_TIME).until(
            EC.url_changes(cls.__instance.driver.current_url))

    @classmethod
    def wait_element_to_be_clickable(cls, selector):
        return WebDriverWait(cls.__instance.driver, WAIT_TIME).until(
            EC.element_to_be_clickable(selector))

    @classmethod
    def do_click_with_action(cls, selector):
        el = WebDriverWait(cls.__instance.driver, WAIT_TIME).until(
            EC.presence_of_element_located(selector))
        actions = ActionChains(Browser.getInstance())
        actions.move_to_element(el).click().perform()

    @classmethod
    def quit(cls):
        return cls.__instance.driver.quit()
