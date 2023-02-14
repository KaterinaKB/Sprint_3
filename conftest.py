import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests import elements_locators as el
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

config_path = r'..\test_config.json'


@pytest.fixture(scope='session')
def config():
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def init_driver(config):
    if config['browser'] == 'Chrome':
        web_driver = webdriver.Chrome(executable_path='./chromedriver')
    elif config['browser'] == 'Firefox':
        web_driver = webdriver.Firefox(executable_path='./geckodriver')
    else:
        web_driver = webdriver.Chrome()
    return web_driver


@pytest.fixture
def driver(request, init_driver):
    init_driver.get(request.param)
    yield init_driver
    init_driver.quit()


@pytest.fixture
def authorized_driver(request, config, init_driver):
    email = config['login']
    password = config['password']
    init_driver.get(el.login_url)
    init_driver.find_element(By.XPATH, el.email_xpath).send_keys(email)
    init_driver.find_element(By.XPATH, el.password_xpath).send_keys(password)
    init_driver.find_element(By.XPATH, el.login_button_xpath).click()
    WebDriverWait(init_driver, 5).until(ec.url_to_be(el.start_url))
    init_driver.get(request.param)
    yield init_driver
    init_driver.quit()
