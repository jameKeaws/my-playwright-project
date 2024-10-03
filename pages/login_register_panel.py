from playwright.sync_api import sync_playwright
import re

class LoginRegisterPanel():
    # TODO There must be a better way of locating these elements
    login_button_href_value = '//a[@href="/B2CLogin/SignIn"]'
    login_button_css_class = '.button.button--large'
    # login_button_locator = '//*[@id="4c92174d-127b-45dc-8813-77a922461e72-1"]/div/div/div[1]/div[2]/a'
    register_button_href_value = '//a[@href="/B2CLogin/SignUp"]'
    register_button_css_class = '.button.button--large'
    # register_button_locator = '//*[@id="4c92174d-127b-45dc-8813-77a922461e72-1"]/div/div/div[2]/div[2]/a'
    
    def __init__(self, page):
        self.page = page
        
    def close_login_register_panel(self, wait_time=3000):
        # print(type(self).login_button_locator)
        print("LoginRegisterPanel - close_login_register_panel()")
        self.page.get_by_role("button", name=re.compile("Close Login", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)
    
    # Functionality to click the 'Login' button
    # https://playwright.dev/python/docs/locators#matching-two-locators-simultaneously
    # https://playwrightsolutions.com/how-can-i-create-a-locator-from-a-link-with-a-unique-href-in-playwright/
    # https://stackoverflow.com/questions/76624911/get-href-link-using-python-playwright
    def navigate_to_account_login(self, wait_time=3000):
        print("LoginRegisterPanel - navigate_to_account_login()")
        login_button = self.page.locator(type(self).login_button_href_value).and_(self.page.locator(type(self).login_button_css_class))
        login_button.click()
        self.page.wait_for_timeout(wait_time)
    
    # Functionality to click the 'Register' button
    def navigate_to_account_registration(self, wait_time=3000):
        print("LoginRegisterPanel - navigate_to_account_registration()")
        register_button = self.page.locator(type(self).register_button_href_value).and_(self.page.locator(type(self).register_button_css_class))
        register_button.click()
        self.page.wait_for_timeout(wait_time)