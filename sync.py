from playwright.sync_api import sync_playwright
from pages.homepage import HomePage
from pages.main_navigation import MainNavigation
from pages.product_card import ProductCard
from pages.quick_cart import QuickCart
from pages.country_and_currency import CountryCurrencySettings
from pages.login_register_panel import LoginRegisterPanel
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.collector_coins_page import CollectorCoinsPage
import re
# References
# https://playwright.dev/python/docs/api/class-playwright
# https://www.youtube.com/watch?v=H2-5ecFwHHQ
# https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A
# https://playwright.dev/python/docs/locators
# https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id
# https://stackoverflow.com/questions/75144059/python-playwright-start-maximized-window
# https://devhints.io/xpath#class-check
# https://www.roborabbit.com/blog/xpath-cheat-sheet-a-quick-reference-to-essential-xpath-expressions/#using-operators-to-combine-expressions
# https://stackoverflow.com/questions/22571267/how-to-verify-an-xpath-expression-in-chrome-developers-tool-or-firefoxs-firebug
# https://playwright.dev/python/docs/pom

# Use a context manager. 
# with sync_playwright() as playwright > This will close our browser when our code is finished running 
# thus preventing possible memory issues from any unclosed browsers used.
# TODO : Separate the functionalities later on.  I am just using this single file for testing of functionalities
with sync_playwright() as playwright:
    chromium = playwright.chromium
    # Create a browser object which we could work with. By default the browser will be running headless = True
    browser = chromium.launch(headless=False, slow_mo=50, args=["--start-maximized"])
    # REFERENCE https://stackoverflow.com/questions/75144059/python-playwright-start-maximized-window
    # Create a new incognito browser context.
    context = browser.new_context(no_viewport=True)
    # Create a new page in a pristine context. Create a page object which we could interact with
    page = context.new_page()
    # page.get_by_role
    
    homepage = HomePage(page)
    # Navigate to website we want to test. For demonstration purposes we are using The Perth Mint
    homepage.navigate('https://www.perthmint.com/')
    # REFERENCE https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id
    # Click on OK button in "Our site uses cookies prompt"
    # We are locating by CSS selector where element id = onetrust-accept-btn-handler
    # page.locator("#onetrust-accept-btn-handler").click()
    homepage.click_accept_cookies()
    
    main_navigation = MainNavigation(page)
    # We are locating by CSS selector where classes are as specified below
    # page.locator('.header__sub-nav-item.header__nav-item--search').click()
        # main_navigation.click_search_icon()
    
    # Item or product to search is hard coded now. Created a variable so it is easier to find what we are searching
    value_to_search = 'James Bond Skyfall'
    # Enter item or product to search in "What are you looking for?" text field.
    # page.locator('//*[@id="search-desktop"]/div/input').fill(value_to_search)
        # main_navigation.input_search(value_to_search='James Bond', wait_time=2000)
    
    # Explicitly click on the "Search" button on upper right hand side of page
    # page.locator('//*[@id="search-desktop"]/div/button[1]').click()
    # page.wait_for_timeout(5000)
        # main_navigation.click_search_bar_button(wait_time=5000)
    
    # product_card = ProductCard(page)
    # product_card.click_product_card_url(wait_time=5000)
    
    # Now that we are able to navigate to specific product detail page, let us click on "Add to cart" button
        # page.locator('//*[@id="mainContent"]/div[1]/div[2]/div/div/div[2]/div[6]/div[1]/span/button').click()
        # page.wait_for_timeout(5000)
    
    # Close the 'Quick cart' after adding an item to the cart
        # quick_cart = QuickCart(page)
        # quick_cart.close_quick_cart(wait_time=3000)
    # Open the 'Quick cart'
        # main_navigation.open_quick_cart(wait_time=3000)
    # Close the 'Quick cart'
        # quick_cart.close_quick_cart(wait_time=3000)
    # Open 'Country and currency settings'
        # main_navigation.open_country_currency_settings(wait_time=3000)
    
    # Close 'Country and currency settings'
        # country_currency_settings = CountryCurrencySettings(page)
        # country_currency_settings.close_country_and_currency_settings(wait_time=3000)
    # Open 'Login / Register' panel
        # main_navigation.open_login_register_panel(wait_time=5000)
    login_register_panel = LoginRegisterPanel(page)
    # Close 'Login / Register' panel
        # login_register_panel.close_login_register_panel(wait_time=3000)
    # Open 'Login / Register' panel again
        # main_navigation.open_login_register_panel(wait_time=3000)
    # Navigate to "Login" page
        # login_register_panel.navigate_to_account_login(wait_time=3000)
        # login_page = LoginPage(page)
    # Enter test account email address, password, click Login
        # login_page.input_email_address(email_address="jd@perthmint.com", wait_time=3000)
        # login_page.input_password(password="not_legit_password", wait_time=3000)
        # login_page.click_login(wait_time=3000)
    # At "Login" page, click on Perth Mint logo to navigate back to 'Home page'
        # login_page.navigate_to_homepage(wait_time=3000)
    # From "Home screen" click on "Login/Register" again
    main_navigation.open_login_register_panel(wait_time=3000)
    # On the "Login/Register" panel, click on "Register"
    login_register_panel.navigate_to_account_registration(wait_time=5000)
    registration_page = RegistrationPage(page)
    # Input Account details on 'Account registration'
    registration_page.input_first_name(first_name='Noah', wait_time=2000)
    registration_page.input_last_name(last_name='Pogi', wait_time=2000)
    registration_page.select_country_code(country_code='PH', wait_time=2000)
    registration_page.input_phone_number(phone_number='414222333', wait_time=3000)
    registration_page.input_email_address(email_address='jd@yahoo.com', wait_time=3000)
    # registration_page.agree_to_terms_and_conditions(wait_time=10000)
    # On the 'Account registration page', click on Perth Mint logo to navigate back to 'Home page'
    # registration_page.navigate_to_homepage(wait_time=3000)
    registration_page.navigate_to_homepage(wait_time=3000)
    main_navigation.open_collector_coins_menu(wait_time=3000)
    collector_coins_page = CollectorCoinsPage(page)
        # collector_coins_page.click_on_by_metal_gold(wait_time=3000)
    collector_coins_page.click_on_by_metal_silver(wait_time=3000)
    
    page.screenshot(path="playwright_sync_demo.png")
    browser.close()