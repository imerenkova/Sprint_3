from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.elements_to_find import TestLocators as TestL
from tests.elements_to_find import have_text
from tests.generators import *


def test_successful_registration(driver):
    driver.find_element(*have_text(*TestL.BUTTON_ON_HEADER, 'Личный Кабинет')).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.LINK_ON_FORM, 'Зарегистрироваться')).click()
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/register'

    email_person = generate_login()
    driver.find_element(*TestL.FIELD_NAME_REGISTRATION_FORM).send_keys(get_name(email_person))
    driver.find_element(*TestL.FIELD_EMAIL_REGISTRATION_FORM).send_keys(email_person)
    driver.find_element(*TestL.FIELD_PASSWORD_REGISTRATION_FORM).send_keys(generate_password())
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Зарегистрироваться')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.ACTION_BUTTON,
                                                                                               'Войти')))


def test_invalid_password_5_symbol_during_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.TITLE_ABOVE_FORM,
                                                                                               'Регистрация')))
    email_person = generate_login()
    driver.find_element(*TestL.FIELD_NAME_REGISTRATION_FORM).send_keys(get_name(email_person))
    driver.find_element(*TestL.FIELD_EMAIL_REGISTRATION_FORM).send_keys(email_person)
    driver.find_element(*TestL.FIELD_PASSWORD_REGISTRATION_FORM).send_keys('12345')
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Зарегистрироваться')).click()
    element = driver.find_element(*TestL.TEXT_INVALID_PASSWORD).text
    assert element == 'Некорректный пароль'


def test_error_user_exist_during_registration(driver):
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.LINK_ON_FORM, 'Зарегистрироваться')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.TITLE_ABOVE_FORM,
                                                                                               'Регистрация')))
    email_person = generate_login()
    driver.find_element(*TestL.FIELD_NAME_REGISTRATION_FORM).send_keys(get_name(email_person))
    driver.find_element(*TestL.FIELD_EMAIL_REGISTRATION_FORM).send_keys(email_person)
    driver.find_element(*TestL.FIELD_PASSWORD_REGISTRATION_FORM).send_keys(generate_password())
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Зарегистрироваться')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.ACTION_BUTTON,
                                                                                               'Войти')))
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.find_element(*have_text(*TestL.LINK_ON_FORM, 'Зарегистрироваться')).click()
    driver.find_element(*TestL.FIELD_NAME_REGISTRATION_FORM).send_keys(get_name(email_person))
    driver.find_element(*TestL.FIELD_EMAIL_REGISTRATION_FORM).send_keys(email_person)
    driver.find_element(*TestL.FIELD_PASSWORD_REGISTRATION_FORM).send_keys(generate_password())
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Зарегистрироваться')).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestL.TEXT_EMAIL_EXIST))
    current_url = driver.current_url
    assert current_url != 'https://stellarburgers.nomoreparties.site/login'

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*TestL.TEXT_EMAIL_EXIST))

    text_error = driver.find_element(*TestL.TEXT_EMAIL_EXIST).text
    assert text_error == 'Такой пользователь уже существует'
