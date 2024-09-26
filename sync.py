from playwright.sync_api import sync_playwright
# References
# https://playwright.dev/python/docs/api/class-playwright
# https://www.youtube.com/watch?v=H2-5ecFwHHQ
# https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A

# Use a context manager. 
# with sync_playwright() as playwright > This will close our browser 
# when our code is finished thus preventing possible memory issues.
with sync_playwright() as playwright:
    chromium = playwright.chromium
    # Create a browser object which we could work with. By default the browser will be running headless
    browser = chromium.launch(headless=False, slow_mo=50)
    # Create a page object which we could interact with
    page = browser.new_page()
    # Navigate to website
    page.goto('https://www.perthmint.com/')
    # REFERENCE https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id
    # Click on OK button in "Our site uses cookies prompt"
    page.locator("#onetrust-accept-btn-handler").click()
    page.screenshot(path="playwright_sync_demo.png")
    browser.close()