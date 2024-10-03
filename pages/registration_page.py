class RegistrationPage():
    logo_in_header_locator = '//*[@id="header"]/div/div[1]/a/img'
    
    def __init__(self, page):
        self.page = page
        
    def navigate_to_homepage(self, wait_time=3000):
        print("RegistrationPage - navigate_to_homepage()")
        self.page.get_by_alt_text("The Perth Mint").click()
        self.page.wait_for_timeout(wait_time)