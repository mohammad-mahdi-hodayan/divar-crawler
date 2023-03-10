from login_config import *
if (test_val) :
    print("config file loaded.")
else : 
    print("error : we couldn't find config file !")
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("user-data-dir="+browser_profile) 
driver = webdriver.Chrome(options=options)
url = "http://divar.ir/"
driver.get(url)
time.sleep(1000)