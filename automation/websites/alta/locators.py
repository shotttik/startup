from selenium.webdriver.common.by import By


class AltaLocators:
    LAPTOPS_CATEGORY = (
        By.XPATH, "//div[@class='top-category']//a[contains(text(), 'ნოუთბუქები')]")

    PRODUCT_COL = (By.XPATH, "//div[contains(@class,'ty-column3 ')]")
    PRODUCT_PRICE = (By.XPATH, "//span[@class='ty-price-num']")
