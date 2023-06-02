from selenium.webdriver.common.by import By


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

        self.text = '//*[@id="login_button_container"]/div/form/div[3]/h3'
        self.item = '//*[@id="item_4_title_link"]/div'
        self.add_to_card_btn = '//*[@id="add-to-cart-sauce-labs-backpack"]'
        self.add_to_card_logo = '//*[@id="shopping_cart_container"]/a'
        self.remove = '//*[@id="remove-sauce-labs-backpack"]'
        self.card = '//*[@id="header_container"]/div[2]/span'
        self.countinue_shpooing = '//*[@id="continue-shopping"]'
        self.back_to_product = '//*[@id="back-to-products"]'
        self.product = '//*[@id="header_container"]/div[2]/span'
        self.selectItem = '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'

    def text_dashboard(self):
        return self.driver.find_element(By.XPATH, self.text).text

    def click_item(self):
        self.driver.find_element(By.XPATH, self.item).click()

    def text_select_item(self):
        return self.driver.find_element(By.XPATH, self.selectItem).text

    def click_add_to_card(self):
        self.driver.find_element(By.XPATH, self.add_to_card_btn).click()

    def click_add_to_card_logo(self):
        self.driver.find_element(By.XPATH, self.add_to_card_logo).click()

    def click_remove(self):
        return self.driver.find_element(By.XPATH, self.remove).text

    def text_your_card(self):
        return self.driver.find_element(By.XPATH, self.card).text

    def click_continue_shopping(self):
        self.driver.find_element(By.XPATH, self.countinue_shpooing).click()

    def click_back_to_product(self):
        self.driver.find_element(By.XPATH, self.back_to_product).click()

    def text_product(self):
        return self.driver.find_element(By.XPATH, self.product).text