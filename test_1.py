from pages.BasePage import BasePage, User
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.signup_page import SignupPage
import time
import logging

# увы, не справился с выносом драйвера в отдельный класс, дабы избежать копипасты с browser в атрибутах


# проверка заголовка домашней страницы
def test_step1(browser):
    logging.info('Test1 starting. Checking the title of home page')

    result = HomePage(browser).get_title()
    logging.debug(f'result: {result}')
    assert result == 'Test home page', 'Text on home page does not match'
    logging.info('Test1 passed!')

# проверка заголовка страницы регистрации
def test_step2(browser):
    logging.info('Test2 starting. Going to signup page and checking the title')

    time.sleep(0.5)
    LoginPage(browser).click_signup_btn() 
    time.sleep(0.5)
    result = LoginPage(browser).get_title()

    logging.debug(f'result: {result}')
    assert result == 'Sign Up', 'Text on home page does not match'
    logging.info('Test2 passed!')


# проверка обязательности поля email регистрации
def test_step3(browser):
    logging.info('Test3 starting. Check is email field required')

    time.sleep(0.5)
    assert SignupPage(browser).check_email_field_required(), 'email field should not be left empty'

# проверка обязательности поля name регистрации
def test_step4(browser):
    logging.info('Test4 starting. Check is name field required')

    time.sleep(0.5)
    assert not SignupPage(browser).check_name_field_reqierd(), 'name field can be empty'
    logging.info('Test4 passed!')

# проверка обязательности поля pas регистрации
def test_step5(browser):
    logging.info('Test5 starting. Check is pas field required')

    time.sleep(0.5)
    assert SignupPage(browser).check_pas_field_reqierd(), 'pas field should not be left empty'
    logging.info('Test5 passed!')


# проверка успешной регистрцации по заголовку страницы login
def test_step6(browser):
    logging.info('Test6 starting. Registrating new user')

    # заполняем все поля валидными данными
    SignupPage(browser).input_email(User.email)
    SignupPage(browser).input_name(User.name)
    SignupPage(browser).input_pas(User.pas)

    SignupPage(browser).click_signup_confirm_btn()
    time.sleep(0.5)

    # проверяеем, что после успешной регистрации мы перенаправлены на login page
    result = LoginPage(browser).get_title()
    logging.debug(f'result: {result}')
    assert result == 'Login', 'Text on login page does not match'
    logging.info('Test6 passed!')
    

# проверка успешного логина по тексту приветсвтия
def test_step7(browser):
    logging.info('Test7 starting. Logging in')
    while LoginPage(browser).get_title() != 'Login':
        BasePage(browser).click_login_btn()

    # заполняем все поля валидными данными
    LoginPage(browser).input_email(User.email)
    LoginPage(browser).input_pas(User.pas)

    LoginPage(browser).click_login_btn()
    time.sleep(0.5)

    result = ProfilePage(browser).get_title()
    logging.debug(f'result: {result}')
    assert result == F'Welcome, {User.name}!', 'Text on profile page does not match'
    logging.info('Test7 passed!')


# проверка регистрации пользователя повторно по тексту алерта (понимаю, что это не алерт, но назвал его таким образом)
def test_step8(browser):
    logging.info('Test8 starting. Trying to registrate an existing user')
    if BasePage(browser).is_login():
        BasePage(browser).click_logout_btn()
    BasePage(browser).click_signup_btn()
    
    time.sleep(0.5)
    SignupPage(browser).input_email(User.email)
    SignupPage(browser).input_name(User.name)
    SignupPage(browser).input_pas(User.pas)
    SignupPage(browser).click_signup_confirm_btn()
    time.sleep(0.5)
    
    result = SignupPage(browser).get_alert_text()
    logging.debug(f'result: {result}')
    assert result == 'Email address already exists. Go to login page.', 'Text of signup alert does not match'
    logging.info('Test8 passed!')


# проверка регистрации с пустыми полями по появлению алерта
# мне не удалось отловить подсказку поля email, поэтому пытался отловить любой алерт, отличный от алерта в предыдущем тесте
def test_step9(browser):
    logging.info('Test9 starting. Trying to registrate using all fields empty')
    if BasePage(browser).is_login():
        BasePage(browser).click_logout_btn()
    BasePage(browser).click_signup_btn()
    time.sleep(0.5)
    SignupPage(browser).input_email(User.email_clear)
    SignupPage(browser).input_name(User.name_clear)
    SignupPage(browser).input_pas(User.pas_clear)
    SignupPage(browser).click_signup_confirm_btn()
    time.sleep(0.5)
    
    result = SignupPage(browser).get_alert_text()
    logging.debug(f'result: {result}')
    assert result != (None or 'Email address already exists. Go to login page.'), 'Text of signup alert does not match'
    logging.info('Test9 passed!')