import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class FooterPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://skinport.com/'

        super().__init__(driver, url)

    market_button = WebElement(class_name='HeaderContainer-link')

    # Languages
    languages = WebElement(xpath='//button[@class="Dropdown-button"]')
    eng_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"]')
    duetsch_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][1]')
    turk_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][3]')
    franc_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][4]')
    span_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][5]')
    suomi_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][6]')
    polsk_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][7]')
    neder_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][8]')
    chin_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][9]')
    port_lng = WebElement(xpath='//div[@class="Dropdown-dropDownItem"][10]')

    # Service Pages Links
    about_us = WebElement(xpath="//a[@class='ServicePagesLinks-link'][1]")
    partnership = WebElement(css_selector='a[href="/affiliate"]')
    blog = WebElement(css_selector="a[href='https://blog.skinport.com']")
    screenshot_tools = WebElement(css_selector="a[href='https://screenshot.skinport.com']")
    data_base = WebElement(css_selector="a[href='https://float.skinport.com']")
    api = WebElement(css_selector="a[href='https://docs.skinport.com']")

    faq = WebElement(css_selector="a[href='/faq']")
    support = WebElement(css_selector="a[href='/support']")
    career = WebElement(css_selector="a[href='/jobs']")
    privacy = WebElement(css_selector="a[href='/privacy']")
    contacts = WebElement(css_selector="a[href='/imprint']")
    application = WebElement(css_selector='a[href="/tos"]')

    # Footer Social Links
    discord = WebElement(css_selector='a[href="https://discord.gg/skinport"]')
    instagram = WebElement(css_selector='a[href="https://www.instagram.com/skinport"]')
    twitter = WebElement(css_selector='a[href="https://twitter.com/skinport"]')
    tiktok = WebElement(css_selector='a[href="https://www.tiktok.com/@skinport"]')
    youtube = WebElement(css_selector='a[href="https://www.youtube.com/skinport"]')
    facebook = WebElement(css_selector='a[href="https://www.facebook.com/skinport"]')
    steam = WebElement(css_selector='a[href="https://steamcommunity.com/groups/skinport"]')
