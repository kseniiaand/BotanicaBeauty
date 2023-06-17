from webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from webelements.actions import Actions


class Filters:
    def __init__(self,browser):
        self.actions = Actions(browser)
        self.categories_btn = Element(browser, By.XPATH, "//*[@id='categories_block']")
        self.categories_dropdown = Element(browser, By.ID, "ul_list_categories")
        self.black_friday_deals_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[1]")
        self.christmas_collection_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[2]")
        self.curly_perfection_bundle_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[3]")
        self.coily_love_bundle_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[4]")
        self.new_products_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[5]")
        self.treatment_bundle_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[6]")
        self.value_set_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[7]")
        self.waves_all_day_btn = Element(browser, By.XPATH, "//*[@id='ul_list_categories']/li[8]")
        self.vendors_btn = Element(browser, By.XPATH, "//*[@id='shopbyvendor']")
        self.vendors_dropdown = Element(browser, By.ID,  "ul_catalog_vendor")
        self.botanika_beauty_btn = Element(browser, By.XPATH, "//*[@id='ul_catalog_vendor']/li")
        self.types_btn = Element(browser, By.XPATH, "//*[@id='shopbytype']")
        self.types_dropdown = Element(browser, By.ID, "ul_catalog_type")
        self.gift_cards_btn = Element(browser, By.XPATH, "//*[@id='ul_catalog_type']/li")
        self.left_price_slider = Element(browser, By.XPATH, "//*[@id='js-slider-range']/span[1]")
        self.right_price_slider = Element(browser, By.XPATH, "//*[@id='js-slider-range']/span[2]")


    def show_black_friday_deals(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.black_friday_deals_btn.click()

    def show_christmas_collection(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.christmas_collection_btn.click()

    def show_curly_perfection_bundle(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.curly_perfection_bundle_btn.click()

    def show_coily_love_bundle(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.coily_love_bundle_btn.click()

    def show_new_products(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.new_products_btn.click()

    def show_treatment_bundle(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.treatment_bundle_btn.click()

    def value_set_bundle(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.value_set_btn.click()

    def waves_all_day_category(self):
        self.categories_btn.click()
        self.categories_dropdown.wait_until_visible()
        self.waves_all_day_btn.click()

    def show_botanika_beauty_category(self):
        self.vendors_btn.click()
        self.vendors_dropdown.wait_until_visible()
        self.botanika_beauty_btn.click()

    def show_gift_cards(self):
        self.types_btn.click()
        self.types_dropdown.wait_until_visible()
        self.gift_cards_btn.click()

    def move_the_left_slider(self):
        self.actions.drag_and_drop(self.left_price_slider)

    def move_the_right_element(self):
        self.actions.drag_and_drop(self.right_price_slider)