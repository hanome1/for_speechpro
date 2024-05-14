from pages.BasePage import BasePage, Locators
    
class HomePage(BasePage):
    
    def get_title(self):
        return self.get_text(Locators.locs["HOMEPAGE_TXT"], description="home page text")