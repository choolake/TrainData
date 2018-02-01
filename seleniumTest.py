#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://eservices.railway.gov.lk/schedule")
assert "Train" in driver.title
elem1 = Select(driver.find_element_by_xpath('.//*[@id=\'startStation\']'))
#elem.clear()
#elem1.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
elem1.select_by_visible_text('GAMPAHA')
##elem2.select_by_visible_text('KURUNEGALA')
elem2 = Select(driver.find_element_by_xpath('.//*[@id=\'endStation\']'))
elem2.select_by_visible_text('KURUNEGALA')
driver.find_element_by_xpath('.//*[@id=\'search_form_id\']/div/div[7]/div/button[1]').click()
#assert "No results found." not in driver.page_source
driver.implicitly_wait(10) # seconds
te1 =driver.find_element_by_xpath(".//*[@id='es-content']/div[6]/div").text
print(te1)
#driver.close()
