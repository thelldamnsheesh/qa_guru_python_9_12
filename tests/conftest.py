import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_options():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1440
    browser.config.window_height = 1860

    yield
    browser.quit()