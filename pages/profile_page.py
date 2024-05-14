from pages.BasePage import BasePage, Locators
    
class ProfilePage(BasePage):

    def get_title(self):
        return self.get_text(Locators.locs["PROFILE_PAGE_TXT"], description="profile page text")