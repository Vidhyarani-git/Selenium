from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

#implicit wait
##driver.implicitly_wait(60)
##
##driver.get("https://www.shoppersstack.com/products_page/51")
##driver.find_element("xpath","//input[@id='Check Delivery']").send_keys("636015")
##driver.find_element("xpath","//button[@id='Check']").click()

driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element("id","country")
driver.find_element("xpath","(//div[@class='form-group'])[6]")
driver.find_element("xpath","(//div[@class='form-group'])[7]")

#explicit wait
##driver.implicitly_wait(100)  
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##
##driver.get("https://www.shoppersstack.com/products_page/51")
##driver.find_element("xpath","//input[@id='Check Delivery']").send_keys("636015")
##a=driver.find_element("xpath","//button[@id='Check']")
##obj=WebDriverWait(driver,40)
##obj.until(EC.element_to_be_clickable(a))
##a.click()
##sleep(4)

##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##
##driver.get("https://demowebshop.tricentis.com")
##sleep(4)
##driver.find_element("xpath","//a[.='Twitter']").click()
##a=driver.window_handles
##driver.switch_to.window(a[1])
##obj=WebDriverWait(driver,80)
##obj.until(EC.title_is("nopCommerce (@nopCommerce) / X"))  #provide title of page
##print(driver.title)

#Fluent wait
##driver.implicitly_wait(100)  
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##
##driver.get("https://www.shoppersstack.com/products_page/51")
##driver.find_element("xpath","//input[@id='Check Delivery']").send_keys("636015")
##a=driver.find_element("xpath","//button[@id='Check']")
##obj=WebDriverWait(driver,40,0.3)
##obj.until(EC.element_to_be_clickable(a))
##a.click()
##sleep(4)

driver.quit()

