from selene import browser, have, be, command
import os
from selene.support.shared import browser


def test_form_complete():
    # Открытие страницы с формой регистрации
    browser.open('/automation-practice-form')

    # Заполнение текстовых полей: имя, фамилия, электронная почта и номер телефона
    browser.element('#firstName').should(be.blank).type('Alex ')
    browser.element('#lastName').should(be.blank).type('Taylor')
    browser.element('#userEmail').should(be.blank).type('alex.taylor@test.ru')

    # Выбор радиокнопки для пола
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('9876543210')

    # Выбор даты рождения через виджет календаря
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element(f'option[value="4"]').click()  # Месяц: Май
    browser.element('.react-datepicker__year-select').element(f'option[value="1991"]').click()  # Год: 1991
    browser.element('.react-datepicker__day--004:not(.react-datepicker__day--outside-month)').click()  # День: 4

    # Ввод и выбор предмета, а также выбор хобби
    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element("label[for='hobbies-checkbox-1']").click()  # Хобби: Спорт
    browser.element("label[for='hobbies-checkbox-3']").click()  # Хобби: Музыка

    # Загрузка файла с изображением
    print("Текущий рабочий каталог:", os.getcwd())
    browser.element('#uploadPicture').send_keys(os.path.abspath('data/image.png'))

    # Заполнение поля адреса
    browser.element('#currentAddress').type('ул. Пушкина 12')

    # Выбор штата и города из выпадающих списков
    browser.element('#state').click()
    browser.element('#react-select-3-option-3').perform(command.js.click)
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').perform(command.js.click)  # Город: Джайсалмер

    # Отправка заполненной формы
    browser.element('#submit').click()

    # Проверка правильности заполнения формы с помощью проверок на текст в таблице результатов
    result_table = browser.element('.table-responsive')
    # Для каждого поля проверяем соответствие введенным данным
    result_table.element("//*[contains(text(),'Student Name')]/following-sibling::td").should(have.text('Alex Taylor'))
    result_table.element("//*[contains(text(),'Student Email')]/following-sibling::td").should(
        have.text('alex.taylor@test.ru'))
    result_table.element("//*[contains(text(),'Gender')]/following-sibling::td").should(have.text('Male'))
    result_table.element("//*[contains(text(),'Mobile')]/following-sibling::td").should(have.text('9876543210'))
    result_table.element("//*[contains(text(),'Date of Birth')]/following-sibling::td").should(have.text('04 May,1991'))
    result_table.element("//*[contains(text(),'Subjects')]/following-sibling::td").should(have.text('Maths'))
    result_table.element("//*[contains(text(),'Hobbies')]/following-sibling::td").should(have.text('Sports, Music'))
    result_table.element("//*[contains(text(),'Picture')]/following-sibling::td").should(have.text('image.png'))
    result_table.element("//*[contains(text(),'Address')]/following-sibling::td").should(have.text('ул. Пушкина 12'))
    result_table.element("//*[contains(text(),'State and City')]/following-sibling::td").should(
        have.text('Rajasthan Jaiselmer'))
