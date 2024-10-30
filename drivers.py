import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def driver_setup():
    """
    Function to create a driver for Linkedin and log in using different drivers for each session to prevent bot detection.

    Returns:
    WebDriver: Initialized web driver.
    """
    random_driver = int(random.uniform(1,3))
    if random_driver == 1:
        try:
            driver = webdriver.Chrome()
        except:
            driver = webdriver.Chrome(ChromeDriverManager().install())
    elif random_driver == 2:
        try:
            driver = webdriver.Edge()
        except:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.delete_all_cookies()
    #driver.get("https://linkedin.com")
    driver.maximize_window()
    driver.implicitly_wait(3)
    time.sleep(random.uniform(2,4))
    return driver