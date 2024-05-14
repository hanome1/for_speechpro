from pages.BasePage import BasePage, Locators

class LoginPage(BasePage):
    

    def get_title(self):
        return self.get_text(Locators.locs["LOGIN_PAGE_TXT"], description="login page text")
    
   
    def input_email(self, word):
        self.input_text(Locators.locs["LOGIN_EMAIL_FIELD"], word, description="email form")


    def input_pas(self, word):
        self.input_text(Locators.locs["LOGIN_PAS_FIELD"], word, description="passwd form")


    def click_login_btn(self):
        self.click(Locators.locs["LOGIN_CONFIRM_BTN"], description="login confirm btn")