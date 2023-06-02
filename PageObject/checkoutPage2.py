from selenium.webdriver.common.by import By

class Checkout2:
    def __init__(self, driver):
        self.driver = driver

        self.text_checkout = '//*[@id="checkout"]'
        self.checkout_overview = '//*[@id="header_container"]/div[2]/span'
        self.finish = '//*[@id="finish"]'
        self.complete = '//*[@id="header_container"]/div[2]/span'
        self.back_home = '//*[@id="back-to-products"]'
        self.product = '//*[@id="header_container"]/div[2]/span'
        self.overview_cancel_button = '//*[@id="cancel"]'

    def cont_checkout(self):
        return self.driver.find_element(By.XPATH, self.text_checkout).click()

    def Checkout_Overview(self):
        return self.driver.find_element(By.XPATH, self.checkout_overview).text

    def click_finish(self):
        return self.driver.find_element(By.XPATH, self.finish).click()

    def text_complete(self):
        return self.driver.find_element(By.XPATH, self.complete).text

    def click_Back_home(self):
        return self.driver.find_element(By.XPATH, self.back_home).click()

    def text_product(self):
        return self.driver.find_element(By.XPATH, self.product).text

    def click_overview_btn_cancel(self):
        return self.driver.find_element(By.XPATH, self.overview_cancel_button).click()
