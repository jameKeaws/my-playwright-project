import re
# We import the Page fixture provided by Playwright that maintains test isolation 
# and takes care of setup and teardown
from playwright.sync_api import Page, expect
from pages.homepage import HomePage

# We will run this in headed mode pytest -k home --headed
def test_navigate(page : Page):
    homepage = HomePage(page)
    homepage.navigate('https://www.perthmint.com/')
    expect(page).to_have_title(re.compile("The Perth Mint | Buy gold, silver coins and bullion"))