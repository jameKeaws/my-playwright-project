from playwright.sync_api import sync_playwright
import re

class MainNavigation():
    # search_icon_locator = '.header__sub-nav-item.header__nav-item--search'
    search_icon_locator = '//*[@id="header-navigation--desktop"]/div/div/nav/ul[2]/li[5]/button'
    search_text_field_locator = '//*[@id="search-desktop"]/div/input'
    search_bar_button_locator = '//*[@id="search-desktop"]/div/button[1]'
    login_register_regex = 'login or register'
    logo_in_header_locator = '//*[@id="header-navigation--desktop"]/div/div/div/a/img'
    
    def __init__(self, page):
        self.page = page
        
    def click_search_icon(self, wait_time=2000):
        print("MainNavigation - click_search_icon()")
        # We are locating by CSS selector where classes are as specified below
        # page.locator('.header__sub-nav-item.header__nav-item--search').click()
        # self.page.locator(type(self).search_icon_locator).click()
        self.page.get_by_role("button", name="Search").click()
        self.page.wait_for_timeout(wait_time)
        
    def input_search(self, value_to_search='James', wait_time=2000):
        print("MainNavigation - input_search()")
        # Below is how it was originally called without Page object model
        # page.locator('//*[@id="search-desktop"]/div/input').fill(value_to_search)
        # self.page.locator(type(self).search_text_field_locator).fill(value_to_search)
        self.page.get_by_role("textbox", name="What are you looking for?").fill(value_to_search)
        self.page.wait_for_timeout(wait_time)
        
    def click_search_bar_button(self, wait_time=5000):
        print("MainNavigation - click_search_bar_button()")
        # Below is how it was originally called without Page object model
        # page.locator('//*[@id="search-desktop"]/div/button[1]').click()
        # page.wait_for_timeout(5000)
        self.page.locator(type(self).search_bar_button_locator).click()
        self.page.wait_for_timeout(wait_time)
        
    # Functionality for opening the 'Login/Register' via the main navigation panel
    def open_login_register_panel(self, wait_time=3000):
        print("MainNavigation - open_login_register_panel()")
        # RegEx starts with
        self.page.get_by_role("button", name=re.compile("^login or register", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)
    
    # Functionality for opening Cart (Quick cart icon) via the main navigation panel
    def open_quick_cart(self, wait_time=3000):
        print("MainNavigation - open_quick_cart()")
        # RegEx ends with
        self.page.get_by_role("button", name=re.compile("open cart$", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)
    
    # Functionality for opening 'Country and currency settings' via the main navigation panel
    def open_country_currency_settings(self, wait_time=3000):
        print("MainNavigation - open_country_currency_settings()")
        self.page.get_by_role("button", name=re.compile("^Change country and currency settings", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)
        
    # Functionality for reloading the default home page by clicking on company logo
    def load_default_homepage(self, wait_time=3000):
        print("MainNavigation - load_default_homepage()")
        self.page.locator(type(self).logo_in_header_locator).click()
        self.page.wait_for_timeout(wait_time)
        
    def open_collector_coins_menu(self, wait_time=3000):
        print("MainNavigation - open_collector_coins_menu()")
        self.page.get_by_role("button", name=re.compile("^Collector coins", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)