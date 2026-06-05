from selenium.webdriver import Chrome,ChromeOptions
obj=ChromeOptions()
obj.add_experimental_option("detach",True)
driver=Chrome(obj)
from time import sleep

#Perform actions import action chains is mandatory
from selenium.webdriver.common.action_chains import ActionChains
obj2=ActionChains(driver)

#Perform keyboard actions import keys class is mandatory
from selenium.webdriver.common.keys import Keys

#mouse actions-click() method
##driver.get("https://www.google.com")
##sleep(4)
##b=driver.find_element("xpath","(//a[@class='MV3Tnb'])[1]")
##obj2.click(b).perform()
##print("About page opened")

#mouse actions-double_click() method
##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(4)
##b=driver.find_element("xpath","//button[.='Copy Text']")
##obj2.double_click(b).perform()
##sleep(4)
##print("Double click button pass")

#mouse actions-context_click() method
##driver.get("https://demoqa.com/buttons")
##sleep(4)
##b=driver.find_element("css selector","button#rightClickBtn")
##obj2.context_click(b).perform()
##sleep(4)
##print("Right click button pass")

#mouse actions-move_to_element() method
##driver.get("https://www.myntra.com/")
##sleep(4)
##b=driver.find_element("xpath","//a[@class='desktop-main']")
##c=obj2.move_to_element(b).perform()
##sleep(4)
##print("mouse hovering element pass")

#mouse actions-click_and_hold(),pause(),release() methods
##driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
##sleep(4)
##driver.find_element("xpath","//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
##sleep(2)
##driver.find_element("css selector","input#password").send_keys("12345")
##sleep(6)
##b=driver.find_element("xpath","(//img[@class='ng-star-inserted'])[1]")
##obj2.click_and_hold(b).pause(5).release().perform()
##sleep(6)

#mouse actions-drag_and_drop() method
##driver.get("https://demoqa.com/droppable")
##sleep(3)
##source=driver.find_element("css selector","div#draggable")
##destination=driver.find_element("css selector","div#droppable")
##sleep(4)
##obj2.drag_and_drop(source,destination).perform()
##sleep(8)
##driver.quit()

##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(3)
##a=driver.find_element("xpath","//p[.='Drag me to my target']")
##b=driver.find_element("id","droppable")
##sleep(4)
##obj2.drag_and_drop(a,b).perform()
##sleep(4)

#mouse actions- send_keys() method
##driver.get("https://www.bigbasket.com/")
##sleep(4)
##driver.find_element("xpath","(//input[@class='flex-1 w-full leading-md lg:text-sm xl:text-md placeholder-silverSurfer-700'])[2]").click()
##obj2.send_keys("dove soap").perform()
##sleep(6)

#mouse actions-send_keys_to_element() method
##driver.get("https://www.bigbasket.com/")
##sleep(4)
##a=driver.find_element("xpath","(//input[@class='flex-1 w-full leading-md lg:text-sm xl:text-md placeholder-silverSurfer-700'])[2]")
##obj2.send_keys_to_element(a,"sunscreen").perform()
##sleep(6)

#mouse actions-scroll_to_element() method
##driver.get("https://www.bigbasket.com/")
##sleep(4)
##a=driver.find_element("xpath","//a[.='About Us']")
##sleep(6)
##obj2.scroll_to_element(a).perform()
##sleep(8)

##driver.get("https://www.amazon.com/")
##sleep(4)
##b=driver.find_element("xpath","//a[.='Sell products on Amazon']")
##sleep(2)
##obj2.scroll_to_element(b).perform()
##sleep(4)

#--------keyboard actions------------------
# driver.get("https://www.google.com")
# sleep(2)
# driver.find_element("xpath","//textarea[@class='gLFyf']")
# sleep(4)
# obj2.key_down(Keys.SHIFT).send_keys('vidhyaraniaravinda').key_up(Keys.SHIFT).perform()
# sleep(2)
# obj2.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(2)
# obj2.key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
# sleep(8)

# driver.get("https://www.facebook.com")
# sleep(2)
# b=driver.find_element("xpath","//a[contains(text(),'Meta Store')]")
# sleep(2)
# #b.send_keys(Keys.PAGE_DOWN)
# b.send_keys(Keys.ARROW_DOWN)
# sleep(2)
# b.send_keys(Keys.ARROW_UP)
# sleep(4)

# driver.get("https://www.google.com/")
# sleep(2)
# b=driver.find_element("xpath","//textarea[@class='gLFyf']")
# sleep(2)
# b.send_keys("python selenium")
# sleep(2)
# b.send_keys(Keys.ENTER)
# sleep(20)

# driver.get("https://www.amazon.com")
# sleep(5)
# b=driver.find_element("xpath","//a[contains(text(),'Privacy Notice')]")
# sleep(3)
# b.send_keys(Keys.PAGE_DOWN)
# sleep(3)
# c=driver.find_element("id","twotabsearchtextbox")
# c.send_keys(Keys.PAGE_UP)
# sleep(5)

driver.get("https://www.amazon.com")
sleep(5)
b=driver.find_element("id","twotabsearchtextbox")
sleep(2)
b.send_keys(Keys.TAB)
sleep(5)

driver.quit()
