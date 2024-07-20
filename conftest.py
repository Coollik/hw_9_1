import pytest
from selene import browser, be

@pytest.fixture
def browser_config():
    browser.config.window_width = 430
    browser.config.window_height = 935
    browser.config.driver_name = 'firefox'
    yield
    browser.quit()
@pytest.fixture()
def browser_open(browser_config):
    browser.open('https://google.com')

@pytest.fixture()
def type_text():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()