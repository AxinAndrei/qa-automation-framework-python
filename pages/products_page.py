from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCTS = (By.CSS_SELECTOR, ".productinfo p")

    def search_product(self, product):
        self.logger.info(f"Searching for product: {product}")
        self.enter_text(self.SEARCH_INPUT, product)
        self.click(self.SEARCH_BUTTON)

    def wait_for_results(self):
        self.logger.info("Waiting for products to load")
        self.wait.until(lambda d: len(d.find_elements(*self.PRODUCTS)) > 0)

    def results_count(self):
        return len(self.driver.find_elements(*self.PRODUCTS))
