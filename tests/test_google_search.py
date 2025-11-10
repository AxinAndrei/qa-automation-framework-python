from pages.google_home_page import GoogleHomePage

def test_google_search(driver):
    google = GoogleHomePage(driver)
    google.open()
    google.search_for("Selenium Python")
    assert "Selenium" in google.get_title()
