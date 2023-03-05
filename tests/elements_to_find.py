from selenium.webdriver.common.by import By


def have_text(method, locator, text):
    locator = locator.format(text)
    return method, locator


class TestLocators:
    # Кнопки Войти / Зарегистрироваться
    ACTION_BUTTON = By.XPATH, "//button[contains(text(), '{}')]"  # SIGN_IN_BUTTON

    # Тайтл "Вход" над формой входа
    TITLE_SIGN_IN = By.XPATH, "//div[@class = 'Auth_login__3hAey'][h2 = 'Вход'][form]"

    # Поля Email / Пароль на форме авторизации
    FIELD_SIGN_IN_FORM = By.XPATH, "//input[@name='{}']"

    # Ссылки на формы Войти / Зарегистрироваться / Восстановить пароль
    LINK_ON_FORM = By.XPATH, "//a[contains(text(), '{}')]"

    # Заголовки Регистрация / Восстановление пароля / Соусы
    TITLE_ABOVE_FORM = By.XPATH, "//h2[text()='{}']"

    # Поле ввода Имени при регистрации
    FIELD_NAME_REGISTRATION_FORM = By.XPATH, "//div[label[text() = 'Имя']]/input[@name='name']"

    # Поле ввода Email при регистрации
    FIELD_EMAIL_REGISTRATION_FORM = By.XPATH, "//div[label[text() = 'Email']]/input[@name='name']"
    # Поле ввода Пароль при регистрации
    FIELD_PASSWORD_REGISTRATION_FORM = By.XPATH, "//div[label[text() = 'Пароль']]/input[@name='Пароль']"

    # Секция сборки бургера
    SECTION_CTEATE_BURGER = By.XPATH, "//main/section[contains(@class,'BurgerIngredients_ingredients')][h1[text(" \
                                      ")='Соберите бургер']] "
    # Заголовок Соберите бургер
    HEADER_CREATE_BURGER = By.XPATH, "//h1[text()='Соберите бургер']"
    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text() = 'Оформить заказ']"

    # Текст ошибки "Некорректный пароль", при вводе невалидного пароля
    TEXT_INVALID_PASSWORD = By.XPATH, "//p[contains(@class, 'input__error') and text() = 'Некорректный пароль']"

    # Текст ошибки "Такой пользователь уже существует"
    TEXT_EMAIL_EXIST = By.XPATH, "//p[contains(@class, 'input__error') and text() = 'Такой пользователь уже " \
                                 "существует'] "

    # Кнопки Личный Кабинет / Конструктор вверху страницы
    BUTTON_ON_HEADER = By.XPATH, "//p[text() = '{}']"

    # Кнопки Сохранить / Выход
    BUTTON_UNDER_FORM = By.XPATH, "//button[text()='{}']"

    # Поле ввода Пароль при регистрации
    FIELD_LOGIN_IN_LK = By.XPATH, "//input[contains(@class, 'input__textfield') and @name = 'name' and not(@type = " \
                                  "'password')] "
    # Поле ввода Пароль при регистрации
    FIELD_NAME_IN_LK = By.XPATH, "//input[contains(@class, 'input__textfield') and @name = 'Name' and not(@type = " \
                                 "'password')] "

    # Раздел Булки / Начинки / Соусы
    COMPONENTS_FOR_BURGERS = By.XPATH, "//span[text()='{}']"

    # Конкретные ингридиенты: Начинки / Соусы / Булки
    INGRIDIENT_FOR_BURGER = By.XPATH, "//p[text()='{}']"

    # Логотип Stellar Burgers
    LOGO = By.XPATH, "//div[contains(@class, 'header__logo')]"
