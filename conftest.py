import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()  # создание объекта для опций
    chrome_options.add_argument('--window-size=1440,900')  # задаём разрешение экрана
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()
