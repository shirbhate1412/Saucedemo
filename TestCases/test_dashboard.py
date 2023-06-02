import time

from PageObject.loginpage import Login
from PageObject.dashboard import Dashboard
from utilities.logger import Logclass
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Testlogin(Logclass):
    def test_005(self):
        log = self.getLogger()

        lg = Login(self.driver)
        db = Dashboard(self.driver)

        lg.input_username("standard_user")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(10)
        db.click_item()
        time.sleep(2)

        if 'Sauce Labs Backpack' in db.text_select_item():
            assert True
            log.info("Test case Pass")
        else:
            log.critical("Test Case Failed")
            assert False


    def test_006(self):
        log = self.getLogger()
        db = Dashboard(self.driver)
        lg = Login(self.driver)
        log.info("Test Case 006")

        lg.input_username("standard_user")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(2)
        db.click_item()
        db.click_add_to_card()
        time.sleep(2)
        if 'Remove' in db.click_remove():
            log.info("Test case Pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_007(self):
        log = self.getLogger()
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log.info("Test Case 007")

        lg.input_username("standard_user")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(2)
        db.click_item()
        time.sleep(2)
        db.click_add_to_card()
        db.click_add_to_card_logo()

        if 'Your Cart' in db.text_your_card():
            log.info("Test case Pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_008(self):
        log = self.getLogger()
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log.info("Test Case 008")

        lg.input_username("standard_user")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(2)
        db.click_item()
        time.sleep(2)
        db.click_add_to_card()
        time.sleep(2)
        db.click_back_to_product()
        time.sleep(5)

        if 'Products' in db.text_product():
            log.info("Test case Pass")
        else:
            log.critical("Test Case Failed")
            assert False

    def test_009(self):
        log = self.getLogger()
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        log.info("Test Case 009")

        lg.input_username("standard_user")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(2)
        db.click_item()
        time.sleep(2)
        db.click_add_to_card()
        time.sleep(5)
        db.click_add_to_card_logo()
        time.sleep(2)

        db.click_continue_shopping()

        if 'Products' in lg.text_product():
            assert True
            log.info("Test case Pass")
        else:
            log.critical("Test Case Failed")
            assert False