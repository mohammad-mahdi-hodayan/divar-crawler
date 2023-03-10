'''https://api.divar.ir/v8/postcontact/web/contact_info/wY_2uZU7'''
from main_config import *
if (test_val) :
    print("config file loaded.")
else : 
    print("error : we couldn't find config file !")
from selenium import webdriver
import json
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("user-data-dir="+browser_profile) 
driver = webdriver.Chrome(options=options)
query = user_query.replace(" ","%20")
print(user_query);
is_end = 0
start_page = 1
main_obj = {}
i = 1 
def main(start_page_function) :
    global i
    global is_end
    if (is_end == 0) : 
        url = "http://divar.ir/s/"+city+"?q="+query+"&page="+str(start_page_function)
        driver.get(url)
        if (driver.find_elements_by_css_selector('.post-card-item-af972 .kt-post-card__title')) :
            print("crawling page : " + str(start_page_function))
            elements = driver.find_elements_by_css_selector(".post-card-item-af972 > a")
            for el in elements : 
                obj = {}
                href = el.get_attribute('href')
                title = el.get_attribute('title')
                obj["title"] = title 
                obj["link"] = href
                subdict_name = "t"+str(i)
                main_obj[subdict_name] = obj
                i = i + 1
            start_page_in = start_page_function + 1
            main(start_page_in)
        else :
            print("this was the last page...")
            is_end = 1
            print("generating json output file")
            driver.close()
            with open('output.json', 'w',encoding='utf8') as convert_file:
                convert_file.write(json.dumps(main_obj,ensure_ascii=False))
main(start_page)
time.sleep(1)
driver.close()
exit()