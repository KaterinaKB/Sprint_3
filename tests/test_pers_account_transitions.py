import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import elements_locators as el
import pytest


class TestOfPersonalAccountTransitions:

    @pytest.mark.parametrize('authorized_driver', [el.start_url], indirect=True)
    def test_transition_with_pers_acc_button_pers_acc_page_opened(self, authorized_driver):
        authorized_driver.find_element(By.XPATH, el.pers_account_xpath).click()
        assert WebDriverWait(authorized_driver, 3).until(ec.presence_of_element_located((By.XPATH, el.profile_link_xpath)))

    @pytest.mark.parametrize('authorized_driver', [el.pers_acc_profile_url], indirect=True)
    def test_transition_with_logo_button_main_page_opened(self, authorized_driver):
        WebDriverWait(authorized_driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, el.logo_button_class))).click()
        assert WebDriverWait(authorized_driver, 3).until(ec.presence_of_element_located((By.XPATH, el.start_page_header_xpath)))

    @pytest.mark.parametrize('authorized_driver', [el.pers_acc_profile_url], indirect=True)
    def test_transition_with_constr_button_main_page_opened(self, authorized_driver):
        WebDriverWait(authorized_driver, 5).until(ec.presence_of_element_located((By.XPATH, el.constructor_button_xpath))).click()
        WebDriverWait(authorized_driver, 5).until(ec.url_to_be(el.start_url))
        assert WebDriverWait(authorized_driver, 3).until(ec.presence_of_element_located((By.XPATH, el.start_page_header_xpath)))

    @pytest.mark.parametrize('authorized_driver', [el.pers_acc_profile_url], indirect=True)
    def test_logout_with_logout_button_logout(self, authorized_driver):
        WebDriverWait(authorized_driver, 5).until(ec.presence_of_element_located((By.XPATH, el.logout_button_xpath))).click()
        assert WebDriverWait(authorized_driver, 3).until(ec.presence_of_element_located((By.XPATH, el.login_header_xpath)))