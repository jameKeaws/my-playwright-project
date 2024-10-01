from playwright.sync_api import sync_playwright
import re

class QuickCart():
    def __init__(self, page):
        self.page = page
    
    def close_quick_cart(self, wait_time=3000):
        print("QuickCart - close_quick_cart()")
        self.page.get_by_role("button", name=re.compile("Close Cart", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)