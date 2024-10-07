from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import re
class RegistrationPage():
    logo_in_header_locator = '//*[@id="header"]/div/div[1]/a/img'
    first_name_aria_label = 'First name'
    last_name_aria_label = 'Last name'
    country_code_select_aria_label = 'Country'
    phone_number_aria_label = 'Phone number'
    email_address_aria_label = 'Email address'
    email_address_title = 'Email address that can be used to contact you.'
    terms_and_conditions_label_locator = '//*[@id="true_option"]'
    terms_and_conditions_checkbox_locator = '//*[@id="extension_AgreedToTermsAndConditions_true"]'
    
    def __init__(self, page):
        self.page = page
        
    def navigate_to_homepage(self, wait_time=3000):
        print("RegistrationPage - navigate_to_homepage()")
        self.page.get_by_alt_text("The Perth Mint").click()
        self.page.wait_for_timeout(wait_time)
    
    # Functionality to enter first name  
    def input_first_name(self, first_name='enter_first_name', wait_time=3000):
        print("RegistrationPage - input_first_name()")
        self.page.get_by_label(type(self).first_name_aria_label).fill(first_name)
        self.page.wait_for_timeout(wait_time)
        
    def input_last_name(self, last_name='enter_last_name', wait_time=3000):
        print("RegistrationPage - input_last_name()")
        self.page.get_by_label(type(self).last_name_aria_label).fill(last_name)
        self.page.wait_for_timeout(wait_time)
        
    def select_country_code(self, country_code='NZ', wait_time=3000):
        print("RegistrationPage - select_country_code()")
        self.page.get_by_label(type(self).country_code_select_aria_label).select_option(country_code)
        self.page.wait_for_timeout(wait_time)
    
    # Functionality to enter email address
    def input_phone_number(self, phone_number='414777555', wait_time=3000):
        print("RegistrationPage - input_phone_number()")
        self.page.get_by_label(type(self).phone_number_aria_label).fill(phone_number)
        self.page.wait_for_timeout(wait_time)
        
    def input_email_address(self, email_address='enter_email_address', wait_time=3000):
        print("RegistrationPage - input_email_address()")
        email_address_field = self.page.get_by_label(type(self).email_address_aria_label).and_(self.page.get_by_title(type(self).email_address_title))
        # self.page.get_by_label(type(self).email_address_aria_label).fill(email_address)
        email_address_field.fill(email_address)
        self.page.wait_for_timeout(wait_time)
    
    # TODO We need to fix this later or check with Development team if the layout could be adjusted
    # https://stackoverflow.com/questions/6293588/how-to-create-a-checkbox-with-a-clickable-label
    # https://testersdock.com/checkbox-playwright/
    # https://www.geeksforgeeks.org/how-to-create-an-html-checkbox-with-a-clickable-label/
    def trial_agree_to_terms_and_conditions(self, wait_time=3000):
        print("RegistrationPage - trial_agree_to_terms_and_conditions()")
        # self.page.get_by_role("checkbox", name="I have read and agree to the Terms and Conditions and Privacy Policy").click()
        # self.page.get_by_label('I have read and agree to the Terms and Conditions and Privacy Policy').check()
        # self.page.get_by_role("button", name=re.compile("^login or register", re.IGNORECASE)).click()
        # self.page.get_by_role("checkbox", name=re.compile("^I have read and agree to the ", re.IGNORECASE)).click()
        # self.page.locator('#true_option').check()
        # self.page.get_by_label(re.compile("^I have read and agree to the", re.IGNORECASE)).click()
        # self.page.get_by_role("checkbox", name=re.compile("^I have read and agree to the ", re.IGNORECASE)).check()
        # what = expect(self.page.get_by_label('I have read and agree to the ').to_be_enabled())
        # checkbox_enabled = expect(self.page.locator('//*[@id="extension_AgreedToTermsAndConditions_true"]').to_be_visible())
        # self.page.get_by_label(re.compile("^I have read and agree to the", re.IGNORECASE)).click()
        # is_visible = expect(self.page.get_by_role("checkbox", name=re.compile("^I have read and agree to the ", re.IGNORECASE)).to_be_visible())
        # print(is_visible)
        # self.page.get_by_label('I have read and agree to the ').check()
        # self.page.get_by_role("checkbox", name=re.compile("^I have read and agree to the ", re.IGNORECASE)).check()
        # self.page.locator('//*[@id="extension_AgreedToTermsAndConditions_true"]').click()
        self.page.locator('//*[@id="true_option"]').check()
        self.page.wait_for_timeout(wait_time)
        