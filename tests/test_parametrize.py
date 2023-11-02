"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import have
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(params=[(2560, 1440), (390, 844)], ids=['desktop', 'mobile'])
def browser_setup(request):
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield
    browser.quit()


@pytest.mark.parametrize('browser_setup', [pytest.param((2560, 1440), id='desktop')], indirect=True)
def test_github_desktop(browser_setup):
    browser.open('/')
    browser.element('[class*=--sign-in]').click()
    browser.element('.auth-form-header h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_setup', [pytest.param((390, 844), id='mobile')], indirect=True)
def test_github_mobile(browser_setup):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('[class*=--sign-in]').click()
    browser.element('.auth-form-header h1').should(have.exact_text('Sign in to GitHub'))
