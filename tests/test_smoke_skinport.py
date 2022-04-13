import pytest
from pages.skinport_main import MainPage
from conftest import valid_mail, valid_password


def test_logo_button(setup):
    """Test Check Button Logo"""
    page = MainPage(setup)
    assert page.logo.is_clickable()
    assert page.logo.is_presented()
    assert page.logo.is_visible()


def test_main_page(setup):
    """Test Checking If It Is Main Page"""
    page = MainPage(setup)
    assert page.get_current_url() == 'https://skinport.com/'


def test_button_sign_in(setup):
    """Test Check Sign In Button"""
    page = MainPage(setup)
    assert page.login.is_presented()
    assert page.login.is_visible()


def test_button_sign_up(setup):
    """Test Check Sign Un Button"""
    page = MainPage(setup)
    assert page.registration.is_presented()
    assert page.registration.is_visible()


@pytest.mark.xfail(reason="There is protection against bots, sign in doesn't work")
def test_sign_in(setup):
    """Tests Authorization """
    page = MainPage(setup)
    page.login.click()
    page.email_input = valid_mail
    page.password_input = valid_password
    page.submit_login.click()
    # After sign-in we have access to the cart
    assert page.cart.is_presented()


def test_button_choose_game(setup):
    """Tests Change Game In Header Menu"""
    page = MainPage(setup)
    assert page.choose_game.is_presented()
    assert page.choose_game.is_visible()


def test_change_game_on_dota2(setup):
    """Tests Change Game From CS GO to Dota2"""
    page = MainPage(setup)
    page.choose_game.click()
    page.dota_2.click()
    assert page.get_current_url() == 'https://skinport.com/dota2'


def test_change_game_on_rust(setup):
    """Tests Change Game From CS GO to Rust"""
    page = MainPage(setup)
    page.choose_game.click()
    page.rust.click()
    assert page.get_current_url() == 'https://skinport.com/rust'


def test_change_game_on_team_fortress2(setup):
    """Tests Change Game From CS GO to TF2"""
    page = MainPage(setup)
    page.choose_game.click()
    page.tf2.click()
    assert page.get_current_url() == 'https://skinport.com/tf2'


def test_button_csgo_market(setup):
    """Tests Button Market CS GO On Main Page"""
    page = MainPage(setup)
    assert page.market_CSGO.is_presented()
    assert page.market_CSGO.is_visible()


def test_check_button_csgo_market(setup):
    """Tests Checking Button CS GO Market On Main Page"""
    page = MainPage(setup)
    page.market_CSGO.click()
    assert page.get_current_url() == 'https://skinport.com/market'


def test_button_tf2_market(setup):
    """Tests Button Market Team Fortress 2 On Main Page"""
    page = MainPage(setup)
    assert page.tf2_market.is_presented()
    assert page.tf2_market.is_visible()


def test_check_button_tf2_market(setup):
    """Tests Checking Button TF2 Market On Main Page"""
    page = MainPage(setup)
    page.tf2_market.click()
    assert page.get_current_url() == 'https://skinport.com/tf2/market'


def test_button_rust_market(setup):
    """Tests Button Market RUST On Main Page"""
    page = MainPage(setup)
    assert page.rust_market.is_presented()
    assert page.rust_market.is_visible()


def test_check_button_rust_market(setup):
    """Tests Checking RUST Market On Main Page"""
    page = MainPage(setup)
    page.rust_market.click()
    assert page.get_current_url() == 'https://skinport.com/rust/market'


def test_button_dota2_market(setup):
    """Tests Button Market DOTA2 On Main Page"""
    page = MainPage(setup)
    assert page.dota2_market.is_presented()
    assert page.dota2_market.is_visible()


def test_check_button_dota2_market(setup):
    """Tests Checking DOTA2 Market On Main Page"""
    page = MainPage(setup)
    page.dota2_market.click()
    assert page.get_current_url() == 'https://skinport.com/dota2/market'
