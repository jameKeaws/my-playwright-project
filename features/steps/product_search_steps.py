from behave import *
from playwright.sync_api import sync_playwright
from pages.main_navigation import MainNavigation
from pages.homepage import HomePage

@given("a Google Chrome browser is at The Perth Mint home page : '{site_home_page}'")
def open_website(context, site_home_page):
    context.playwright = sync_playwright().start()
    chromium = context.playwright.chromium
    # Create a browser object which we could work with. By default the browser will be running headless = True
    browser = chromium.launch(headless=False, slow_mo=50, args=["--start-maximized"])
    # REFERENCE https://stackoverflow.com/questions/75144059/python-playwright-start-maximized-window
    # Create a new incognito browser context.
    context.browser = browser.new_context(no_viewport=True)
    # Create a new page in a pristine context. Create a page object which we could interact with
    context.page = context.browser.new_page()
    homepage = HomePage(context.page)
    # Navigate to website we want to test. For demonstration purposes we are using The Perth Mint
    homepage.navigate('https://www.perthmint.com/')
    # REFERENCE https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id
    # Click on OK button in "Our site uses cookies prompt"
    # We are locating by CSS selector where element id = onetrust-accept-btn-handler
    # page.locator("#onetrust-accept-btn-handler").click()
    homepage.click_accept_cookies()
    
# value_to_search value is coming from product_search.feature
@when("the user enters '{value_to_search}' into the search bar")
def search_product(context, value_to_search):
    main_navigation = MainNavigation(context.page)
    main_navigation.click_search_icon(wait_time=5000)
    main_navigation.input_search(value_to_search, wait_time=2000)
    main_navigation.click_search_bar_button(wait_time=5000)
    
@then("product cards related to '{value_to_search}' are shown on the search results page")
def verify_search_result(context, value_to_search):
    context.browser.close()
    context.playwright.stop()
