#chrome browser
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--enable-notifications')
driver=Chrome(o)
from time import sleep


#edge browser
##from selenium import webdriver
##from selenium.webdriver.edge.service import Service
##from selenium.webdriver.edge.options import Options
##from time import sleep
##service=Service("C:\\Users\\Saravanan\\msedgedriver.exe")
##options=Options()
##driver=webdriver.Edge(service=service,options=options)

driver.maximize_window()
sleep(2)

#JS alert-simple alert
##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(4)
##driver.find_element("xpath","(//button[@id='alertBtn'])[1]").click()
##sleep(3)
##driver.switch_to.alert.accept()
##sleep(4)

#JS alert-confirmation alert
##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(4)
##driver.find_element("xpath","//button[@id='confirmBtn']").click()
##sleep(3)
##driver.switch_to.alert.accept()
##sleep(4)

##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(4)
##driver.find_element("xpath","//button[@id='confirmBtn']").click()
##sleep(3)
##driver.switch_to.alert.dismiss()
##sleep(4)

#--JS alert-prompt alert
# driver.get("https://testautomationpractice.blogspot.com/")
# sleep(4)
# driver.find_element("xpath","//button[@id='promptBtn']").click()
# sleep(3)
# a=driver.switch_to.alert
# a.send_keys("aravinda")
# sleep(3)
# a.accept()
# sleep(4)

##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(4)
##driver.find_element("xpath","//button[@id='promptBtn']").click()
##sleep(3)
##a=driver.switch_to.alert
##a.send_keys("aravinda")
##sleep(3)
##a.dismiss()
##sleep(4)

#--Notification popup
# driver.get("https://www.deccanherald.com/")
# sleep(6)
# driver.find_element("xpath","(//a[@class='menu-link p1dgL'])[1]").click()
##sleep(4)

##driver.get("https://www.irctc.co.in/nget/train-search")
##sleep(8)
##driver.find_element("xpath","//a[.=' CONTACT US ']").click()
##sleep(4)

#--Authentication popup-syntax:(https://username:password@url)
##driver.get("https://postman:password@postman-echo.com/basic-auth")
##sleep(6)

#--File upload-
#single file upload
##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(4)
##path="C:\\Users\\Saravanan\\Downloads\\actionchains.py"
##driver.find_element("id","singleFileInput").send_keys(path)
##sleep(4)
##driver.find_element("xpath","//button[.='Upload Single File']").click()
##sleep(10)

#multiple file upload
##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(4)
##path1="C:\\Users\\Saravanan\\Downloads\\actionchains.py"
##path2="C:\\Users\\Saravanan\\Desktop\\selenium\\switchwindow_handling.py"
##path3="C:\\Users\\Saravanan\\Desktop\\selenium\\locator.py"
##a=driver.find_element("id","multipleFilesInput")
##a.send_keys(path1)
##a.send_keys(path2)
##a.send_keys(path3)
##sleep(4)
##driver.find_element("xpath","//button[.='Upload Multiple Files']").click()
##sleep(10)

#hidden division
driver.get("https://mamaearth.in/")
sleep(4)
driver.find_element("id","wzrk-cancel-id").click()
sleep(2)
driver.find_element("xpath","//div[.='Login']").click()
sleep(4)
driver.find_element("xpath","//input[@name='contact']").send_keys("8867751528")
sleep(4)
driver.find_element("xpath","//button[.='Login with OTP']").click()
sleep(10)

#file download



driver.quit()
