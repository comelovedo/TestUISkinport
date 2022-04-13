from pages.skinport_footer import FooterPage


# Tests Languages
def test_language_button(setup):
    """Test button change language, if it located on page"""
    page = FooterPage(setup)
    assert page.languages.is_presented()
    assert page.languages.is_visible()
    assert page.languages.is_clickable()


def test_change_language_on_german(setup):
    """Test Change language from English to German"""
    page = FooterPage(setup)
    page.languages.click()
    page.duetsch_lng.click()
    page.refresh()
    assert page.market_button.get_text() == 'MARKT'


def test_change_language_on_turkish(setup):
    """Test Change language from English to Turkish"""
    page = FooterPage(setup)
    page.languages.click()
    page.turk_lng.click()
    page.refresh()
    assert page.market_button.get_text() == 'PAZAR'


def test_change_language_on_chinese(setup):
    """Test Change language from English to Chinese"""
    page = FooterPage(setup)
    page.languages.click()
    page.chin_lng.click()
    page.refresh()
    assert page.market_button.get_text() == '市场'


def test_change_language_on_french(setup):
    """Test Change language from English to French"""
    page = FooterPage(setup)
    page.languages.click()
    page.franc_lng.click()
    page.refresh()
    assert page.market_button.get_text() == 'MARCHÉ'


def test_change_language_on_spanish(setup):
    """Test Change language from English to Spanish"""
    page = FooterPage(setup)
    page.languages.click()
    page.span_lng.click()
    page.refresh()
    assert page.market_button.get_text() == 'MERCADO'


def test_change_language_on_finnish(setup):
    """Test Change language from English to Finnish"""
    page = FooterPage(setup)
    page.languages.click()
    page.suomi_lng.click()
    page.refresh()
    assert page.market_button.get_text() == 'KAUPPAPAIKKA'


def test_change_language_on_polish(setup):
    """Test Change language from English to Polish"""
    page = FooterPage(setup)
    page.languages.click()
    page.polsk_lng.click()
    page.refresh()
    assert page.market_button.get_text() == 'RYNEK'


# Tests Service Pages Links
def test_check_button_about_us(setup):
    """Test Checking Button About Us After Click"""
    page = FooterPage(setup)
    page.about_us.click()
    assert page.get_current_url() == 'https://skinport.com/about'


def test_button_about_us(setup):
    """Test Checking Button About Us"""
    page = FooterPage(setup)
    assert page.about_us.is_visible()
    assert page.about_us.is_presented()


def test_check_button_affiliate(setup):
    """Test Checking Button Affiliate After Click"""
    page = FooterPage(setup)
    page.partnership.click()
    assert page.get_current_url() == 'https://skinport.com/affiliate'


def test_button_affiliate(setup):
    """Test Checking Button Affiliate"""
    page = FooterPage(setup)
    assert page.partnership.is_visible()
    assert page.partnership.is_presented()
    assert page.partnership.is_clickable()


def test_button_blog(setup):
    """Test Checking Button Blog"""
    page = FooterPage(setup)
    assert page.blog.is_visible()
    assert page.blog.is_presented()
    assert page.blog.is_clickable()


def test_button_screenshot(setup):
    """Test Checking Button Screenshot"""
    page = FooterPage(setup)
    assert page.screenshot_tools.is_visible()
    assert page.screenshot_tools.is_presented()
    assert page.screenshot_tools.is_clickable()


def test_button_database(setup):
    """Test Checking Button Database"""
    page = FooterPage(setup)
    assert page.data_base.is_visible()
    assert page.data_base.is_presented()
    assert page.data_base.is_clickable()


def test_button_api(setup):
    """Test Checking Button API"""
    page = FooterPage(setup)
    assert page.api.is_visible()
    assert page.api.is_presented()
    assert page.api.is_clickable()


def test_button_faq(setup):
    """Test Checking Button FAQ"""
    page = FooterPage(setup)
    assert page.faq.is_visible()
    assert page.faq.is_presented()


def test_check_button_faq(setup):
    """Test Checking Button FAQ After Click"""
    page = FooterPage(setup)
    page.faq.click()
    assert page.get_current_url() == 'https://skinport.com/faq'


def test_button_support(setup):
    """Test Checking Button Support"""
    page = FooterPage(setup)
    assert page.support.is_visible()
    assert page.support.is_presented()


def test_check_button_support(setup):
    """Test Checking Button Support After Click"""
    page = FooterPage(setup)
    page.support.click()
    assert page.get_current_url() == 'https://skinport.com/support'


def test_button_jobs(setup):
    """Test Checking Button Jobs"""
    page = FooterPage(setup)
    assert page.career.is_visible()
    assert page.career.is_presented()


def test_check_button_jobs(setup):
    """Test Checking Button Jobs After Click"""
    page = FooterPage(setup)
    page.career.click()
    assert page.get_current_url() == 'https://skinport.com/jobs'


def test_button_privacy(setup):
    """Test Checking Button Privacy"""
    page = FooterPage(setup)
    assert page.privacy.is_visible()
    assert page.privacy.is_presented()


def test_check_button_privacy(setup):
    """Test Checking Button Privacy After Click"""
    page = FooterPage(setup)
    page.privacy.click()
    assert page.get_current_url() == 'https://skinport.com/privacy'


def test_button_imprint(setup):
    """Test Checking Button Imprint"""
    page = FooterPage(setup)
    assert page.contacts.is_visible()
    assert page.contacts.is_presented()


def test_check_button_imprint(setup):
    """Test Checking Button Imprint After Click"""
    page = FooterPage(setup)
    page.contacts.click()
    assert page.get_current_url() == 'https://skinport.com/imprint'


def test_button_terms_of_service(setup):
    """Test Checking Button Terms Of Service"""
    page = FooterPage(setup)
    assert page.application.is_visible()
    assert page.application.is_presented()


def test_check_button_terms_of_service(setup):
    """Test Checking Button Terms Of Service After Click"""
    page = FooterPage(setup)
    page.application.click()
    assert page.get_current_url() == 'https://skinport.com/tos'


# Tests Footer Social Links
def test_button_discord(setup):
    """Test Checking Button Discord"""
    page = FooterPage(setup)
    assert page.discord.is_visible()
    assert page.discord.is_presented()
    assert page.discord.is_clickable()


def test_button_instagram(setup):
    """Test Checking Button Instagram"""
    page = FooterPage(setup)
    assert page.instagram.is_visible()
    assert page.instagram.is_presented()
    assert page.instagram.is_clickable()


def test_button_twitter(setup):
    """Test Checking Button Twitter"""
    page = FooterPage(setup)
    assert page.twitter.is_visible()
    assert page.twitter.is_presented()
    assert page.twitter.is_clickable()


def test_button_tiktok(setup):
    """Test Checking Button TikTok"""
    page = FooterPage(setup)
    assert page.tiktok.is_visible()
    assert page.tiktok.is_presented()
    assert page.tiktok.is_clickable()


def test_button_youtube(setup):
    """Test Checking Button YouTube"""
    page = FooterPage(setup)
    assert page.youtube.is_visible()
    assert page.youtube.is_presented()
    assert page.youtube.is_clickable()


def test_button_facebook(setup):
    """Test Checking Button FaceBook"""
    page = FooterPage(setup)
    assert page.facebook.is_visible()
    assert page.facebook.is_presented()
    assert page.facebook.is_clickable()


def test_button_steam(setup):
    """Test Checking Button Steam"""
    page = FooterPage(setup)
    assert page.steam.is_visible()
    assert page.steam.is_presented()
    assert page.steam.is_clickable()
