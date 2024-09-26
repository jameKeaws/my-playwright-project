import asyncio
from playwright.async_api import async_playwright, Playwright
# References
# https://playwright.dev/python/docs/api/class-playwright
# https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A

async def main():
    print('async.py main()')
    async with async_playwright() as playwright:
        chromium = playwright.firefox
        browser = await chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.perthmint.com/')
        # Other actions here
        # page.screenshot(path="playwright_async_demo.png")
        print(await page.title())
        await browser.close()

asyncio.run(main())

