
# DIVAR crawler

## Description

this code will crawl all of the data from divar website using python and webdrivers. you can crawl number phones, titles, subtitles, table data and descriptions. output will be a json file that Contains URLs and excel file Contains all of the information that was said.

### Words from the programmer :

1. Any monetary use of the program without informing the programmer is a violation of the programming rights of the project, and please contact the programmer before that.
2. If you see any bug in program, I will be happy to keep you informed and fix it together.
3. This software has a fundamental problem, After 250 crawls, the site will block your session. If you have any ideas to solve this problem, please share it.
4. Respect the license fee. This is open source software but always respect the developers for the time they spentRespect the license fee. This is open source software but always respect the developers for the time they spent

## Usage

first of all run `install-req.bat` (if you are a windows os user) or install the requirements with `pip install requirements.txt`.

after that you need to download your chrome [webdrivers ](https://chromedriver.chromium.org/downloads/)from :

```bash

  https://chromedriver.chromium.org/downloads/

```

*( notes :*

*- a web driver is already in main folder for ver 110.xxx of chrome*

*- you can see your browser version from this URl : `chrome://version/ `)*

everything is readyeverything is ready for start !

now run `login.py` and login to your account and close the browser. (close the code first by "ctrl + c" 😅)

(note : before that open `login_config.py` in editor and change `browser_profile`  value to address that you want to save your driver profile. ex : C:\\divar-web-driver_acc1 )

now the coockies saved successfuly. edit `main_config.py` set the `browser_profile` as same before and enter your query in `user_query` and choose your city by changing `city` value.

simply run `main.py ` and wait to end crawl. you will have a file with name of `output.json`
(note : if you want to crawl a category run `main_cat_crawler.py` and change the cat name in line 24 )

edit advanced_config.py :

- insert `input_jsonfile` (ex : output.json)
- `output_xlsxfile` is name of final excel output
- `wait_before_click` and `wait_after_click` are time to wait on page for anti block error (429 Too Many Requests)
- `crawl_starts_from` and `crawl_limit` are values that tell to code where it should start and end crawling

(note : we use crawl_starts_from Becausebe you can't crawl more than **250 pages per day** )

After all these boring steps, at the end just run `advanced-crawler.py` and enjoy the results !

#### last words

I hope this code helps you, enjoy your evry moment in your life and be helpful for other. 

> all from a progressing person (MMH) 🌈🤍
