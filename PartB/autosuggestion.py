#for chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Inspectable auto suggestion
##driver.get("https://www.amazon.com/")
##time.sleep(4)
##driver.find_element("css selector","input#twotabsearchtextbox").send_keys("earbuds")
##time.sleep(2)

##a=driver.find_elements("xpath","//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
##for i in a:
##  print(i.text)


##a=driver.find_element("xpath","(//div[@class='s-suggestion s-suggestion-ellipsis-direction'])[4]").click()


#non inspectable auto suggestion
##driver.get("https://www.flipkart.com")
##time.sleep(4)
##driver.find_element("xpath","//span[@class='b3wTlE']").click()
##time.sleep(4)
##driver.find_element("xpath","//input[@class='nw1UBF v1zwn25']").send_keys("iphone")
##time.sleep(2)
##a=driver.find_elements("xpath","//div[@class='B8i0s_']")
####a.click()
####print(a)
##for i in a:
##  print(i.text)



# task:-
# open https://www.zepto.com/
# type chocolate and print all the auto suggestions it is displaying
driver.get("https://www.zepto.com/")
time.sleep(4)
driver.find_element("xpath","//a[@class='relative flex items-center gap-x-4 overflow-hidden rounded-lg border bg-white px-4 py-3']").click()
time.sleep(4)
driver.find_element("xpath","//input[@class='flex-1 outline-none']").send_keys("chocolate")
time.sleep(4)
a=driver.find_elements("xpath","//li[@role='option']")
for i in a:
  print(i.text)









driver.quit()
