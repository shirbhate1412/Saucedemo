import os
import time
import pytest
from selenium.webdriver.common.by import By
from utilities.logger import Logclass
from PageObject.loginpage import Login
from PageObject.dashboard import Dashboard

@pytest.mark.usefixtures("setup")
class Testlogin(Logclass):
    def test_001(self):
        log = self.getLogger()

        lg = Login(self.driver)
        db = Dashboard(self.driver)

        log.info("Test Case 001")
        log.info("Test case starting")
        lg.input_username("standard_user")
        log.info("entered passsword")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(5)
        # log.info("click login")
        if 'Products' in lg.text_product():
            assert True
            log.info("Test case Pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_002(self):
        log = self.getLogger()

        lg = Login(self.driver)
        db = Dashboard(self.driver)

        log.info("Test Case 002")
        lg.input_username("standard_user12")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(5)
        if 'Epic sadface: Username and password do not match any user in this service' in self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text:
             assert True
             log.info("Test case Pass")
        else:
            log.critical("Test Case Failed")
            assert False


    def test_003(self):
        log = self.getLogger()
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log.info("Test Case 003")
        lg.input_username("standard_user12")
        lg.input_password("secret_sauce12")
        lg.click_login()
        time.sleep(2)
        if 'Epic sadface: Username and password do not match any user in this service' in self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text:
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False


    def test_004(self):
        log = self.getLogger()
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log.info("Test Case 004")
        lg.input_username("standard_user")
        lg.input_password("secret_sauce12")
        lg.click_login()
        time.sleep(2)
        if 'Epic sadface: Username and password do not match any user in this service' in self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text:
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False
