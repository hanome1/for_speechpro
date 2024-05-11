from driver import Driver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.profile_page import ProfilePage
from components.header import Header
import logging


def test_main_page(browser: Driver):
    logging.info('test started')
    text_we_get = MainPage.verify_page(browser)
    logging.info(text_we_get)
    assert text_we_get, 'PIZDA'