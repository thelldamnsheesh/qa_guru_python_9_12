import pytest
from selene import browser, by, command

@pytest.fixture
def browser_options():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.set_window_size(height=2560, width=1440)
    # изменил масштаб, тк кнопка при 100% масштабе не видна
    browser.driver.execute_script("document.body.style.zoom='65%'")

    yield
    browser.quit()

def test_registration_form(browser_options):
    browser.element('[placeholder="First Name"]').type('Пользователь')
    browser.element('[placeholder="Last Name"]').type('Тестовый')
    browser.element('[placeholder="name@example.com"]').type('Test@gmail.ru')
    browser.element('[name=gender][value=Male]').perform(command.js.click)
    browser.element('[placeholder="Mobile Number"]').type('8005553535')
    #browser.element('[id="dateOfBirthInput"]').click().element('[class="react-datepicker__month-select"]').click().element('[value="5"]').click().element('[class="react-datepicker__year-select"]').click().element('[value="1995"]').click().element('[aria-label="Choose Tuesday, June 13th, 1995"]').click()
    browser.element('[class="btn-primary"]').perform(command.js.click)