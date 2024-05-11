import yaml
from pages.BasePage import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
import time
import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


# with open("locators.yaml") as f:
#     loc = yaml.safe_load(f)

def test_step1(browser):
    logging.info('Test1 starting')
    test_page = BasePage(browser)

    result = HomePage(browser).get_homepage_text()
    
    logging.info(f'result: {result}')
    assert result == 'Test home page', 'Text on home page does not match'


def test_step2(browser):
    logging.info('Test2 starting')
    test_page = BasePage(browser)

    time.sleep(1)
    BasePage(browser).click_login_btn()
    time.sleep(1)
    result = LoginPage(browser).get_login_page_text()

    logging.info(f'result: {result}')
    assert result == 'Login', 'Text on home page does not match'

    

# def test_step1(browser):
#     logging.info('Test1 starting')
#     test_page = OperationsHelper(browser)
#     test_page.go_to_site()
#     test_page.enter_email(loc["EMAIL"])
#     test_page.enter_pas(loc["PAS"])
#     test_page.click_login_btn()
#     assert test_page.get_err_text() == 'Flask Auth Example'


# def test_step2(site, login_field, pas_field, log_btn, blog_head,
#                new_post_btn, new_post_title, new_post_desc, new_post_content, new_post_confirm_btn, new_post_result):
#     input1 = site.find_element("xpath", login_field)
#     input1.send_keys(cfg["user"])
#     input2 = site.find_element("xpath", pas_field)
#     input2.send_keys(cfg["pas"])
#     log_btn = site.find_element("xpath", log_btn)
#     log_btn.click()
#     login = site.find_element("xpath", blog_head)
#     assert login.text == "Blog"

#     # homework2

#     # time.sleep(1)
#     # title = 'Test#'
#     # new_post_btn = site.find_element("xpath", new_post_btn)
#     # new_post_btn.click()
#     # new_post_title = site.find_element("xpath", new_post_title)
#     # new_post_title.send_keys(title)
#     # new_post_confirm_btn = site.find_element("xpath", new_post_confirm_btn)
#     # new_post_confirm_btn.click()
#     # time.sleep(1)
#     # new_post_result = site.find_element("xpath", new_post_result)
#     # assert new_post_result.text == title

#     # homework3

# def test_step2(browser):
#     logging.info('Test2 starting')
#     test_page = OperationsHelper(browser)
#     test_page.go_to_site()
#     test_page.enter_login(cfg['user'])
#     test_page.enter_pas(cfg['pas'])
#     test_page.click_login_btn()
#     assert test_page.get_blog_header() == 'Blog'

# def test_step3(browser):
#     logging.info('Test3 starting')
#     test_page = OperationsHelper(browser)
#     # time.sleep(1)
#     title = 'Test#'
#     test_page.click_new_post_btn()
#     test_page.enter_new_post_title(title)
#     test_page.click_new_post_confirm_btn()
#     time.sleep(1)
#     assert test_page.get_new_post_header() == title

# def test_step4(browser):
#     logging.info('Test4 starting')
#     test_page = OperationsHelper(browser)
#     # time.sleep(1)
#     text = 'Test#'
#     email = 'test@test'
#     test_page.click_contact_btn()
#     test_page.enter_contact_name(text)
#     # time.sleep(1)
#     test_page.enter_contact_email(email)
#     # time.sleep(1)
#     test_page.enter_contact_content(text)
#     time.sleep(1)
#     test_page.click_contact_confirm_btn()
#     msg = test_page.switch_to_alert()
#     logging.info(f'Got alert message: {msg}')
#     assert msg == 'Form successfully submitted'

# def test_step5_1(token):
#     logging.info('Test5_1 starting')
#     res_get = requests.get(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'owner': 'notMe'}).json()
#     # print(res_get)
#     res = False
#     for post in res_get['data']:
#         if cfg['post_desc'] in post['description']:
#             res = True
#     assert res, 'POST NOT FOUND'


# def test_step5_2(token):
#     logging.info('Test5_2 starting')
#     post = requests.post(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'title': 'Test title', 'description': cfg['post_test_desc'], 'content': 'test text content\n'*10})
#     res_get = requests.get(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'description': cfg['post_test_desc']}).json()
#     res = False
#     for post in res_get['data']:
#         if cfg['post_test_desc'] == post['description']:
#             res = True
#     assert res, 'POST NOT FOUND'
    
