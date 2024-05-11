from pages.BasePage import BasePage, TestSearchLocators
from selenium.webdriver.common.by import By
import logging
import yaml

# class TestSearchLocators():
#     locs = {}
#     with open("locators.yaml") as f:
#         locators = yaml.safe_load(f)
#     for locator in locators:
#         locs[locator] = (By.XPATH, locators[locator])
            
            
    # for locator in locators["css"].keys():
    #     locs[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    
class HomePage(BasePage):
    
    # TEXT INPUT

    def enter_login(self, word):
        self.input_text(TestSearchLocators.locs["LOCATOR_LOGIN_FIELD"], word, description="Login form")


    # CLICK

    def click_login_btn(self):
        self.click(TestSearchLocators.locs["LOCATOR_LOGIN_BTN"], description="login")


    # GET TEXT


    def get_homepage_text(self):
        return self.get_text(TestSearchLocators.locs["HOMEPAGE_TXT"], description="fuck")
    
   
    # def get_alert_text(self):
    #     logging.info("Get alert text")
    #     text = self.alert()
    #     logging.info(text)
    #     return text