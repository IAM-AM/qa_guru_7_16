import pytest
from selene import have
from selene.support.shared import browser
from selenium import webdriver

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


@pytest.fixture(params=[(1440, 2560), (844, 390)], ids=['desktop', 'mobile'])
def browser_setup(request):
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    browser.config.base_url = 'https://github.com'

    yield request.param
    browser.quit()


def test_github_desktop(browser_setup):
    if browser_setup[0] > browser_setup[1]:
        pytest.skip('Desktop resolution')
    browser.open('/')
    browser.element('[class*=--sign-in]').click()
    browser.element('.auth-form-header h1').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_setup):
    if browser_setup[0] <= browser_setup[1]:
        pytest.skip('Mobile resolution')
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('[class*=--sign-in]').click()
    browser.element('.auth-form-header h1').should(have.exact_text('Sign in to GitHub'))