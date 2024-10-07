class CollectorCoinsPage():
    # Below values might be changing from environment to environment
    item_xlarge_submenu_identifier = 'e78d6228-0f28-431d-a915-867e5d9cd61b'
    by_metal_gold_locator = '//*[@id="item-xlarge-e78d6228-0f28-431d-a915-867e5d9cd61b-submenu"]/div/div[1]/div[2]/ul/li[1]/a'
    by_metal_silver_locator = '//*[@id="item-xlarge-e78d6228-0f28-431d-a915-867e5d9cd61b-submenu"]/div/div[1]/div[2]/ul/li[2]/a'
    
    def __init__(self, page):
        self.page = page
    
    # https://stackoverflow.com/questions/21405267/how-to-use-regex-in-xpath-contains-function
    # https://stackoverflow.com/questions/12176723/xpath-search-for-divs-where-the-id-contains-specific-text
    def click_on_by_metal_gold(self, wait_time=3000):
        print("CollectorCoinsPage - click_on_by_metal_gold()")
        self.page.locator(type(self).by_metal_gold_locator).click()
        self.page.wait_for_timeout(wait_time)
        
    def click_on_by_metal_silver(self, wait_time=3000):
        print("CollectorCoinsPage - click_on_by_metal_silver()")
        self.page.locator(type(self).by_metal_silver_locator).click()
        self.page.wait_for_timeout(wait_time)
        
    
    