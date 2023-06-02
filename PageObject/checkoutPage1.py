from selenium.webdriver.common.by import By


class Checkout1:
    def __init__(self, driver):
        self.driver = driver

        self.text_checkout = '//*[@id="checkout"]'
        self.text_yourInformation = '//*[@id="header_container"]/div[2]/span'
        self.first_name = '//*[@id="first-name"]'
        self.last_name = '//*[@id="last-name"]'
        self.postal_code = '//*[@id="postal-code"]'
        self.continue1 =  '//*[@id="continue"]'
        self.error = '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3'
        self.cancel = '//*[@id="cancel"]'
        self.text_login = '//*[@id="login-button"]'


    def checkout(self):
        self.driver.find_element(By.XPATH, self.text_checkout).click()

    def checkout_Your_Information(self):
        return self.driver.find_element(By.XPATH, self.text_yourInformation).text

    def input_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.first_name).send_keys(firstname)

    def input_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.last_name).send_keys(lastname)

    def input_postalcode(self, postal_code):
        self.driver.find_element(By.XPATH, self.postal_code).send_keys(postal_code)

    def continue_next(self):
        return self.driver.find_element(By.XPATH, self.continue1).text

    def click_continue(self):
        return self.driver.find_element(By.XPATH, self.continue1).click()

    def text_error(self):
        return self.driver.find_element(By.XPATH, self.error).text

    def button_cancel(self):
        self.driver.find_element(By.XPATH, self.cancel).click()

    def text_login(self):
        return self.driver.find_element(By.XPATH, self.text_login).text

