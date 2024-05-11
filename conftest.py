import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
import requests

# with open("./config.yaml") as f:
#     testdata = yaml.safe_load(f)
# browser = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    # if browser == "firefox":
    #     service = Service(executable_path=GeckoDriverManager().install())
    #     options = webdriver.FirefoxOptions()
    #     driver = webdriver.Firefox(service=service, options=options)
    # else:
    serv = Service(executable_path=ChromeDriverManager().install())
    ops = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=serv, options=ops)
    yield driver
    driver.quit()


# with open("config.yaml") as f:
#     cfg = yaml.safe_load(f)


# @pytest.fixture()
# def token():
#     return requests.post(
#         url=cfg["login"], data={"username": cfg["user"], "password": cfg["pas"]}
#     ).json()["token"]


# @pytest.fixture()
# def post_create():
#     res = requests.post(
#         url=cfg["posts"],
#         headers={"X-Auth-Token": token},
#         params={
#             "title": "Test title",
#             "description": cfg["post_test_desc"],
#             "content": "test text content\n" * 10,
#         },
#     )


# @pytest.fixture()
# def login_field():
#     return """//*[@id="login"]/div[1]/label/input"""


# @pytest.fixture()
# def pas_field():
#     return """//*[@id="login"]/div[2]/label/input"""


# @pytest.fixture()
# def log_btn():
#     return """//*[@id="login"]/div[3]/button"""


# @pytest.fixture()
# def err_label():
#     return """//*[@id="app"]/main/div/div/div[2]/h2"""


# @pytest.fixture()
# def blog_head():
#     return """//*[@id="app"]/main/div/div[1]/h1"""


# @pytest.fixture()
# def site():
#     site = Site(cfg["address"])
#     yield site
#     site.close()


# @pytest.fixture()
# def new_post_btn():
#     return """//*[@id="create-btn"]"""


# @pytest.fixture()
# def new_post_title():
#     return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


# @pytest.fixture()
# def new_post_desc():
#     return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


# @pytest.fixture()
# def new_post_content():
#     return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


# @pytest.fixture()
# def new_post_confirm_btn():
#     return """//*[@id="create-item"]/div/div/div[7]/div/button"""


# @pytest.fixture()
# def new_post_result():
#     return """//*[@id="app"]/main/div/div[1]/h1"""

# @pytest.fixture()
# def token():
#     return requests.post(url=cfg['login'], data={'username': cfg['user'], 'password': cfg['pas']}).json()['token']


