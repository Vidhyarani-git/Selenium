
#for chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#for edge browser
##from selenium import webdriver
##from selenium.webdriver.chrome.service import Service
##from selenium.webdriver.edge.options import Options
##import time
##service=Service("C:\\Users\\Saravanan\\msedgedriver.exe")
##options=Options()
##driver=webdriver.Edge(service=service,options=options)

#submit() method-syntax:webelement.submit()
##driver.get("https://www.google.com")
##time.sleep(3)
##a=driver.find_element("css selector","input.truncate")
##time.sleep(2)
##a.sendkeys("python selenium")
##time.sleep(2)
##a.submit()

##driver.get("https://www.amazon.com")
##time.sleep(2)
##a=driver.find_element("css selector","input#twotabsearchtextbox")
##a.send_keys("handbags")
##a.submit()

#clear() method-syntax:webelement.clear()
driver.get("https://demo.vtiger.com/vtigercrm/index.php")
time.sleep(2)
a=driver.find_element("id","username")
a.clear()
b=driver.find_element("id","password")
b.clear()
time.sleep(2)
a.send_keys("vidhya")
time.sleep(2)
b.send_keys("Test@123")
time.sleep(2)

#is_displayed and is_enabled methods-
#syntax:webelement.is_displayed()
#syntax:webelement.is_enabled()
##driver.get("https://www.instagram.com")
##time.sleep(2)
##driver.find_element("name","email").send_keys("vidhya")
##time.sleep(2)
##driver.find_element("name","pass").send_keys("1234")
##time.sleep(2)
##a=driver.find_element("xpath","(//div[@role='button'])[2]")
##a.click()
##time.sleep(2)
##print(a.is_displayed())
##print(a.is_enabled())

#is_selected method-syntax:webelement.is_selected()
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("xpath","(//input[@class='form-check-input'])[2]")
##a.click()
##time.sleep(2)
##print(a.is_selected())
##b=driver.find_element("xpath","(//input[@class='form-check-input'])[1]")
####b.click()
##time.sleep(10)
##print(b.is_selected())

#get_attribute()-syntax:webelement.get_attribute("attribute_name")
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","button.start")
##print(a.get_attribute("class"))
##b=driver.find_element("css selector","button#alertBtn")
##print(b.get_attribute("id"))
##c=driver.find_element("css selector","button#confirmBtn")
##print(c.get_attribute("id"))
##d=driver.find_element("css selector","button#promptBtn")
##print(d.get_attribute("id"))

#size method-syntax:webelement.size
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","button.start")
##print(a.size)

#location method-syntax:webelement.location
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","button.start")
##print(a.location)

#rect method-syntax:webelement.rect
##driver.get("https://testautomationpractice.blogspot.com/")
##time.sleep(2)
##a=driver.find_element("css selector","button.start")
##print(a.rect)


driver.quit()
