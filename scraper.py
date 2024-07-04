import requests
from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    # options.add_argument("no-sandbox")
    # options.add_experimental_option("exclueSwitches")

    driver = webdriver.Chrome(options)
    driver.get("http://automated.pythonanywhere.com")
    return driver
