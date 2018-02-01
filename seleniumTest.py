#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://eservices.railway.gov.lk/schedule")
assert "Train" in driver.title
selStart = Select(driver.find_element_by_xpath('.//*[@id=\'startStation\']'))
startOptions = selStart.options
selEnd = Select(driver.find_element_by_xpath('.//*[@id=\'endStation\']'))
endOptions = selEnd.options
for startIndex in range(1, len(startOptions) - 1):
    selStart.select_by_index(startIndex)
    # do stuff
    for endIndex in range(1, len(endOptions) - 1):
        selEnd.select_by_index(endIndex)
        #click the button
        driver.find_element_by_xpath('.//*[@id=\'search_form_id\']/div/div[7]/div/button[1]').click()
        driver.implicitly_wait(10) # seconds
	try:
            te1 =driver.find_element_by_xpath(".//*[@id='es-content']/div[6]/div").text
            print(te1)
            driver.get("https://eservices.railway.gov.lk/schedule")
        except NoSuchElementException:
            #print (Error Occured...)
            print( "error occured while start ", startIndex," and end ", endIndex)
            pass
#driver.close()

