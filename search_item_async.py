import asyncio
from playwright.async_api import async_playwright, Playwright
from pages_async.home_page_async import HomePageAsync
from pages_async.main_navigation_async import MainNavigationAsync

# https://playwright.dev/python/docs/pom
async def run(playwright: Playwright):
    chromium = playwright.chromium
    # Create a browser object which we could work with. By default the browser will be running headless = True
    browser = await chromium.launch(headless=False, slow_mo=50, args=["--start-maximized"])
    # https://playwright.dev/python/docs/api/class-browser#browser-new-context
    # Playwright uses browser contexts to achieve Test Isolation. 
    # Each test has its own Browser Context. 
    # Running the test creates a new browser context each time. 
    # When using Playwright as a Test Runner, browser contexts are created by default. 
    # Otherwise, you can create browser contexts manually.
    context = await browser.new_context(no_viewport=True)
    page = await context.new_page()
    home_page_async = HomePageAsync(page)
    await home_page_async.navigate('https://www.perthmint.com/')
    main_navigation_async = MainNavigationAsync(page)
    await main_navigation_async.load_default_homepage(wait_time=15000)
    await main_navigation_async.click_search_icon(wait_time=5000)
    value_to_search = 'James Bond Skyfall'
    # Enter item or product to search
    await main_navigation_async.input_search(value_to_search, wait_time=5000)
    await page.screenshot(path="async_search_item_demo.png")
    
async def main():
    # Use async_playwright context manager to close the Playwright instance automatically
    async with async_playwright() as playwright:
        await run(playwright)
        
asyncio.run(main())