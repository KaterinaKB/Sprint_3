# TESTS FOR Stellar Burgers

## Конфигурирование и запуск тестов
Переда запуском можно отредактировать файл test_config.json

В нем можно указать:
* значение 'Chrome' или 'Firefox' для Browser, при использовании другого значения будет использовано дефолтное значение 'Chrome'
* любые значения для 'login' и 'password', соответствующие существующему зарегистрированному пользователю

Тесты необходимо запускать из директории ./tests
````
cd ./tests
pytest ./*.py
````

## Дерево проекта

     |- README.md #Общая информация о проекте
     |- conftest.py #Используемые фикстуры
     |- test_config.json #Конфигурационный файл
     |- /tests
            |-elements_locators.py #Используемые локаторы
            |-service_functions.py #Вспомогательные функции
            |-test*.py #Файлы, содержащие тесты


## Описание тестов
### test_registration.py
* test_regist_valid_values_successful_regist #Проверка успешной регистрации. Критерий успешной регистрации - возможность авторизоваться под новой парой логин-пароль.
* test_regist_wrong_password_regist_error #Проверка появления ошибки для некорректного пароля

### test_login.py
Критерий успешной авторизации во всех случаях открытие стартовой страницы с доступной кнопкой Оформить заказ
* test_login_with_main_login_button_successful_login #Проверка входа по кнопке «Войти в аккаунт» на главной странице
* test_login_with_pers_acc_button_successful_login #Проверка входа через кнопку «Личный кабинет»
* test_login_with_reg_form_button_successful_login #Проверка входа через кнопку в форме регистрации
* test_login_with_fogot_pass_button_successful_login #Проверка входа через кнопку в форме восстановления пароля

### test_pers_account_transitions.py
* test_transition_with_pers_acc_button_pers_acc_page_opened #Проверка перехода в личный кабинет по клику на «Личный кабинет»
* test_transition_with_logo_button_main_page_opened #Проверка перехода из личного кабинета на стартовую по клику на логотип Stellar Burgers
* test_transition_with_constr_button_main_page_opened #Проверка перехода из личного кабинета на стартовую по клику на «Конструктор»
* test_logout_with_logout_button_logout #Проверка выхода по кнопке «Выйти» в личном кабинете

### test_constructor_transitions.py
* test_transition_buns_button_buns_displayed #Проверка перехода к разделу Меню Булки
* test_transition_sauces_button_sauces_displayed #Проверка перехода к разделу Меню Соусы
* test_transition_toppings_button_toppings_displayed #Проверка перехода к разделу Меню Начинки