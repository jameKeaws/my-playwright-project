import asyncio
from playwright.async_api import async_playwright

# https://apidog.com/blog/await-in-playwright/
class MainNavigationAsync():
     # search_icon_locator = '.header__sub-nav-item.header__nav-item--search'
    search_icon_locator = '//*[@id="header-navigation--desktop"]/div/div/nav/ul[2]/li[5]/button'
    search_text_field_locator = '//*[@id="search-desktop"]/div/input'
    search_bar_button_locator = '//*[@id="search-desktop"]/div/button[1]'
    login_register_regex = 'login or register'
    logo_in_header_locator = '//*[@id="header-navigation--desktop"]/div/div/div/a/img'
    
    def __init__(self, page):
        self.page = page
        
     # Functionality for reloading the default home page by clicking on company logo
    async def load_default_homepage(self, wait_time=3000):
        print("MainNavigationAsync - load_default_homepage()")
        # self.page.locator(type(self).logo_in_header_locator).click()
        await self.page.get_by_role("link", name="The Perth Mint", exact=True).click()
        await self.page.wait_for_timeout(wait_time)
        
    async def click_search_icon(self, wait_time=2000):
        print("MainNavigationAsync - click_search_icon()")
        # We are locating by CSS selector where classes are as specified below
        # page.locator('.header__sub-nav-item.header__nav-item--search').click()
        # self.page.locator(type(self).search_icon_locator).click()
        await self.page.get_by_role("button", name="Search").click()
        await self.page.wait_for_timeout(wait_time)
        
    async def input_search(self, value_to_search='James', wait_time=2000):
        print("MainNavigationAsync - input_search()")
        # Below is how it was originally called without Page object model
        # page.locator('//*[@id="search-desktop"]/div/input').fill(value_to_search)
        # self.page.locator(type(self).search_text_field_locator).fill(value_to_search)
        await self.page.get_by_role("textbox", name="What are you looking for?").fill(value_to_search)
        await self.page.wait_for_timeout(wait_time)
        
    async def click_search_bar_button(self, wait_time=5000):
        print("MainNavigation - click_search_bar_button()")
        await self.page.locator("#search-desktop").get_by_label("Search").click()
        await self.page.wait_for_timeout(wait_time)