from playwright.sync_api import sync_playwright
from pages.homepage import HomePage
from pages.main_navigation import MainNavigation
from pages.product_card import ProductCard
from pages.product_details_page import ProductDetailsPage
from pages.quick_cart import QuickCart

with sync_playwright() as playwright:
    chromium = playwright.chromium
    # Create a browser object which we could work with. By default the browser will be running headless = True
    browser = chromium.launch(headless=False, slow_mo=50, args=["--start-maximized"])
    # Create a new page in a pristine context. Create a page object which we could interact with
    # page = browser.new_page()
    # https://playwright.dev/python/docs/api/class-browser#browser-new-context
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    homepage = HomePage(page)
    # Navigate to website we want to test. For demonstration purposes we are using The Perth Mint
    homepage.navigate('https://www.perthmint.com/')
    # homepage.click_accept_cookies()
    
    main_navigation = MainNavigation(page)
    main_navigation.load_default_homepage(wait_time=15000)
    main_navigation.click_search_icon(wait_time=5000)
    value_to_search = 'James Bond Skyfall'
    # Enter item or product to search
    main_navigation.input_search(value_to_search, wait_time=5000)
    # Explicitly click on the "Search" button on upper right hand side of page
    main_navigation.click_search_bar_button(wait_time=5000)
    
    product_card = ProductCard(page)
    product_card.click_product_card_url(wait_time=5000)
    
    product_details_page = ProductDetailsPage(page)
    product_details_page.click_add_to_cart(wait_time=5000)
    page.screenshot(path="playwright_search_item_sync_demo.png")
    
    # Close the 'Quick cart' after adding an item to the cart
    quick_cart = QuickCart(page)
    quick_cart.close_quick_cart(wait_time=3000)
    product_details_page.use_plus_button(how_much_more_to_add=5, wait_time=5000)
    quick_cart.close_quick_cart(wait_time=3000)
    product_details_page.use_minus_button(how_much_to_subtract=4, wait_time=5000)
    
    # gracefully close up everything
    context.close()
    browser.close()