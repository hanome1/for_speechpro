from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from components.header import Header

from driver import Driver


class LoginPage:
    Header = Header
    
    title_xpath = '/html/body/section/div[2]/div/div/h3'
    email_field_xpath = '/html/body/section/div[2]/div/div/div/form/div[1]/div/input'
    pas_field_xpath = '/html/body/section/div[2]/div/div/div/form/div[2]/div/input'
    remember_me_checkbox_xpath = '/html/body/section/div[2]/div/div/div/form/div[3]/label'
    login_btn_xpath = '/html/body/section/div[2]/div/div/div/form/button'


    def verify_page(expected_txt: str):
        # SearchPage.wait_for_loader_off(driver)
        LoginPage.Header.verify_component()
        Driver().find_element(By.XPATH(LoginPage.title_xpath))

        # articles = driver.find_elements_by_xpath(SearchPage.title_xpath)
        # assert articles, "empty articles list"

        # errors = []
        # for article in articles:
        #     if expected_string_in_results not in article.text.lower():
        #         errors.append(f"'{expected_string_in_results}' not found in '{article.text.lower()}'")

        # assert not errors, errors


    def input_email(email: str):
        input_email = Driver().find_element(By.XPATH(LoginPage.email_field_xpath))
        input_email.send_keys(email)


    def input_pas(pas: str):
        input_pas = Driver().find_element(By.XPATH(LoginPage.pas_field_xpath))
        input_pas.send_keys(pas)


    def press_login_button():
        login_button = Driver().find_element(By.XPATH(LoginPage.login_btn_xpath))
        login_button.click()