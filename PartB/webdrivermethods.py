from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
#get method
##driver.get("https://www.myntra.com/")
##sleep(4)
#window_handles
##a=driver.window_handles
##sleep(4)
##print(a)
#current_window_handles
##print(driver.current_window_handle)
#switch_to.window
##driver.switch_to.window(a[3])
##sleep(4)
##driver.get("https://www.zepto.com/")
##sleep(4)
##print(driver.title)
##driver.switch_to.window(a[2])
##sleep(4)
##driver.get("https://www.blinkit.com/")
##sleep(4)
##driver.switch_to.window(a[1])
##sleep(4)
##driver.get("https://www.bigbasket.com/")
##sleep(4)

#Store the parent window handle and:
##open a child window
##capture text from it
##close it
##return to the parent window
##driver.get("https://www.myntra.com")
##sleep(4)
##a=driver.window_handles
##driver.switch_to.window(a[1])
##sleep(4)
##driver.get("https://www.instamart.com")
##sleep(4)
##print(driver.title)
##driver.close()
##sleep(4)

##Open multiple tabs and print all window titles.
##driver.get("https://www.instamart.com")
##sleep(4)
##a=driver.window_handles
##print(driver.title)
##driver.switch_to.window(a[3])
##driver.get("https://www.bigbasket.com")
##print(driver.title)
##sleep(4)
##driver.switch_to.window(a[2])
##driver.get("https://www.jiomart.com")
##print(driver.title)
##sleep(4)
##driver.switch_to.window(a[1])
##driver.get("https://www.blinkit.com")
##print(driver.title)
##sleep(8)

##Write a script to:
##Open Amazon
##Search for a product
##Open the product in a new tab
##Switch to the new tab
##Print the product title
##Close the tab
##Return to the main tab
driver.get("https://www.amazon.com")
sleep(6)
driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("handbags")
sleep(6)
driver.find_element("css selector","input#nav-search-submit-button").click()
sleep(6)
a=driver.window_handles
driver.switch_to.window(a[1])
driver.find_element("xpath","(//span[contains(text(),'LOVEVOOK')])[1]").click()
driver.get("https://www.amazon.com/Handbags-Removable-Closure-Crossbody-Shoulder/dp/B09B55CXRQ/ref=sr_1_1_sspa?crid=1OWXJ8748VQXS&dib=eyJ2IjoiMSJ9.inhamTzcYHDP93tT3Wy8soGkY388C2gJR3yuuqXLvM-pp4d2jChX8YqPei2kcNcdDS2O38tNBdPPmExIE7fZrCCUU0zHudGNjjXNdgaBnRXMaFte1A064Ll9h2wKpQdvbHjB3zh9croFFL3igbokIB42CjDu99Tl2exZ7B5hvK1CmKZyfYJMI-IcULgHthIp9eRQMD6foBXdmUBTpALKZ6lp0W6PSqaT6iYTd44rAbjMthUzV10dt1F_nETi-zuJPqRJKR3HvQ0Z8TMFoHzpsguJq8ivfp2HZ9mg3c04Ch4.-hZLhlo3d8lFMIx3eAMSIYZw7iP-sn9D77uM4ZCcEA0&dib_tag=se&keywords=handbags&qid=1778158413&sprefix=handbags%2Caps%2C432&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
print(driver.title)
sleep(6)
driver.close()
sleep(4)









#-----switch_to.new_window
##driver.get("https://www.myntra.com/")
##sleep(4)
##driver.switch_to.new_window('tab')
##sleep(4)
##driver.get("https://www.ajio.com/")
##sleep(4)
##driver.switch_to.new_window('window')
##sleep(2)
##driver.get("https://www.amazon.com/")
##sleep(6)



driver.quit()
