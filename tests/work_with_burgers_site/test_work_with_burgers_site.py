from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.elements_to_find import TestLocators as TestL
from tests.elements_to_find import have_text

name = 'Ирина'
email = 'imerenkova07sun@yandex.ru'
password = 'Qwerty123@Qwerty'


def test_move_to_lk(driver):
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    driver.find_element(*have_text(*TestL.BUTTON_ON_HEADER, 'Личный Кабинет')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.BUTTON_UNDER_FORM,
                                                                                               'Сохранить')))
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    assert driver.find_element(*TestL.FIELD_LOGIN_IN_LK).get_attribute('value') == email
    assert driver.find_element(*TestL.FIELD_NAME_IN_LK).get_attribute('value') == name


def test_move_from_lk_to_constructor(driver):
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    driver.find_element(*have_text(*TestL.BUTTON_ON_HEADER, 'Личный Кабинет')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.BUTTON_UNDER_FORM,
                                                                                               'Сохранить')))
    driver.find_element(*have_text(*TestL.BUTTON_ON_HEADER, 'Конструктор')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    element = driver.find_element(*TestL.HEADER_CREATE_BURGER).text
    assert element == 'Соберите бургер'


def test_move_from_lk_to_main_page_click_on_logo(driver):
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    driver.find_element(*have_text(*TestL.BUTTON_ON_HEADER, 'Личный Кабинет')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.BUTTON_UNDER_FORM,
                                                                                               'Сохранить')))
    driver.find_element(*TestL.LOGO).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    element = driver.find_element(*TestL.HEADER_CREATE_BURGER).text
    assert element == 'Соберите бургер'


def test_move_between_ingridients_in_constructor(driver):
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestL.TITLE_SIGN_IN))
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'name')).send_keys(email)
    driver.find_element(*have_text(*TestL.FIELD_SIGN_IN_FORM, 'Пароль')).send_keys(password)
    driver.find_element(*have_text(*TestL.ACTION_BUTTON, 'Войти')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestL.SECTION_CTEATE_BURGER))
    driver.find_element(*have_text(*TestL.COMPONENTS_FOR_BURGERS, 'Начинки')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(have_text(*TestL.INGRIDIENT_FOR_BURGER,
                                                                    'Плоды Фалленианского дерева')))

    sauce = driver.find_element(*have_text(*TestL.INGRIDIENT_FOR_BURGER, 'Соус традиционный галактический'))
    driver.execute_script("arguments[0].scrollIntoView();", sauce)
    sauce = sauce.text
    assert sauce == 'Соус традиционный галактический'

    element = driver.find_element(*have_text(*TestL.INGRIDIENT_FOR_BURGER, 'Плоды Фалленианского дерева'))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element = element.text
    assert element == 'Плоды Фалленианского дерева'

    driver.find_element(*have_text(*TestL.COMPONENTS_FOR_BURGERS, 'Булки')).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(have_text(*TestL.INGRIDIENT_FOR_BURGER,
                                                                    'Краторная булка N-200i')))
    bun = driver.find_element(*have_text(*TestL.INGRIDIENT_FOR_BURGER, 'Краторная булка N-200i'))
    driver.execute_script("arguments[0].scrollIntoView();", bun)
    bun = bun.text
    assert bun == 'Краторная булка N-200i'
