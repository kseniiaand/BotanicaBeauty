from components import navigation_bar

class HomePage:
    def __init__(self, browser):
        self.navbar = navigation_bar(browser)

    def open_shop_all_products(self):
        self.navbar.open_shop_all_products

    def open_new_products(self):
        self.navbar.open_shop_new_products