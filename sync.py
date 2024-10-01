from playwright.sync_api import sync_playwright
from pages.homepage import HomePage
from pages.main_navigation import MainNavigation
# References
# https://playwright.dev/python/docs/api/class-playwright
# https://www.youtube.com/watch?v=H2-5ecFwHHQ
# https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A
# https://playwright.dev/docs/locators
# https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id
# https://stackoverflow.com/questions/75144059/python-playwright-start-maximized-window
# https://devhints.io/xpath#class-check
# https://www.roborabbit.com/blog/xpath-cheat-sheet-a-quick-reference-to-essential-xpath-expressions/#using-operators-to-combine-expressions
# https://stackoverflow.com/questions/22571267/how-to-verify-an-xpath-expression-in-chrome-developers-tool-or-firefoxs-firebug
# https://playwright.dev/python/docs/pom

# Use a context manager. 
# with sync_playwright() as playwright > This will close our browser when our code is finished running 
# thus preventing possible memory issues from any unclosed browsers used.
with sync_playwright() as playwright:
    chromium = playwright.chromium
    # Create a browser object which we could work with. By default the browser will be running headless = True
    browser = chromium.launch(headless=False, slow_mo=50, args=["--start-maximized"])
    # REFERENCE https://stackoverflow.com/questions/75144059/python-playwright-start-maximized-window
    # Create a new incognito browser context.
    context = browser.new_context(no_viewport=True)
    # Create a new page in a pristine context. Create a page object which we could interact with
    page = context.new_page()
    # TODO Start using Page object model for HomePage
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
    main_navigation.click_search_icon()
    
    # Item or product to search is hard coded now. Created a variable so it is easier to find what we are searching
    value_to_search = 'James Bond Skyfall'
    # Enter item or product to search in "What are you looking for?" text field.
    # page.locator('//*[@id="search-desktop"]/div/input').fill(value_to_search)
    # page.wait_for_timeout(2000)
    main_navigation.input_search(value_to_search='James Bond Skyfall', wait_time=2000)
    
    # Explicitly click on the "Search" button on upper right hand side of page
    # page.locator('//*[@id="search-desktop"]/div/button[1]').click()
    # page.wait_for_timeout(5000)
    main_navigation.click_search_bar_button(wait_time=5000)
    
    # TODO This kind of XPath locator will likely break later.  We need to improve it for easier maintenance
    page.locator('//*[@id="panel-Products"]/div[2]/div[1]/div/div[2]/div[1]/h3/a').click()
    page.wait_for_timeout(5000)
    # Now that we are able to navigate to specific product detail page, let us click on "Add to cart" button
    page.locator('//*[@id="mainContent"]/div[1]/div[2]/div/div/div[2]/div[6]/div[1]/span/button').click()
    page.wait_for_timeout(10000)
    page.screenshot(path="playwright_sync_demo.png")
    browser.close()