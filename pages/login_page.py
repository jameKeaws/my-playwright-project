from playwright.sync_api import sync_playwright
import re
class LoginPage():
    logo_in_header_locator = '//*[@id="header"]/div/div[1]/a/img'
    email_address_aria_label = 'Email address'
    password_aria_label = 'Password'
    login_button_name = 'Login'
    
    def __init__(self, page):
        self.page = page
        
    def navigate_to_homepage(self, wait_time=3000):
        print("LoginPage - navigate_to_homepage()")
        self.page.locator(type(self).logo_in_header_locator).click()
        self.page.wait_for_timeout(wait_time)
    
    # Functionality to input email address
    def input_email_address(self, email_address='enter_applicable_email', wait_time=2000):
        print("LoginPage - input_email_address()")
        self.page.get_by_label(type(self).email_address_aria_label).fill(email_address)
        self.page.wait_for_timeout(wait_time)
    
    # Functionality to input password
    def input_password(self, password='enter_applicable_password', wait_time=2000):
        print("LoginPage - input_password()")
        self.page.get_by_label(type(self).password_aria_label).fill(password)
        self.page.wait_for_timeout(wait_time)
        
    # Functionality to click on 'Login' button
    def click_login(self, wait_time=3000):
        print("LoginPage - click_login()")
        self.page.get_by_role("button", name=re.compile("Login", re.IGNORECASE)).click()
        self.page.wait_for_timeout(wait_time)
        
        
        
    