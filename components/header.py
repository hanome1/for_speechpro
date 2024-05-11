from driver import Driver
from selenium.webdriver.common.by import By


class Header:
    home_btn_xpath = '//*[@id="navbarMenuHeroA"]/div/a[1]'
    login_profile_btn_xpath = '//*[@id="navbarMenuHeroA"]/div/a[2]'
    signup_logout_btn_xpath = '//*[@id="navbarMenuHeroA"]/div/a[3]'


    # def verify_header():
    #     Driver().find_element(By.XPATH(Header.home_btn_xpath))


    def click_home_btn():
        home = Driver().find_element(By.XPATH(Header.home_btn_xpath))
        home.click


    def click_login_profile_btn():
        login_profile = Driver().find_element(By.XPATH(Header.login_profile_btn_xpath))
        login_profile.click


    def signup_logout_btn():
        signup_logout = Driver().find_element(By.XPATH(Header.signup_logout_btn_xpath))
        signup_logout.click

