from pages.BasePage import BasePage, Data_
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.signup_page import SignupPage
import time
import logging

# увы, не справился с выносом драйвера в отдельный класс, дабы избежать копипасты с browser в атрибутах


# проверка заголовка домашней страницы
def test_step1(browser):
    logging.info('Test1 starting')

    result = HomePage(browser).get_title()
    
    logging.info(f'result: {result}')
    assert result == 'Test home page', 'Text on home page does not match'

# проверка заголовка страницы регистрации
def test_step2(browser):
    logging.info('Test2 starting')

    time.sleep(0.5)
    LoginPage(browser).click_signup_btn() 
    time.sleep(0.5)
    result = LoginPage(browser).get_title()

    logging.info(f'result: {result}')
    assert result == 'Sign Up', 'Text on home page does not match'


# проверка обязательности поля email регистрации
def test_step3(browser):
    logging.info('Test3 starting')

    time.sleep(0.5)
    assert SignupPage(browser).check_email_field_reqierd(), 'email field should not be left empty'

# проверка обязательности поля name регистрации
def test_step4(browser):
    logging.info('Test4 starting')

    time.sleep(0.5)
    assert not SignupPage(browser).check_name_field_reqierd(), 'name field can be empty'

# проверка обязательности поля pas регистрации
def test_step5(browser):
    logging.info('Test5 starting')

    time.sleep(0.5)
    assert SignupPage(browser).check_pas_field_reqierd(), 'pas field should not be left empty'


# проверка успешной регистрцации по заголовку страницы login
def test_step6(browser):
    logging.info('Test6 starting')
    SignupPage(browser).input_email(Data_.email)
    SignupPage(browser).input_name(Data_.name)
    SignupPage(browser).input_pas(Data_.pas)

    SignupPage(browser).click_signup_confirm_btn()
    time.sleep(0.5)

    result = LoginPage(browser).get_title()
    logging.info(f'result: {result}')
    assert result == 'Login', 'Text on login page does not match'
    

# проверка успешного логина по тексту приветсвтия
def test_step7(browser):
    logging.info('Test7 starting')
    while LoginPage(browser).get_title() != 'Login':
        BasePage(browser).click_login_btn()
    LoginPage(browser).input_email(Data_.email)
    time.sleep(0.5)
    LoginPage(browser).input_pas(Data_.pas)
    time.sleep(0.5)
    LoginPage(browser).click_login_btn()
    time.sleep(3)

    result = ProfilePage(browser).get_title()
    logging.info(f'result: {result}')
    assert result == F'Welcome, {Data_.name}!', 'Text on profile page does not match'


# проверка регистрации с пустыми полями по появлению алерта
def test_step8(browser):
    logging.info('Test8 starting')
    time.sleep(0.5)
    BasePage(browser).click_logout_btn()
    time.sleep(0.5)
    BasePage(browser).click_signup_btn()
    time.sleep(0.5)
    SignupPage(browser).input_email('')
    time.sleep(0.5)
    SignupPage(browser).input_name('') 
    time.sleep(0.5)
    SignupPage(browser).input_pas('')
    time.sleep(0.5)
    SignupPage(browser).click_signup_confirm_btn()
    time.sleep(0.5)
    
    result = SignupPage(browser).get_alert_text()
    logging.info(f'result: {result}')
    assert result != (None or 'Email address already exists. Go to login page.'), 'Text of signup alert does not match'


# проверка регистрации с некорректным email по тексту алерта
def test_step9(browser):
    logging.info('Test9 starting')
    time.sleep(0.5)
    SignupPage(browser).input_email('test')
    time.sleep(0.5)
    SignupPage(browser).input_name('') 
    time.sleep(0.5)
    SignupPage(browser).input_pas('')
    time.sleep(0.5)
    SignupPage(browser).click_signup_confirm_btn()
    time.sleep(1)
    
    result = SignupPage(browser).get_alert_text()
    logging.info(f'result: {result}')
    assert result == 'Email address already exists. Go to login page.', 'Text of signup alert does not match'