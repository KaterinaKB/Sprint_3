import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import elements_locators as el
import pytest


class TestOfConstructorTransitions:

    @pytest.mark.parametrize('driver', [el.start_url], indirect=True)
    def test_transition_buns_button_buns_displayed(self, driver):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.constr_sauces_xpath))).click()
        driver.find_element(By.XPATH, el.constr_buns_xpath).click()
        time.sleep(1)
        container_location = driver.find_element(By.XPATH, el.ingredients_container_xpath).location
        buns_header_location = driver.find_element(By.XPATH, el.constr_buns_header_xpath).location
        assert container_location['y'] == buns_header_location['y']

    @pytest.mark.parametrize('driver', [el.start_url], indirect=True)
    def test_transition_sauces_button_sauces_displayed(self, driver):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.constr_sauces_xpath))).click()
        time.sleep(1)
        container_location = driver.find_element(By.XPATH, el.ingredients_container_xpath).location
        sauces_header_location = driver.find_element(By.XPATH, el.constr_sauces_header_xpath).location
        assert container_location['y'] == sauces_header_location['y']

    @pytest.mark.parametrize('driver', [el.start_url], indirect=True)
    def test_transition_toppings_button_toppings_displayed(self, driver):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, el.constr_toppings_xpath))).click()
        time.sleep(1)
        container_location = driver.find_element(By.XPATH, el.ingredients_container_xpath).location
        toppings_header_location = driver.find_element(By.XPATH, el.constr_toppings_header_xpath).location
        assert container_location['y'] == toppings_header_location['y']

