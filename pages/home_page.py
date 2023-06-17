from components import NavigationBar

class HomePage:
    def __init__(self, browser):
        self.navbar = NavigationBar(browser)

    def open_shop_all_products(self):
        self.navbar.shop_all_products()

    def open_new_products(self):
        self.navbar.shop_new_products()