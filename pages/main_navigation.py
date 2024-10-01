from playwright.sync_api import sync_playwright
import re

class MainNavigation():
    search_icon_locator = '.header__sub-nav-item.header__nav-item--search'
    search_text_field_locator = '//*[@id="search-desktop"]/div/input'
    search_bar_button_locator = '//*[@id="search-desktop"]/div/button[1]'
    
    def __init__(self, page):
        self.page = page
        
    def click_search_icon(self, wait_time=2000):
        print("MainNavigation - click_search_icon()")
        # Below is how it was originally called without Page object model
        # We are locating by CSS selector where classes are as specified below
        # page.locator('.header__sub-nav-item.header__nav-item--search').click()
        self.page.locator(type(self).search_icon_locator).click()
        
    def input_search(self, value_to_search='James', wait_time=2000):
        print("MainNavigation - input_search()")
        # Below is how it was originally called without Page object model
        # page.locator('//*[@id="search-desktop"]/div/input').fill(value_to_search)
        self.page.locator(type(self).search_text_field_locator).fill(value_to_search)
        self.page.wait_for_timeout(wait_time)
        
    def click_search_bar_button(self, wait_time=5000):
        print("MainNavigation - click_search_bar_button()")
        # Below is how it was originally called without Page object model
        # page.locator('//*[@id="search-desktop"]/div/button[1]').click()
        # page.wait_for_timeout(5000)
        self.page.locator(type(self).search_bar_button_locator).click()
        self.page.wait_for_timeout(wait_time)
        
    def click_quick_cart(self, wait_time=3000):
        print("MainNavigation - click_quick_cart()")
        self.page.get_by_role("button", name=re.compile("open cart$", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)