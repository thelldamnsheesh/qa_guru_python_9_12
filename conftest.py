import pytest
from selene import browser

@pytest.fixture
def browser_options():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.set_window_size(height=2560, width=1440)
    # изменил масштаб, тк кнопка при 100% масштабе не видна
    browser.driver.execute_script("document.body.style.zoom='65%'")

    yield
    browser.quit()