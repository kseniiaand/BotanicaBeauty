from BotanicaBeauty.webelements.UIElement import UIElement as Element
from BotanicaBeauty.webdriver.common.by import  By

class HomePage:
    def __init__(self, browser):
        self.navbar = NavigationBar(browser)
        self.shop_btn = Element(browser, By.XPATH, "//a[contains(text(),'Shop Now')]")

    def open_shop_all_products(self):
        pass

    def click_shop_btn(self):
        self.shop_btn.click()