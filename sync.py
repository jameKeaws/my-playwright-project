from playwright.sync_api import sync_playwright
# References
# https://playwright.dev/python/docs/api/class-playwright
# https://www.youtube.com/watch?v=H2-5ecFwHHQ
# https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A
# IMPORTANT REFERENCE FOR LOCATORS https://playwright.dev/docs/locators

# Use a context manager. 
# with sync_playwright() as playwright > This will close our browser when our code is finished running 
# thus preventing possible memory issues from any unclosed browsers used.
with sync_playwright() as playwright:
    chromium = playwright.chromium
    # Create a browser object which we could work with. By default the browser will be running headless = True
    browser = chromium.launch(headless=False, slow_mo=50)
    # Create a page object which we could interact with
    page = browser.new_page()
    # Navigate to website we want to test. For demonstration purposes we are using The Perth Mint
    page.goto('https://www.perthmint.com/')
    # REFERENCE https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id
    # Click on OK button in "Our site uses cookies prompt"
    # We are locating by CSS selector where element id = onetrust-accept-btn-handler
    page.locator("#onetrust-accept-btn-handler").click()
    page.wait_for_timeout(2000)
    # page.get_by_role("button").and_()
    # We are locating by CSS selector where classes are as specified below
    page.locator('.header__sub-nav-item.header__nav-item--search').click()
    # Item or product to search is hard code now
    value_to_search = 'James Bond Skyfall'
    # Enter item or product to search in "What are you looking for?" text field
    
    page.locator('//*[@id="search-desktop"]/div/input').fill(value_to_search)
    page.wait_for_timeout(2000)
    
    page.screenshot(path="playwright_sync_demo.png")
    browser.close()