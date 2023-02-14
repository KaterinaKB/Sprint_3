import random
import string


def random_email():
    return f'voronova6{random.randint(100, 999)}@yandex.ru'


def random_password(password_lenght):
    password = ''
    for i in range(int(password_lenght)):
        password += random.choice(string.ascii_letters + string.digits)
    return password
