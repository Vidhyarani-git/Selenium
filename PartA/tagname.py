from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

service=Service("C:\\Users\\Saravanan\\msedgedriver.exe")

options=Options()

driver=webdriver.Edge(service=service,options=options)

#tag name(same tag name for multiple elements we can used to locate the element for find_elements and using index for sending the data on those elements)
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
time.sleep(2)
a=driver.find_elements("tag name","input")
a[0].send_keys("vidhya")
a[1].send_keys("vidhya@gmail.com")
a[2].send_keys("123456")


driver.quit()
