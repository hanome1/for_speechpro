from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.common.by import By

 
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://localhost:5000/")


# text method is used in python to retrieve the text of WebElement

# print(driver.find_element(By.CSS_SELECTOR, "h1").text)
print(driver.find_element(By.XPATH, "/html/body/section/div[2]/div/h1").text == 'Test home page')

driver.close()