from driver import Driver
from selenium.webdriver.common.by import By
from components.header import Header


class ProfilePage:
    Header = Header

    main_txt_xpath = '/html/body/section/div[2]/div/h1'


    def verify_page():
        ProfilePage.Header.verify_component()
        Driver().find_element(By.XPATH(ProfilePage.main_txt_xpath))

