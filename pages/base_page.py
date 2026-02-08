import logging
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logging.getLogger(__name__)

    def handle_cookies(self):
        try:
            self.logger.info("Removing cookie & ad overlays")
            self.driver.execute_script("""
                let overlays = document.querySelectorAll(
                    '.fc-dialog-overlay, .fc-consent-root, iframe, .adsbygoogle'
                );
                overlays.forEach(el => el.remove());
            """)
        except Exception:
            pass

    def click(self, locator):
        try:
            self.handle_cookies()
            self.logger.info(f"Clicking on element: {locator}")

            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

        except Exception:
            self.take_screenshot("click_error")
            raise

    def enter_text(self, locator, text):
        try:
            self.handle_cookies()
            self.logger.info(f"Entering text '{text}' into element: {locator}")
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception:
            self.take_screenshot("enter_text_error")
            raise

    def get_title(self):
        return self.driver.title

    def take_screenshot(self, name):
        screenshots_dir = "reports/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"{screenshots_dir}/{name}_{timestamp}.png"
        self.driver.save_screenshot(path)
