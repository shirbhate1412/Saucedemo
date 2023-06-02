from PageObject.checkoutPage1 import Checkout1
from PageObject.checkoutPage2 import Checkout2
from PageObject.dashboard import Dashboard
from utilities.logger import Logclass
from PageObject.loginpage import Login
import time
import pytest

@pytest.mark.usefixtures("setup")
class Testlogin(Logclass):

    def test_008(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
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
        time.sleep(5)
        db.click_add_to_card_logo()
        time.sleep(2)
        ck1.checkout()

        if 'Checkout: Your Information' in ck1.checkout_Your_Information():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_009(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 009")
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

        ck1.click_continue()
        time.sleep(2)
        if 'Checkout: Overview' in ck2.Checkout_Overview():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False


    def test_010(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 010")
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

        time.sleep(5)
        info.input_firstname("Jin")
        info.input_lastname("Jing")
        info.input_postalcode('')
        time.sleep(2)
        ck1.click_continue()
        time.sleep(2)

        if 'Error: Postal Code is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False


    def test_011(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 011")
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
        info.input_lastname("")
        info.input_postalcode('')
        time.sleep(10)
        ck1.click_continue()
        time.sleep(5)

        if 'Error: Last Name is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_012(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 012")
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

        info.input_firstname("")
        info.input_lastname("")
        info.input_postalcode('')
        time.sleep(10)
        ck1.click_continue()
        time.sleep(5)

        if 'Error: First Name is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_013(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 013")
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

        info.input_firstname("")
        info.input_lastname("Jing")
        info.input_postalcode('')
        time.sleep(10)
        ck1.click_continue()
        time.sleep(5)

        if 'Error: First Name is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_014(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 014")
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

        info.input_firstname("")
        info.input_lastname("Jing")
        info.input_postalcode('123456')
        time.sleep(10)
        ck1.click_continue()
        time.sleep(5)

        if 'Error: First Name is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_015(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 015")
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
        info.input_postalcode('')
        time.sleep(10)
        ck1.click_continue()
        time.sleep(5)

        if 'Error: Postal Code is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_016(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 016")
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
        info.input_lastname("")
        info.input_postalcode('123456')
        time.sleep(5)
        ck1.click_continue()
        time.sleep(5)

        if 'Error: Last Name is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_017(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 017")
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

        info.input_firstname("")
        info.input_lastname("")
        info.input_postalcode('123456')
        time.sleep(10)
        ck1.click_continue()
        time.sleep(5)

        if 'Error: First Name is required' in ck1.text_error():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False

    def test_018(self):
        log = self.getLogger()
        ck1 = Checkout1(self.driver)
        ck2 = Checkout2(self.driver)
        log.info("Test Case 018")
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

        ck1.button_cancel()

        if 'Your Cart' in db.text_your_card():
            log.info("Test case Pass")
            assert True
        else:
            log.critical("Test Case Failed")
            assert False