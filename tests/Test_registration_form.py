import os
from selene import browser, command, have


def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Пользователь')
    browser.element('#lastName').type('Тестовый')
    browser.element('#userEmail').type('Test@gmail.com')
    browser.all('[for^=gender-radio-1]').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('8005553535')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('June')
    browser.element('.react-datepicker__year-select').send_keys('1995')
    browser.element('[aria-label="Choose Tuesday, June 13th, 1995"]').perform(command.js.click)
    browser.element('#subjectsInput').type('Ma').press_tab()
    browser.all('[for^=hobbies-checkbox-1]').element_by(have.exact_text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/mem.jpg'))
    browser.element('#currentAddress').type('Russia, Moscow')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    browser.driver.execute_script("document.body.style.zoom='75%'")

    browser.element('#submit').perform(command.js.click)


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
