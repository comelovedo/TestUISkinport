import time
import pytest
from pages.skinport_market import MarketPage


def test_market_page(setup):
    """Test Checking If It Is Market Page, CS GO Market By Default"""
    page = MarketPage(setup)
    assert page.get_current_url() == 'https://skinport.com/market'


def test_search_field(setup):
    """Tests Search Field"""
    page = MarketPage(setup)
    assert page.search.is_visible()
    assert page.search.is_presented()
    assert page.search.is_clickable()


def test_search_field_input_correct_value(setup):
    """Tests Find Item By Name in Search Field"""
    page = MarketPage(setup)
    page.search.send_keys('butterfly knife')
    for title in page.items_titels.get_text():
        assert 'Butterfly Knife' in title


@pytest.mark.xfail(reason="Input wrong words in search field doesn't work")
def test_search_field_input_incorrect_value(setup):
    """Tests Find Item By Name With Wrong Keyboard in Search Field"""
    page = MarketPage(setup)
    page.search.send_keys('игееукадн лтшау')
    # The same as "butterfly knife" but
    # on different language keyboard
    for title in page.items_titels.get_text():
        assert 'Butterfly Knife' in title


def test_search_field_input_partial_correct_value(setup):
    """Tests Find Item By Part Of Name in Search Field"""
    page = MarketPage(setup)
    page.search.send_keys('butterfly')
    for title in page.items_titels.get_text():
        assert 'Butterfly Knife' in title


def test_check_header_menu_items(setup):
    """Tests Header Menu, CS GO Page"""
    page = MarketPage(setup)
    assert page.header_menu_items.is_presented()
    assert page.header_menu_items.is_visible()
    assert page.header_menu_items.is_clickable()


def test_check_elements_in_header_items_menu(setup):
    """Tests Header Menu Has All Elements, CS GO Page"""
    page = MarketPage(setup)
    assert page.elements_menu.count() == 15


def test_find_item_by_header_menu(setup):
    """Make sure that we can filter the items in catalog though the header menu"""
    page = MarketPage(setup)
    page.knifes.click()
    page.bayonet_knife.click()
    page.first_item.click()
    for title in page.items_titels.get_text():
        assert 'Bayonet' in title


def test_check_button_sort_by_best_value(setup):
    """ Tests Button Sorts By Best Value"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.best_value.is_visible()
    assert page.best_value.is_presented()
    assert page.best_value.is_clickable()


def test_check_button_sort_by_highest_discount(setup):
    """ Tests Button Sorts By Highest Discount"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.highest_discount.is_visible()
    assert page.highest_discount.is_presented()
    assert page.highest_discount.is_clickable()


def test_check_button_sort_by_cheapest_first(setup):
    """ Tests Button Sorts By Cheapest First"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.cheapest_first.is_visible()
    assert page.cheapest_first.is_presented()
    assert page.cheapest_first.is_clickable()


def test_check_button_sort_by_expensive_first(setup):
    """ Tests Button Sorts By Expensive First"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.expensive_first.is_visible()
    assert page.expensive_first.is_presented()
    assert page.expensive_first.is_clickable()


def test_check_button_sort_by_lowest_wear(setup):
    """ Tests Button Sorts By Lowest Wear"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.lowest_wear.is_visible()
    assert page.lowest_wear.is_presented()
    assert page.lowest_wear.is_clickable()


def test_check_button_sort_by_highest_wear(setup):
    """ Tests Button Sorts By Highest Wear"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.highest_wear.is_visible()
    assert page.highest_wear.is_presented()
    assert page.highest_wear.is_clickable()


def test_check_button_sort_by_oldest(setup):
    """ Tests Button Sorts By Oldest"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.oldest.is_visible()
    assert page.oldest.is_presented()
    assert page.oldest.is_clickable()


def test_check_button_sort_by_newest(setup):
    """ Tests Button Sorts By Newest"""
    page = MarketPage(setup)
    page.sort_by.click()
    assert page.newest.is_visible()
    assert page.newest.is_presented()
    assert page.newest.is_clickable()


def test_sort_items_in_catalog_by_highest_discount(setup):
    """ Tests Button Sorts By Highest Discount Work Correctly"""
    page = MarketPage(setup)
    page.sort_by.click()
    page.highest_discount.click()
    for title in page.items_discount.get_text():
        assert '- 60' or '− 50%' in title


def test_sort_items_in_catalog_by_cheapest_first(setup):
    """ Tests Button Sorts By Cheapest First Work Correctly"""
    page = MarketPage(setup)
    page.sort_by.click()
    page.cheapest_first.click()
    all_prices = page.items_price.get_text()
    # Convert all prices from strings to float
    all_prices = [float(p.split('\n')[0].replace('€', '').replace(',', '')) for p in all_prices]
    assert all_prices == sorted(all_prices)


def test_sort_items_in_catalog_by_expensive_first(setup):
    """ Tests Button Sorts By Expensive First Work Correctly"""
    page = MarketPage(setup)
    page.sort_by.click()
    page.expensive_first.click()
    all_prices = page.items_price.get_text()
    # Convert all prices from strings to float
    all_prices = [float(p.split('\n')[0].replace('€', '').replace(',', '')) for p in all_prices]
    assert all_prices == sorted(all_prices, reverse=True)


def test_button_row_view(setup):
    """Tests Row View Button"""
    page = MarketPage(setup)
    assert page.icon_row.is_visible()
    assert page.icon_row.is_presented()
    assert page.icon_row.is_clickable()


def test_button_card_view(setup):
    """Tests Card View Button"""
    page = MarketPage(setup)
    assert page.icon_card.is_visible()
    assert page.icon_card.is_presented()
    assert page.icon_card.is_clickable()


def test_check_row_catalog(setup):
    """ Tests Button List View Work Correctly"""
    page = MarketPage(setup)
    page.icon_row.click()
    assert page.catalog_items_list.is_presented()


def test_check_grid_catalog(setup):
    """ Tests Button Card View Work Correctly"""
    page = MarketPage(setup)
    page.icon_card.click()
    time.sleep(5)
    assert page.catalog_items_grid.is_presented()


def test_check_item_card(setup):
    """Tests Check if all cards consist: prices, names, titles, texts, images."""
    # Check if all cards consist: prices, names, titles, texts, images.
    page = MarketPage(setup)
    price = len(page.items_price.get_text())
    name = len(page.items_name.get_text())
    title = len(page.items_titels.get_text())
    text = len(page.items_text.get_text())
    image = len(page.items_image.get_text())
    assert max(price, name, title, text, image) == min(price, name, title, text, image)
