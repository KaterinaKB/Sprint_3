from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import elements_locators as el
import pytest


class TestOfLogin:
    @pytest.mark.parametrize('driver', [el.start_url], indirect=True)
    def test_login_with_main_login_button_successful_login(self, driver, config):
        driver.find_element(By.XPATH, el.login_page_button_xpath).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.login_header_xpath)))
        driver.find_element(By.XPATH, el.email_xpath).send_keys(config['login'])
        driver.find_element(By.XPATH, el.password_xpath).send_keys(config['password'])
        driver.find_element(By.XPATH, el.login_button_xpath).click()
        assert WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.order_button_xpath)))

    @pytest.mark.parametrize('driver', [el.start_url], indirect=True)
    def test_login_with_pers_acc_button_successful_login(self, driver, config):
        driver.find_element(By.XPATH, el.pers_account_xpath).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.login_header_xpath)))
        driver.find_element(By.XPATH, el.email_xpath).send_keys(config['login'])
        driver.find_element(By.XPATH, el.password_xpath).send_keys(config['password'])
        driver.find_element(By.XPATH, el.login_button_xpath).click()
        assert WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.order_button_xpath)))

    @pytest.mark.parametrize('driver', [el.registr_url], indirect=True)
    def test_login_with_reg_form_button_successful_login(self, driver, config):
        driver.find_element(By.XPATH, el.login_link_other_forms_xpath).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.login_header_xpath)))
        driver.find_element(By.XPATH, el.email_xpath).send_keys(config['login'])
        driver.find_element(By.XPATH, el.password_xpath).send_keys(config['password'])
        driver.find_element(By.XPATH, el.login_button_xpath).click()
        assert WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.order_button_xpath)))

    @pytest.mark.parametrize('driver', [el.forgot_pass_url], indirect=True)
    def test_login_with_fogot_pass_button_successful_login(self, driver, config):
        driver.find_element(By.XPATH, el.login_link_other_forms_xpath).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.login_header_xpath)))
        driver.find_element(By.XPATH, el.email_xpath).send_keys(config['login'])
        driver.find_element(By.XPATH, el.password_xpath).send_keys(config['password'])
        driver.find_element(By.XPATH, el.login_button_xpath).click()
        assert WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.order_button_xpath)))
