from playwright.sync_api import sync_playwright
import re

class CountryCurrencySettings():
    def __init__(self, page):
        self.page = page
        
    def close_country_and_currency_settings(self, wait_time=3000):
        print("CountryCurrencySettings - close_country_and_currency_settings()")
        self.page.get_by_role("button", name=re.compile("Close Country and Currency controls", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)