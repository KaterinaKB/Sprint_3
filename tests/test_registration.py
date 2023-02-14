import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import elements_locators as el
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import service_functions as sf


class TestOfRegistration:
    @pytest.mark.parametrize('driver', [el.registr_url], indirect=True)
    def test_regist_valid_values_successful_regist(self, driver):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.name_xpath))).send_keys('User name')
        email = sf.random_email()
        driver.find_element(By.XPATH, el.email_xpath).send_keys(email)
        password = sf.random_password(6)
        driver.find_element(By.XPATH, el.password_xpath).send_keys(password)
        driver.find_element(By.XPATH, el.registr_button_xpath).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.login_header_xpath)))
        driver.find_element(By.XPATH, el.email_xpath).send_keys(email)
        driver.find_element(By.XPATH, el.password_xpath).send_keys(password)
        driver.find_element(By.XPATH, el.login_button_xpath).click()
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, el.pers_account_xpath))).click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.profile_link_xpath)))
        assert driver.find_element(By.XPATH, el.pers_account_name_xpath).get_attribute('value') == 'User name' and driver.find_element(By.XPATH, el.pers_account_email_xpath).get_attribute('value') == email

    @pytest.mark.parametrize('driver', [el.registr_url], indirect=True)
    def test_regist_wrong_password_regist_error(self, driver):
        driver.find_element(By.XPATH, el.name_xpath).send_keys('User name')
        email = sf.random_email()
        driver.find_element(By.XPATH, el.email_xpath).send_keys(email)
        password = sf.random_password(5)
        driver.find_element(By.XPATH, el.password_xpath).send_keys(password)
        driver.find_element(By.XPATH, el.registr_button_xpath).click()
        assert driver.find_element(By.XPATH, el.wrong_password_path)
        driver.quit()
