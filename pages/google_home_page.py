from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class GoogleHomePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")
    ACCEPT_COOKIES = (By.XPATH, "//button[.//div[text()='Acceptă tot']]")

    def open(self):
        self.driver.get("https://www.google.com")

    def accept_cookies_if_present(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.ACCEPT_COOKIES)
            ).click()
        except:
            pass 

    def search_for(self, text):
        self.accept_cookies_if_present()
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search_box.send_keys(text + Keys.ENTER)
