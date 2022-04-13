import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://skinport.com/'

        super().__init__(driver, url)

        # path = '/Users/bazucer/Desktop/IT/skinTesting/CookieChrome/cookie.json'
        # with open(path, 'rb') as cookiesfile:
        #     cookies = json.load(cookiesfile)
        # for cookie in cookies:
        #     print(cookie)
        #     driver.add_cookie(cookie)
        # driver.refresh()

    # logo on the main page in header navigation
    logo = WebElement(class_name='HeaderContainer-logoLink')

    cart = WebElement(css_selector='div[class="CartButton-icon"]')

    # Market button in header navigation
    market_button = WebElement(class_name='HeaderContainer-link')

    # Game Switcher Button in header navigation
    choose_game = WebElement(xpath="//div[@class='GameSwitcherButton-title']")
    csgo = WebElement(xpath='//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/button[1]/img[1]')
    dota_2 = WebElement(xpath='//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/button[2]/img[1]')
    rust = WebElement(xpath='//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/button[3]/img[1]')
    tf2 = WebElement(xpath='//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/button[4]/img[1]')

    # Main search field in header navigation
    search = WebElement(xpath='//*[@id="searchInput"]')

    # Button to the login form in header navigation
    login = WebElement(xpath='//a[@class="HeaderContainer-link HeaderContainer-link--login"]')
    # Email field
    login_steam = WebElement(css_selector="button[class='SocialAuthButtons-btn SocialAuthButtons-btn--steam']")
    email_input = WebElement(xpath="//div[@class='TextField-inputWrapper']/input[@id='email']")
    # Password field
    password_input = WebElement(xpath='//div[@class="TextField-inputWrapper"]/input[@id="password"]')
    # Submit login form
    submit_login = WebElement(xpath='//div[@class="Form-btns LoginForm-submit"]')

    # Button of registration form in header navigation
    registration = WebElement(class_name='SubmitButton.HeaderContainer-registerBtn')


    # Market CS GO
    market_CSGO = WebElement(css_selector='a[href="/market"]')
    # Market Team Fortress 2
    tf2_market = WebElement(css_selector='a[href="/tf2/market"]')
    # Market RUST
    rust_market = WebElement(css_selector='a[href="/rust/market"]')
    # Market Dota 2
    dota2_market = WebElement(css_selector='a[href="/dota2/market"]')

