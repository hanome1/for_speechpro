from pages.BasePage import BasePage, Locators
    
class SignupPage(BasePage):
    

    def get_title(self):
        return self.get_text(Locators.locs["SIGNUP_PAGE_TXT"], description="signup page text")
    

    def check_email_field_required(self):
        self.check_requred(Locators.locs["SIGNUP_EMAIL_FIELD"])


    def input_email(self, email):
        self.input_text(Locators.locs["SIGNUP_EMAIL_FIELD"], email, description="email form")
    



    def check_name_field_reqierd(self):
        self.check_requred(Locators.locs["SIGNUP_NAME_FIELD"])


    def input_name(self, name):
        self.input_text(Locators.locs["SIGNUP_NAME_FIELD"], name, description="name form")
    



    def check_pas_field_reqierd(self):
        self.check_requred(Locators.locs["SIGNUP_PAS_FIELD"])


    def input_pas(self, pas):
        self.input_text(Locators.locs["SIGNUP_PAS_FIELD"], pas, description="passwd form")




    def click_signup_confirm_btn(self):
        self.click(Locators.locs["SIGNUP_CONFIRM_BTN"], description="signup confirm btn")
    

    def get_alert_text(self):
        return self.get_text(Locators.locs["SIGNUP_ALERT_TXT"], description="signup alert text")