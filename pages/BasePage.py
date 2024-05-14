from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import yaml
import logging


# здесь должен был быть класс-генератор тестового пользователя
class User():
    email = 'test111@test'
    email_clear = ''
    email_one_symbol = '1'
    email_only_dog = '@'
    email_dog_symbol = '@1'

    name = 'test'
    name_clear = ''

    pas = 'passwd'
    pas_clear = ''


# заморочился с файлом, содержащим разные локаторы, но использовал в итоге только xpath
class Locators():
    locs = {}
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators:
        locs[locator] = (By.XPATH, locators[locator])


# основные функции сайта и хедера
class BasePage():
    def __init__(self, driver) -> None:
        self.driver = driver


    def find_element(self, locator, time=30):
        # logging.debug(f'{locator=}')
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator} ")
        except:
            logging.exception("ELEMENT NOT FOUND")
            element = None
        return element


    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found in element with locator {locator}')
            return None


    def input_text(self, locator, text, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {text} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(text)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True


    def click(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
        logging.debug(f'Clicked {element_name} button') 
        return True


    def get_text(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        # logging.info(locator)
        field = self.find_element(locator, time=1)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'found text {text} in field {element_name}')
        text = field.text
        return text
        

    def click_home_btn(self):
        self.click(Locators.locs["HOME_BTN"])

        
    def click_login_btn(self):
        self.click(Locators.locs["LOGIN_BTN"])


    def click_signup_btn(self):
        self.click(Locators.locs["SIGNUP_BTN"])


    def click_profile_btn(self):
        self.click(Locators.locs["PROFILE_BTN"])


    def click_logout_btn(self):
        self.click(Locators.locs["LOGOUT_BTN"])


    def check_requred(self, locator):
        return self.find_element(locator).get_attribute('required') == True
    

    def is_login(self):
        return self.get_text(Locators.locs["SIGNUP_BTN"]) == 'Logout'