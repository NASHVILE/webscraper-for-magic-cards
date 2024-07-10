import requests
from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    # options.add_experimental_option("exclueSwitches")

    driver = webdriver.Chrome(options)
    return driver

def scrape_cards(driver, url):
    content = driver.get(url).content
    print(content)

if __name__ == "__main__":
    url = "https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&output=spoiler&method=visual&sort=abc%20,abc+&format=[%22Commander%22]"
    driver = get_driver() 
    scrape_cards(driver, url)
