test_val = True
browser_profile = "C:\\divar-web-driver"
input_jsonfile = 'output.json'
output_xlsxfile = 'appliance6.xlsx'
wait_before_click = 0.5 # time to load page after loading finished and befor click on get phone number button
wait_after_click = 1 # time to wait on page for anti block error (429 Too Many Requests) 
crawl_starts_from = 450 # for numberphone limit (get inf per day is ~200 in divar website.) (min)
crawl_limit = 500 # for debug or test by programmer (for ex : 2 or 5) (max)