import os
import allure
from selene import browser, command, have, by


@allure.title('Форма регистрации студента')
def test_registration_form():
    with allure.step('Открываем форму'):
        browser.open('/automation-practice-form')

    with allure.step('Отключаем рекламу'):
        browser.all('.Google_Ad').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('.Google_Ad').perform(command.js.remove)

    with allure.step('Вводим данные студента'):
        browser.element('#firstName').type('Пользователь')
        browser.element('#lastName').type('Тестовый')
        browser.element('#userEmail').type('Test@gmail.com')
        browser.all('[for^=gender-radio-1]').element_by(have.exact_text('Male')).click()
        browser.element('#userNumber').type('8005553535')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text('June')
        ).click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text('1995')
        ).click()
        browser.element('.react-datepicker__day--013').click()

    with allure.step('Выбираем предмет'):
        browser.element('#subjectsInput').type('Ma').press_tab()

    with allure.step('Отмечаем хобби'):
        browser.all('[for^=hobbies-checkbox-1]').element_by(have.exact_text('Sports')).click()

    with allure.step('Загружаем картинку'):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/mem.jpg'))

    with allure.step('Вводим адрес'):
        browser.element('#currentAddress').type('Russia, Moscow')

    with allure.step('Выбираем штат и город'):
        browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
        browser.element('#react-select-4-input').type('Agra').press_enter()

    with allure.step('Нажимаем на кнопку "Submit"'):
        browser.element('#submit').perform(command.js.click)

    with allure.step('Проверяем введенные данные'):
        browser.all('.table td:nth-child(2)').should(
            have.texts('Пользователь Тестовый',
                       'Test@gmail.com',
                       'Test@gmail.com',
                       'Male',
                       '8005553535',
                       'Maths'
                       'Sports',
                       'Russia, Moscow',
                       'Uttar Pradesh Agra')
        )






'''
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
'''