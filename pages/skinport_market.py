import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MarketPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://skinport.com/market'

        super().__init__(driver, url)

    '''Main search field in header navigation'''
    search = WebElement(xpath='//*[@id="searchInput"]')

    """Header Menu-items, CS GO Page"""
    header_menu_items = WebElement(class_name="HeaderMenu-items")
    elements_menu = ManyWebElements(xpath='//div[@class="HeaderMenu-item"]')
    first_item = WebElement(css_selector='div[class="ProductFinder-item"]')
    # Knife
    knifes = WebElement(xpath="//div[@class='HeaderMenu-item'][1]")
    bayonet_knife = WebElement(xpath='//div[@class="HeaderMenu-item"][1]/button')
    Bowie_knife = WebElement(xpath='//div[@class="HeaderMenu-item"][2]/button')
    butterfly_knife = WebElement(xpath='//div[@class="HeaderMenu-item"][3]/button')
    classic_knife = WebElement(xpath='//div[@class="HeaderMenu-item"][4]/button')
    falchion = WebElement(xpath='//div[@class="HeaderMenu-item"][5]/button')
    folding_knife = WebElement(xpath='//div[@class="HeaderMenu-item"][6]/button')
    hook_blade_knife = WebElement(xpath='//div[@class="HeaderMenu-item"][7]/button')
    hunting_knife = WebElement(xpath='//div[@class="HeaderMenu-item"][8]/button')

    # Pistol
    pistol = WebElement(xpath="//div[@class='HeaderMenu-item'][2]")
    cz75_auto = WebElement(xpath='//div[@class="HeaderMenu-item"][1]/button')
    desert_eagle = WebElement(xpath='//div[@class="HeaderMenu-item"][2]/button')
    dual_berettas = WebElement(xpath='//div[@class="HeaderMenu-item"][3]/button')
    five_seven = WebElement(xpath='//div[@class="HeaderMenu-item"][4]/button')
    glock_18 = WebElement(xpath='//div[@class="HeaderMenu-item"][5]/button')
    p2000 = WebElement(xpath='//div[@class="HeaderMenu-item"][6]/button')
    p250 = WebElement(xpath='//div[@class="HeaderMenu-item"][7]/button')
    r8 = WebElement(xpath='//div[@class="HeaderMenu-item"][8]/button')
    tec_9 = WebElement(xpath='//div[@class="HeaderMenu-item"][9]/button')
    usp_s = WebElement(xpath='//div[@class="HeaderMenu-item"][10]/button')
    ssg_8 = WebElement(xpath='//div[@class="HeaderMenu-item"][11]/button')

    # Rifle
    rifles = WebElement(xpath="//div[@class='HeaderMenu-item'][3]")
    ak_47 = WebElement(xpath='//div[@class="HeaderMenu-item"][1]/button')
    aug = WebElement(xpath='//div[@class="HeaderMenu-item"][2]/button')
    famas = WebElement(xpath='//div[@class="HeaderMenu-item"][3]/button')
    galil = WebElement(xpath='//div[@class="HeaderMenu-item"][4]/button')
    m4a1 = WebElement(xpath='//div[@class="HeaderMenu-item"][5]/button')
    m4a4 = WebElement(xpath='//div[@class="HeaderMenu-item"][6]/button')
    sg553 = WebElement(xpath='//div[@class="HeaderMenu-item"][7]/button')
    awp = WebElement(xpath='//div[@class="HeaderMenu-item"][8]/button')
    g3sg1 = WebElement(xpath='//div[@class="HeaderMenu-item"][9]/button')
    skar_20 = WebElement(xpath='//div[@class="HeaderMenu-item"][10]/button')
    # Machine gun
    machine_gun = WebElement(xpath="//div[@class='HeaderMenu-item'][4]")
    mac_10 = WebElement(xpath='//div[@class="HeaderMenu-item"][1]/button')
    mp5_sd = WebElement(xpath='//div[@class="HeaderMenu-item"][2]/button')
    mp7 = WebElement(xpath='//div[@class="HeaderMenu-item"][3]/button')
    mp9 = WebElement(xpath='//div[@class="HeaderMenu-item"][4]/button')
    p90 = WebElement(xpath='//div[@class="HeaderMenu-item"][5]/button')
    pp19_bizon = WebElement(xpath='//div[@class="HeaderMenu-item"][6]/button')
    ump45 = WebElement(xpath='//div[@class="HeaderMenu-item"][7]/button')
    # Heavy weapons
    heavy_weapons = WebElement(xpath="//div[@class='HeaderMenu-item'][5]")
    mag_7 = WebElement(xpath='/div[@class="HeaderMenu-item"][1]/button')
    nova = WebElement(xpath='/div[@class="HeaderMenu-item"][2]/button')
    sawed_off = WebElement(xpath='/div[@class="HeaderMenu-item"][3]/button')
    xm1014 = WebElement(xpath='/div[@class="HeaderMenu-item"][4]/button')
    m249 = WebElement(xpath='/div[@class="HeaderMenu-item"][5]/button')
    negev = WebElement(xpath='/div[@class="HeaderMenu-item"][6]/button')

    # Gloves
    gloves = WebElement(xpath="//div[@class='HeaderMenu-item'][6]")
    # Keys
    Keys = WebElement(xpath="//div[@class='HeaderMenu-item'][7]")
    # Container
    container = WebElement(xpath="//div[@class='HeaderMenu-item'][8]")
    # Agent
    agent = WebElement(xpath="//div[@class='HeaderMenu-item'][9]")

    """Header Menu-filter"""
    filter_button = WebElement(css_selector="span[class='FilterButton-text']")
    cost_section = WebElement(css_selector='div[class="FilterWrapper-title"]')
    cost_input_from = WebElement(id='pricegt')
    cost_input_to = WebElement(id='pricelt')

    """Dropdown sort by"""
    # The most popular by default
    sort_by = WebElement(css_selector='button[class="Dropdown-button"]')
    best_value = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][1]')
    highest_discount = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][2]')
    cheapest_first = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][3]')
    expensive_first = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][4]')
    lowest_wear = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][5]')
    highest_wear = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][6]')
    oldest = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][7]')
    newest = WebElement(xpath='//div[@class="Dropdown-dropDownItem CatalogHeader-dropdown"][8]')

    """View of market's cards"""
    icon_row = WebElement(class_name="icon-row")
    icon_card = WebElement(class_name='icon-card')

    """Cards of items"""

    catalog_items_grid = ManyWebElements(css_selector="div[class='CatalogPage-items CatalogPage-items--grid']")
    catalog_items_list = ManyWebElements(css_selector="div[class='CatalogPage-items CatalogPage-items--list']")
    first_card = WebElement(xpath='//div[@class="CatalogPage-item CatalogPage-item--grid"][1]')
    card = WebElement(css_selector='div[class="ItemPreview-commonInfo"]')
    second_card = WebElement(css_selector="div[class='CatalogPage-items CatalogPage-items--grid'][2]")

    """Card of item"""
    items_name = ManyWebElements(css_selector='div[class="ItemPreview-itemName"]')
    items_text = ManyWebElements(css_selector='div[class="ItemPreview-itemText"]')
    items_image = ManyWebElements(css_selector='div[class="ItemPreview-itemImage"]')
    items_titels = ManyWebElements(xpath='//div[@class="ItemPreview-itemTitle"]')
    items_price = ManyWebElements(css_selector='div[class="ItemPreview-priceValue"]')
    items_discount = ManyWebElements(class_name='GradientLabel.ItemPreview-discount')
    items_old_price = ManyWebElements(css_selector='div[class="ItemPreview-oldPrice"]')

    """Actions Bar of item"""
    card_menu = WebElement(css_selector='button[class="ItemPreview-sideAction"]')
    add_in_cart = WebElement(css_selector='button[class="ItemPreview-mainAction"]')
    item_on_screen = WebElement(xpath='//a[@class="ActionLink"][1]')
    check_in_steam = WebElement(xpath='//a[@class="ActionLink"][2]')
    search_the_item = WebElement(xpath='//a[@class="ActionLink"][3]')
    subscribe_on_item = WebElement(xpath='//button[@class="ActionLink"]')
