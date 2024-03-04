import os
import allure
from selene import browser, command, have, by, be


@allure.title('Форма регистрации студента')
def test_registration_form():
    with allure.step('Открываем форму'):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step('Вводим данные студента'):
        browser.element('#firstName').should(be.blank).with_(type_by_js=True).type('Пользователь')
        browser.element('#lastName').should(be.blank).with_(type_by_js=True).type('Тестовый')
        browser.element('#userEmail').should(be.blank).with_(type_by_js=True).type('Test@gmail.com')
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
        browser.element('#userNumber').should(be.blank).with_(type_by_js=True).type('1002003040')
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
                       'Male',
                       '8005553535',
                       '13 June,1995'
                       'Maths'
                       'Sports',
                       'mem.jpg'
                       'Russia, Moscow',
                       'Uttar Pradesh Agra')
        )

