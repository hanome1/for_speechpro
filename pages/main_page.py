from driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.header import Header
from selenium.common.exceptions import NoSuchElementException
import logging


class MainPage:
    Header = Header

    main_txt_xpath = '/html/body/section/div[2]/div/h1'


    def wait_for_loader_off():
        # WebDriverWait(Driver(), 30).until_not(EC.presence_of_element_located((By.XPATH, MainPage.main_txt_xpath)))
        logging.info(MainPage.main_txt_xpath)
        while True:
            try:
                Driver().find_element(By.XPATH(MainPage.main_txt_xpath)).text
                return True
            except NoSuchElementException:
                continue



    def verify_page():
        MainPage.wait_for_loader_off()
        Driver().find_element(By.XPATH(MainPage.main_txt_xpath)).text

