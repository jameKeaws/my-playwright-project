from playwright.sync_api import sync_playwright
from pages.homepage import HomePage
from pages.main_navigation import MainNavigation
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
    # page = browser.new_page()
    
    homepage = HomePage(page)
    homepage.navigate('https://www.perthmint.com/')
    # Click on OK button in "Our site uses cookies prompt"
    homepage.click_accept_cookies()
    
    main_navigation = MainNavigation(page)
    main_navigation.load_default_homepage(wait_time=10000)
    # Open 'Login / Register' panel
    main_navigation.open_login_register_panel(wait_time=20000)
    login_register_panel = LoginRegisterPanel(page)
    # Navigate to "Login" page
    login_register_panel.navigate_to_account_login(wait_time=3000)
    login_page = LoginPage(page)
    # Enter test account email address, password, click Login
    login_page.input_email_address(email_address="jd@perthmint.com", wait_time=3000)
    login_page.input_password(password="not_legit_password", wait_time=3000)
    login_page.click_login(wait_time=3000)
    # At "Login" page, click on Perth Mint logo to navigate back to 'Home page'
    login_page.navigate_to_homepage(wait_time=3000)
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
    # gracefully close up everything
    context.close()
    browser.close()