import time
from selenium import webdriver

# def get_driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("disable-infobars")
#     options.add_argument("start-maximized")
#     options.add_argument("disable-dev-shm-usage")
#     # options.add_argument("no-sandbox")
#     # options.add_experimental_option("exclueSwitches")

#     driver = webdriver.Chrome(options)
#     driver.get("http://automated.pythonanywhere.com")
#     return driver

def get_driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main(driver, xpath):
    # driver = get_driver()
    return driver.find_element("xpath",xpath).text

driver = get_driver()
time.sleep(2)
print(main(driver,"/html/body/div[1]/div/h1[1]")) #Inspect element to find xpath
print(main(driver,"/html/body/div[1]/div/h1[2]")) # Copy full xpath (!)
