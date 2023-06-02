from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver = driver

        self.user_name_XPATH = '//*[@id="user-name"]'
        self.password_Xpath = '//*[@id="password"]'
        self.login_XPATH = '//*[@id="login-button"]'
        self.text_message_XPATH = '//*[@id="login_button_container"]/div/form/div[3]/h3'
        self.product_text = '//*[@id="header_container"]/div[2]/span'


    def input_username(self,username):
        self.driver.find_element(By.XPATH, self.user_name_XPATH).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(By.XPATH, self.password_Xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_XPATH).click()

    def msg_invalid(self):
        return self.driver.find_element(By.XPATH, self.text_message_XPATH).text

    def text_product(self):
        return self.driver.find_element(By.XPATH, self.product_text).text