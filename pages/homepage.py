# https://playwright.dev/python/docs/pom
# https://stackoverflow.com/questions/25577578/can-i-access-a-class-variable-from-an-instance
# https://pynative.com/python-class-variables/#:~:text=A%20class%20variable%20is%20declared,constructor%20method%20and%20other%20methods.

class HomePage():
    cookies_accept_button_locator = '#onetrust-accept-btn-handler'
    
    def __init__(self, page):
        self.page = page
        
    def navigate(self, website_url):
        self.page.goto(website_url)
    
    # https://stackoverflow.com/questions/25577578/can-i-access-a-class-variable-from-an-instance
    def click_accept_cookies(self, wait_time=2000):
        print("HomePage - click_accept_cookies()")
        # We are locating by CSS selector where element id = onetrust-accept-btn-handler
        # page.locator("#onetrust-accept-btn-handler").click()
        self.page.locator(type(self).cookies_accept_button_locator).click()
        self.page.wait_for_timeout(wait_time)