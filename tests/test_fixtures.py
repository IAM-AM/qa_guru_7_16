import pytest
from selene import have
from selenium import webdriver
from selene.support.shared import browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture
def browser_desktop():
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options
    browser.config.window_width = 2560
    browser.config.window_height = 1440
    browser.config.base_url = 'https://github.com/'

    yield
    browser.quit()


def test_github_desktop(browser_desktop):
    browser.open('/')
    browser.element('[class*=--sign-in]').click()
    browser.element('.auth-form-header h1').should(have.exact_text('Sign in to GitHub'))


@pytest.fixture()
def browser_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844
    browser.config.base_url = 'https://github.com/'

    yield
    browser.quit()


def test_github_mobile(browser_mobile):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('[class*=--sign-in]').click()
    browser.element('.auth-form-header h1').should(have.exact_text('Sign in to GitHub'))
