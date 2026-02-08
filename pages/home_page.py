from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.products_page import ProductsPage


class HomePage(BasePage):

    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")

    def open(self):
        self.driver.get("https://automationexercise.com")
        self.handle_cookies()

    def go_to_products(self):
        self.logger.info("Navigating to Products page")
        self.click(self.PRODUCTS_BUTTON)
        return ProductsPage(self.driver)
