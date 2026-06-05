from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
sleep(2)

##driver.get("https://vinothqaacademy.com/iframe/")
##sleep(3)
##
##driver.switch_to.frame(0)
##sleep(2)
##driver.find_element("css selector","input#nameInput").send_keys("john doe")
##sleep(3)
##
##driver.switch_to.parent_frame()
##
##driver.switch_to.frame(1)
##sleep(2)
##driver.find_element("xpath","//button[@name='promptalertbox1234']").click()
##sleep(4)
##
##driver.switch_to.parent_frame()
##
##driver.switch_to.frame(2)
##sleep(2)
##driver.find_element("name","vfb-5").send_keys("vidhya")
##sleep(6)
##
##driver.switch_to.parent_frame()
##
##driver.find_element("xpath","(//a[.='Home'])[2]").click()
##sleep(4)

driver.get("https://www.zomato.com/bangalore/delivery")
sleep(2)
driver.find_element("xpath","//a[.='Log in']").click()
sleep(6)
driver.find_element("xpath","//input[@class='sc-60vv3c-0 gmdLhr sc-fPXMVe iHUNmi']").send_keys("9876543210")
sleep(5)

driver.quit()
