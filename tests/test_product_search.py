from pages.home_page import HomePage


def test_product_search(driver):
    home = HomePage(driver)
    home.open()

    products = home.go_to_products()
    products.search_product("Dress")
    products.wait_for_results()

    assert products.results_count() > 0
