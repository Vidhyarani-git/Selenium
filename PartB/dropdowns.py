#for chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#for Standard dropdown handling by selecting the options we import the select class
##from selenium.webdriver.support.select import Select

#standard dropdown single selection-By using index-select_by_index('index value')
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
##a=driver.find_element("id","oldSelectMenu")
##s=Select(a)
##s.select_by_index(1)
##time.sleep(4)

#standard dropdown single selection-By using value-select_by_value('value attribute')
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
##a=driver.find_element("id","oldSelectMenu")
##s=Select(a)
##s.select_by_value("4")
##time.sleep(4)

#standard dropdown single selection-By using value-select_by_visible_text('visible text')
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
##a=driver.find_element("id","oldSelectMenu")
##s=Select(a)
##s.select_by_visible_text("Black")
##time.sleep(4)

#Standard dropdown- deselect the  single option selection
#it throws error as NotImplementedError: You may only deselect options of a multi-select
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
##a=driver.find_element("id","oldSelectMenu")
##s=Select(a)
##s.select_by_visible_text("Black")
##time.sleep(4)
##s.deselect_by_visible_text("Black")
##time.sleep(4)

#task 1:-
# https://testautomationpractice.blogspot.com/
# select option in country dropdown
# using indexing try to select one option
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(4)
##a=driver.find_element("css selector","select.form-control")
##s=Select(a)
##s.select_by_index(3)
##time.sleep(4)

#task 2:-
# https://testautomationpractice.blogspot.com/
# select option in country dropdown
# using value attribute try to select one option
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(4)
##a=driver.find_element("css selector","select.form-control")
##s=Select(a)
##s.select_by_value("japan")
##time.sleep(4)

#task 3:-
# https://testautomationpractice.blogspot.com/
# select option in country dropdown
# using visible text try to select one option
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(4)
##a=driver.find_element("css selector","select.form-control")
##s=Select(a)
##s.select_by_visible_text("India")
##time.sleep(3)

#Standard dropdown single selection-multiple option selection by using id
##driver.get("https://demoqa.com/select-menu")
##time.sleep(4)
##a=driver.find_element("css selector","select#oldSelectMenu")
##s=Select(a)
##s.select_by_index(1)
##time.sleep(4)
##s.select_by_index(7)
##time.sleep(4)

#Standard dropdown multiple selection dropdown-by using combination of index,value,visible text
##driver.get("https://demoqa.com/select-menu")
##time.sleep(4)
##a=driver.find_element("css selector","select#cars")
##s=Select(a)
##s.select_by_index(1)
##time.sleep(2)
##s.select_by_value("opel")
##time.sleep(2)
##s.select_by_visible_text("Audi")
##time.sleep(2)
##print("multiple options selection pass")

#standard dropdown multiple options deselection by using combination of index,value and visible text
##driver.get("https://demoqa.com/select-menu")
##time.sleep(4)
##a=driver.find_element("css selector","select#cars")
##s=Select(a)
##s.select_by_index(1)
##time.sleep(2)
##s.select_by_value("opel")
##time.sleep(2)
##s.select_by_visible_text("Audi")
##time.sleep(2)
##--deselect combination of index,visible text and value
##s.deselect_by_index(3)
##time.sleep(2)
##s.deselect_by_visible_text("Opel")
##time.sleep(2)
##s.deselect_by_value("saab")
##time.sleep(2)
##deselect all
##s.deselect_all()
##time.sleep(2)
##print("multiple options deselection pass")

#Standard dropdowns-is_multiple property
#is multiple-true
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
####a=driver.find_element("css selector","select#cars")
####s=Select(a)
####print(s.is_multiple)
###is not multiple-None
##a=driver.find_element("xpath","//select[@id='oldSelectMenu']")
##s=Select(a)
##print(s.is_multiple)

#Standard dropdown- options property
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
###single select dropdown
####a=driver.find_element("xpath","//select[@id='oldSelectMenu']")
###multi select dropdown
##a=driver.find_element("xpath","//select[@id='cars']")
##s=Select(a)
###print(s.options)
##var=s.options
##for i in var:
##    print(i.text)

#Standard dropdown- all_selected_options property
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
##a=driver.find_element("xpath","//select[@id='cars']")
##s=Select(a)
##s.select_by_index(1)
##time.sleep(2)
##s.select_by_value("opel")
##time.sleep(2)
##s.select_by_visible_text("Audi")
##time.sleep(2)
####print(s.all_selected_options)
##var=s.all_selected_options
##for i in var:
##    print(i.text)

#Standard dropdown- first_selected_option property
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
##a=driver.find_element("xpath","//select[@id='cars']")
##s=Select(a)
##s.select_by_index(1)
##time.sleep(2)
##s.select_by_value("opel")
##time.sleep(2)
##s.select_by_visible_text("Audi")
##time.sleep(2)
####print(s.first_selected_option)
##var=s.first_selected_option
##print(var.text)

#---------------Non standard dropdown
##driver.get("https://demoqa.com/select-menu")
##time.sleep(2)
##driver.find_element("xpath","(//div[@class='css-19bb58m'])[2]").click()
##time.sleep(2)
##driver.find_element("xpath","//div[.='Other']").click()
##time.sleep(2)

driver.get("https://www.flipkart.com")
time.sleep(4)
driver.find_element("xpath","//span[@class='b3wTlE']").click()
time.sleep(4)
driver.find_element("xpath","(//div[@class='wszdrO'])[1]").click()
driver.find_element("xpath","(//div[@class='pkKEsC'])[2]").click()
time.sleep(4)

#task 1:-
#https://testautomationpractice.blogspot.com/
# check whther country dropdown is a single select dropdown or multi select dropdown
# write script for above
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","select#country")
##s=Select(a)
##print(s.is_multiple)

#task2:-
# check whther colors dropdown is a single select or multi select
# write script for above
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","select#colors")
##time.sleep(2)
##s=Select(a)
##print(s.is_multiple)

#task3:-
# extract options from country dropdown
# extract options from color dropdown
#write script for both
#extract options from color dropdown
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","select#colors")
##s1=Select(a)
##var1=s1.options
##for i in var1:
##    print(i.text)

# extract options from country dropdown
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##b=driver.find_element("css selector","select#country")
##s2=Select(b)
##var2=s2.options
##for i in var2:
##    print(i.text)

# task 4 :- on multi select dropdown:-
# from colors dropdown
# Select 3 colors
# Print selected colors
#write script for above
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","select#colors")
##s1=Select(a)
##s1.select_by_index(2)
##s1.select_by_index(3)
##s1.select_by_index(5)
##time.sleep(3)
##var1=s1.all_selected_options
##for i in var1:
##    print(i.text)

#task 5:- on multi select dropdown
# locate country dropdown
# Select 3 values
# Print only first selected
#write script for above
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##b=driver.find_element("css selector","select#country")
##s2=Select(b)
##s2.select_by_value("france")
##s2.select_by_value("germany")
##s2.select_by_value("canada")
##var2=s2.first_selected_option
##print(var2.text)

driver.quit()
