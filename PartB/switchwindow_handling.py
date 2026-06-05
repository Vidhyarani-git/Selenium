from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from selenium.webdriver.common.action_chains import ActionChains
obj=ActionChains(driver)

driver.maximize_window()
sleep(2)

##driver.get("https://www.flipkart.com")
##sleep(4)
##driver.find_element("xpath","//span[@class='b3wTlE']").click()
##sleep(4)
##driver.find_element("xpath","(//input[@class='nw1UBF v1zwn25'])[1]").send_keys("iphone")
##driver.find_element("xpath","(//button[@class='XFwMiH'])[1]").click()
##sleep(2)
##driver.find_element("xpath","//div[@class='RG5Slk']").click()
##sleep(3)
##a=driver.window_handles
##driver.switch_to.window(a[1])
##sleep(2)
##driver.find_element("xpath","//div[contains(text(),'Buy now')]").click()
##sleep(5)
##driver.find_element("xpath","//input[@class='jwCbxy']").send_keys("7448758616")
##sleep(2)
##driver.find_element("xpath","//button[.='Continue']").click()
##sleep(4)

driver.get("https://www.nykaa.com/")
sleep(4)
a=driver.find_element("xpath","//input[@class='css-1upamjb']")
a.send_keys("sunscreen")
a.submit()
sleep(6)
s=driver.find_element("xpath","(//div[@class='css-1rd7vky'])[2]")
obj.scroll_to_element(s).perform()
sleep(6)
driver.find_element("xpath","(//button[.='Preview Size'])[2]")
sleep(3)
driver.find_element("xpath","//div[@class='css-3due47']").click()
sleep(3)
a=driver.window_handles
driver.switch_to.window(a[1])
sleep(3)
c=driver.find_element("xpath","(//button[@class=' css-13zjqg6'])[1]")
obj.move_to_element(c).perform()
sleep(3)
driver.find_element("css selector","button#header-bag-icon").click()
sleep(4)
d=driver.find_element("xpath","//div[@class='css-1wwsa40']")
print("Total: ",d.text)
sleep(4)








driver.quit()
