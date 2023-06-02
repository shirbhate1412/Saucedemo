from PageObject.checkoutPage2 import Checkout2
from PageObject.checkoutPage1 import Checkout1
from PageObject.loginpage import Login
from PageObject.dashboard import Dashboard
import pytest
from utilities.logger import Logclass
import time

@pytest.mark.usefixtures("setup")
class Testlogin(Logclass):

    def test_019(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 019")
        db = Dashboard(self.driver)
        lg = Login(self.driver)
        info = Checkout1(self.driver)

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
        ck1.checkout()

        info.input_firstname("Jin")
        info.input_lastname("Jing")
        info.input_postalcode('123546')
        time.sleep(20)
        ck1.click_continue()
        time.sleep(2)
        ck2.click_finish()
        time.sleep(2)

        if 'Checkout: Complete!' in ck2.text_complete():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_020(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 020")
        db = Dashboard(self.driver)
        lg = Login(self.driver)
        info = Checkout1(self.driver)

        lg.input_username("standard_user")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(2)
        db.click_item()
        time.sleep(2)
        db.click_add_to_card()
        time.sleep(2)
        db.click_add_to_card_logo()
        time.sleep(2)
        ck1.checkout()

        info.input_firstname("Jin")
        info.input_lastname("Jing")
        info.input_postalcode('123546')
        time.sleep(1)
        ck1.click_continue()
        time.sleep(2)
        ck2.click_finish()
        time.sleep(2)
        ck2.click_Back_home()

        if 'Products' in lg.text_product():
            assert True
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def text_021(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 021")
        db = Dashboard(self.driver)
        lg = Login(self.driver)
        info = Checkout1(self.driver)

        lg.input_username("standard_user")
        lg.input_password("secret_sauce")
        lg.click_login()
        time.sleep(2)
        db.click_item()
        time.sleep(2)
        db.click_add_to_card()
        time.sleep(2)
        db.click_add_to_card_logo()
        time.sleep(2)
        ck1.checkout()

        info.input_firstname("Jin")
        info.input_lastname("Jing")
        info.input_postalcode('123546')
        time.sleep(1)
        ck1.click_continue()

        ck2.click_overview_btn_cancel()

        if 'Products' in ck2.text_product():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False