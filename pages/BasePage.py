from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import yaml
import logging

class Data_():
    email = 'test5@test'
    name = 'test'
    pas = 'passwd'
    
class Locators():
    locs = {}
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators:
        locs[locator] = (By.XPATH, locators[locator])

class BasePage():
    def __init__(self, driver) -> None:
        self.driver = driver
        # self.base_url = "http://localhost:5000/"

    def find_element(self, locator, time=30):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator} ")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found in element with locator {locator}')
            return None

    # def go_to_site(self):
    #     try:
    #         start_browsing = self.driver.get(self.base_url)
    #     except:
    #         logging.exception("Exception while open site")
    #         start_browsing = None
    #     return start_browsing
    
    def alert(self):
        try:
            alert_obj = self.driver.switch_to.alert
            return alert_obj.text
        except:
            logging.exception("Exception with alert")
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
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(locator)
        field = self.find_element(locator, time=10)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
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