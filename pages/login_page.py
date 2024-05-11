from pages.BasePage import BasePage, TestSearchLocators

class LoginPage(BasePage):
    
    # TEXT INPUT

    def enter_login(self, word):
        self.input_text(TestSearchLocators.locs["LOCATOR_LOGIN_FIELD"], word, description="Login form")


    # CLICK

    def click_login_btn(self):
        self.click(TestSearchLocators.locs["LOCATOR_LOGIN_BTN"], description="login")


    # GET TEXT


    def get_login_page_text(self):
        return self.get_text(TestSearchLocators.locs["LOGIN_PAGE_TXT"], description="login page text")
    
   
    # def get_alert_text(self):
    #     logging.info("Get alert text")
    #     text = self.alert()
    #     logging.info(text)
    #     return text