import os

import pytest
from selene import browser, command, have


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
    browser.element('[placeholder="name@example.com"]').type('Test@gmail.com')
    browser.element('[name=gender][value=Male]').perform(command.js.click)
    browser.element('[placeholder="Mobile Number"]').type('8005553535')
    browser.element('[id="dateOfBirthInput"]').perform(command.js.click)
    browser.element('[class="react-datepicker__month-select"]').send_keys('June')
    browser.element('[class="react-datepicker__year-select"]').send_keys('1995')
    browser.element('[aria-label="Choose Tuesday, June 13th, 1995"]').perform(command.js.click)
    browser.element('[id="subjectsInput"]').type('Ma').press_tab()
    browser.element('[id="hobbies-checkbox-1"]').perform(command.js.click)
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('mem.jpg'))
    browser.element('[id="currentAddress"]').type('Russia, Moscow')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('[id="submit"]').perform(command.js.click)

    #check

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Пользователь Тестовый'))
    browser.element('.modal-body').should(have.text('Test@gmail.com'))
    browser.element('.modal-body').should(have.text('Male'))
    browser.element('.modal-body').should(have.text('8005553535'))
    browser.element('.modal-body').should(have.text('13 June,1995'))
    browser.element('.modal-body').should(have.text('Maths'))
    browser.element('.modal-body').should(have.text('Sports'))
    browser.element('.modal-body').should(have.text('Russia, Moscow'))
    browser.element('.modal-body').should(have.text('Uttar Pradesh Agra'))

