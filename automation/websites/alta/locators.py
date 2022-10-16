from selenium.webdriver.common.by import By
WAIT_TIME = 5


class AltaLocators:
    @staticmethod
    def get_competitive_locator(first_price):
        return (By.XPATH, f"//span[@class='ty-price-num' and (number() - {first_price} >= 300)]/../../../parent::form//div[@class='ty-grid-list__item-name']")

    LAPTOPS_CATEGORY = (
        By.XPATH, "//div[@class='top-category']//a[contains(text(), 'ნოუთბუქები')]")

    PRODUCT_COL = (By.XPATH, "//div[contains(@class,'ty-column3')]")
    PRODUCT_PRICE = (By.XPATH, "//span[@class='ty-price-num']")
    PRODUCT_TITLE = (By.XPATH, "//div[@class='ty-grid-list__item-name']//a")

    PAGINATION_NEXT_BTN = (
        By.XPATH, "//a[contains(@class, 'ty-pagination__next')]")
