# https://playwright.dev/python/docs/pom
class HomePageAsync():
    cookies_accept_button_locator = '#onetrust-accept-btn-handler'
    
    def __init__(self, page):
        self.page = page
        
    async def navigate(self, website_url):
        print("HomePageAsync - navigate()")
        await self.page.goto(website_url)
    
    # https://stackoverflow.com/questions/25577578/can-i-access-a-class-variable-from-an-instance
    async def click_accept_cookies(self, wait_time=2000):
        print("HomePageAsync - click_accept_cookies()")
        # We are locating by CSS selector where element id = onetrust-accept-btn-handler
        # page.locator("#onetrust-accept-btn-handler").click()
        await self.page.locator(type(self).cookies_accept_button_locator).click()
        await self.page.wait_for_timeout(wait_time)