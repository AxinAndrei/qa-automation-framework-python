from selenium import webdriver

def create_driver(browser="chrome", headless=False):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        return webdriver.Chrome(options=options)