from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.elements_to_find import TestLocators as TestL
from tests.elements_to_find import have_text

email = 'imerenkova07sun@yandex.ru'
password = 'Qwerty123@Qwerty'


def test_login_via_button_sing_in_and_logout(driver):
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
    driver.find_element(*have_text(*TestL.BUTTON_UNDER_FORM, 'Выход')).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(have_text(*TestL.ACTION_BUTTON,
                                                                                               'Войти')))
    current_url = driver.current_url
    assert current_url == 'https://stellarburgers.nomoreparties.site/login'
