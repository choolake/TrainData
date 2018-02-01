#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://eservices.railway.gov.lk/schedule")
assert "Train" in driver.title
selStart = Select(driver.find_element_by_xpath('.//*[@id=\'startStation\']'))
startOptions = selStart.options
selend = Select(driver.find_element_by_xpath('.//*[@id=\'endStation\']'))
endOptions = selend.options
startindex in range(0, len(startOptions) - 1):
    selstart.select_by_index(startindex)
    # do stuff
    endindex in range(0, len(endOptions) - 1):
        selend.select_by_index(endindex)
        #click the button
        driver.find_element_by_xpath('.//*[@id=\'search_form_id\']/div/div[7]/div/button[1]').click()
        driver.implicitly_wait(10) # seconds
        te1 =driver.find_element_by_xpath(".//*[@id='es-content']/div[6]/div").text
        print(te1)
#driver.close()
