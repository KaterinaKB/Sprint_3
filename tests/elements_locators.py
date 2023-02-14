#Используемые ссылки
start_url = 'https://stellarburgers.nomoreparties.site/' #стартовая страница
login_url = 'https://stellarburgers.nomoreparties.site/login' #страница авторизации
registr_url = 'https://stellarburgers.nomoreparties.site/register' #страница регистрации
forgot_pass_url = 'https://stellarburgers.nomoreparties.site/forgot-password' #страница восстановления пароля
pers_acc_profile_url = 'https://stellarburgers.nomoreparties.site/account' #страница персонального аккаунта

#Используемые локаторы

#Поля на формах авторизации и регистрации (почта и пароль имеют одинаковые xpath на разных страницах)
name_xpath = ".//label[text() = 'Имя']/following-sibling::input"  #поле для ввода имени
email_xpath = ".//label[text() = 'Email']/following-sibling::input"  #поле для ввода адреса эл.почты
password_xpath = ".//label[text() = 'Пароль']/following-sibling::input"  #поле для ввода пароля

#Локаторы, связанные со страницей авторизации
login_page_button_xpath = ".//button[text() = 'Войти в аккаунт']"  #кнопка "Войти в аккаунт" для перехода на страницу авторизации
login_header_xpath = ".//h2[text() = 'Вход']" #хэдер страницы авторизации
login_button_xpath = ".//button[text() = 'Войти']"  #кнопка "Войти" для подтверждения авторизации
login_link_other_forms_xpath = ".//a[text() = 'Войти']" #ссфлка "Войти" для перехода на страцу авторизации с других страниц

#Локаторы, связанные со страницей регистрации
registr_link = ".//a[text() = 'Зарегистрироваться')]"#ссылка "Зарегистрироваться" для перехода на страницу регистрации со страницы авторизации
registr_button_xpath = "//button[text() = 'Зарегистрироваться']"#кнопка "Зарегистрироваться" для подтверждения регистрации
wrong_password_path = ".//p[text() = 'Некорректный пароль']" #элемент с ошибкой о некорректном пароле

#Локаторы, связанные со страницей персонального аккаунта
pers_account_xpath = ".//a[@href = '/account']"
pers_account_name_xpath = ".//label[text() = 'Имя']/following-sibling::input" #поле с именем
pers_account_email_xpath = ".//label[text() = 'Логин']/following-sibling::input" #поле с адресом эл.почты
profile_link_xpath = ".//a[text()='Профиль']" #ссылка для перехода на вкладку Профиль
logout_button_xpath = ".//button[text() = 'Выход']" #кнопка "Выход" для деавторизации

#Локаторы, связанные со стартовой страницей(Конструктор)
logo_button_class = "AppHeader_header__logo__2D0X2" #кнопка с логотипом
order_button_xpath = ".//button[text() = 'Оформить заказ']" #кнопка для оформления заказа
constructor_button_xpath = ".//p[text() = 'Конструктор']/parent::a" #ссылка "Конструктор" для перехода на стартовую стр.
start_page_header_xpath = ".//h1[text() = 'Соберите бургер']" #хэдер "Соберите бургер"
constr_buns_xpath = ".//span[text() = 'Булки']/parent::div"  #ссылка для прокрутки ингредиентов до Булок
constr_buns_header_xpath = ".//h2[text() = 'Булки']"  #хэдер раздела ингредиентов Булки
constr_sauces_xpath = ".//span[text() = 'Соусы']/parent::div"  #ссылка для прокрутки ингредиентов до Соусов
constr_sauces_header_xpath = ".//h2[text() = 'Соусы']"  #хэдер раздела ингредиентов Соусы
constr_toppings_xpath = ".//span[text() = 'Начинки']/parent::div"  #ссылка для прокрутки ингредиентов до Начинок
constr_toppings_header_xpath = ".//h2[text() = 'Начинки']"  #хэдер раздела ингредиентов Начинки
ingredients_container_xpath = ".//h2[text()='Булки']/parent::div" #контейнер с ингредиентами
