from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Jenkins compatible options
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)

    return driver