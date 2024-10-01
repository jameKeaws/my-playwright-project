class ProductCard():
    first_product_card_tile_url = '//*[@id="panel-Products"]/div[2]/div[1]/div/div[2]/div[1]/h3/a'
    
    def __init__(self, page):
        self.page = page
    
    def click_product_card_url(self, wait_time=5000):
        print("ProductCard - click_product_card_url()")
        # Below is how it was originally called without Page object model
        # page.locator('//*[@id="panel-Products"]/div[2]/div[1]/div/div[2]/div[1]/h3/a').click()
        # page.wait_for_timeout(5000)
        self.page.locator(type(self).first_product_card_tile_url).click()
        self.page.wait_for_timeout(wait_time)