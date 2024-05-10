from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocators():
    locs = {}
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators:
        locs[locator] = (By.XPATH, locator)
            
            
    # for locator in locators["css"].keys():
    #     locs[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    
class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, text, description=None):
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

    def click_button(self, locator, description=None):
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

    def get_text_from_element(self, locator, description=None):

        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(By.XPATH, locator, time=10)
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
    
    # TEXT INPUT

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_LOGIN_FIELD"], word, description="Login form")

    def enter_pas(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_PASS_FIELD"], word, description="Password form")

    def enter_new_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_TITLE_FIELD"], word, description="title form")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_DESCRIPTION_FIELD"], word, description="description form")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_CONTENT_FIELD"], word, description="post content form")

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_CONTACT_NAME_FIELD"], word, description="name form")

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_CONTACT_EMAIL_FIELD"], word, description="email form")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.locs["LOCATOR_CONTACT_CONTENT_FIELD"], word,
                                    description="contact content form")

    # CLICK

    def click_login_btn(self):
        self.click_button(TestSearchLocators.locs["LOCATOR_LOGIN_BTN"], description="login")

    def click_new_post_btn(self):
        self.click_button(TestSearchLocators.locs["LOCATOR_NEW_POST_BTN"], description="new post")

    def click_new_post_confirm_btn(self):
        self.click_button(TestSearchLocators.locs["LOCATOR_SAVE_BTN"], description="save post")

    def click_contact_button(self):
        self.click_button(TestSearchLocators.locs["LOCATOR_CONTACT_BTN"], description="contact")

    def contact_us_save_button(self):
        self.click_button(TestSearchLocators.locs["LOCATOR_CONTACT_SAVE_BTN"], description="contact save")

    # GET TEXT


    # def get_blog_header(self):
    def get_homepage_text(self):
        blog_header = self.find_element(TestSearchLocators.locs["HOMEPAGE_TXT"], timer=3)
        text = blog_header.text
        # logging.info(f'Got text: {text} in blog header: {TestSearchLocators.LOCATOR_BLOG_HEADER[1]}')
        return text


        # return self.find_element(By.XPATH, "/html/body/section/div[2]/div/h1").text
        return self.find_element(By.CSS_SELECTOR, "h1").text
    
    def get_title_text(self):
        return self.get_text_from_element(TestSearchLocators.locs["LOCATOR_TITLE_TEXT"], description="title")

    def get_err_text(self):
        return self.get_text_from_element(TestSearchLocators.locs["LOCATOR_ERROR_FIELD"], description="error label")

    def get_profile_text(self):
        return self.get_text_from_element(TestSearchLocators.locs["LOCATOR_USER_PROFILE_NAME"], description="user profile name")

    def get_alert_text(self):
        logging.info("Get alert text")
        text = self.alert()
        logging.info(text)
        return text