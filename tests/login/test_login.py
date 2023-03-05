from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.elements_to_find import TestLocators as TestL
from tests.elements_to_find import have_text

email = 'imerenkova07sun@yandex.ru'
password = 'Qwerty123@Qwerty'


def test_login_via_button_sing_in(driver):
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    element = driver.find_element(*TestL.CREATE_ORDER_BUTTON).text
    assert element == 'Оформить заказ'


def test_login_via_lk(driver):
    driver.find_element(*have_text(*TestL.BUTTON_ON_HEADER, 'Личный Кабинет')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    element = driver.find_element(*TestL.CREATE_ORDER_BUTTON).text
    assert element == 'Оформить заказ'


def test_login_via_registratin_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.TITLE_ABOVE_FORM,
                                                                                               'Регистрация')))
    driver.find_element(*have_text(*TestL.LINK_ON_FORM, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    element = driver.find_element(*TestL.CREATE_ORDER_BUTTON).text
    assert element == 'Оформить заказ'


def test_login_via_restore_password_form(driver):
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(have_text(*TestL.LINK_ON_FORM, 'Восстановить пароль')))

    el = driver.find_element(*have_text(*TestL.LINK_ON_FORM, 'Восстановить пароль'))
    driver.execute_script("arguments[0].scrollIntoView();", el)
    el.click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.TITLE_ABOVE_FORM,
                                                                                               'Восстановление пароля')))
    element = driver.find_element(*have_text(*TestL.TITLE_ABOVE_FORM, 'Восстановление пароля')).text
    assert element == 'Восстановление пароля'

    driver.find_element(*have_text(*TestL.LINK_ON_FORM, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    element = driver.find_element(*TestL.CREATE_ORDER_BUTTON).text
    assert element == 'Оформить заказ'
