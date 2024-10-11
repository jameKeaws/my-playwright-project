import re
class ProductDetailsPage():
    add_to_cart_button_css_class = '.button.button--large'
    add_to_cart_plus_button_locator = '//*[@id="mainContent"]/div[1]/div[2]/div/div/div[2]/div[6]/div[1]/span/span/button[2]'
    add_to_cart_minus_button_locator = '//*[@id="mainContent"]/div[1]/div[2]/div/div/div[2]/div[6]/div[1]/span/span/button[1]'
    
    def __init__(self, page):
        self.page = page
    
    def click_add_to_cart(self, wait_time=3000):
        print("ProductDetailsPage - click_add_to_cart()")
        # add_to_cart_button = self.page.get_by_role("button", name=re.compile("Add to cart", re.IGNORECASE)).and_(self.page.locator(type(self).add_to_cart_button_css_class))
        # add_to_cart_button.click()
        self.page.get_by_role("button", name="Add to cart").first.click()
        self.page.wait_for_timeout(wait_time)
    
    def use_plus_button(self, how_much_more_to_add=1, wait_time=3000):
        print("ProductDetailsPage - use_plus_button()")
        for i in range(how_much_more_to_add):
            # Original way we called it
            # self.page.locator(type(self).add_to_cart_plus_button_locator).click()
            self.page.get_by_role("button", name="Increase quantity +").click()
        self.page.wait_for_timeout(wait_time)
        
    def use_minus_button(self, how_much_to_subtract=1, wait_time=3000):
        print("ProductDetailsPage - use_minus_button()")
        for i in range(how_much_to_subtract):
            self.page.get_by_role("button", name="Decrease quantity −").click()
        self.page.wait_for_timeout(wait_time)
    