#for chrome browser
##from selenium import webdriver
##from selenium.webdriver.chrome.service import Service
##from webdriver_manager.chrome import ChromeDriverManager
##import time
##driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#for edge browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options
import time
service=Service("C:\\Users\\Saravanan\\msedgedriver.exe")
options=Options()
driver=webdriver.Edge(service=service,options=options)

#--tagname#id locator
# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)
# driver.find_element("css selector","input#gender-female").click()
# time.sleep(2)
# driver.find_element("css selector","input#FirstName").send_keys("abc")
# time.sleep(2)
# driver.find_element("css selector","input#LastName").send_keys("def")
# time.sleep(2)
# driver.find_element("css selector","input#Email").send_keys("testemail@gmail.com")
# time.sleep(2)
# driver.find_element("css selector","input#Password").send_keys("123456")
# time.sleep(2)
# driver.find_element("css selector","input#ConfirmPassword").send_keys("123456")
# time.sleep(2)
# driver.find_element("css selector","input#register-button").click()
# time.sleep(2)

#--tagname.class locator
#driver.get("https://saucedemo.com/")
#time.sleep(5)
#elements=driver.find_elements("css selector","input.input_error.form_input")
#time.sleep(4)
#elements[0].send_keys("standard_user")
#time.sleep(2)
#elements[1].send_keys("secret_sauce")
#time.sleep(2)
#driver.find_element("css selector","input.submit-button.btn_action").click()
#time.sleep(4)

#--xpath locator
#absolute xpath
#driver.get("https://demowebshop.tricentis.com/register")
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[1]/div[2]/input").click()
#time.sleep(2)
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/input").send_keys("vidhya")
#time.sleep(2)
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/input").send_keys("rani")
#time.sleep(2)
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/input").send_keys("vidhyarani@gmail.com")
#time.sleep(2)
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[1]/input").send_keys("123456")
#time.sleep(2)
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/input").send_keys("123456")
#time.sleep(2)
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[4]/input").click()
#time.sleep(4)

#Relative xpath- basic xpath- xpath with attribute
#driver.get("https://www.saucedemo.com/")
#time.sleep(2)
#driver.find_element("xpath","//input[@autocorrect='off']").send_keys("standard_user")
#time.sleep(2)
#driver.find_element("xpath","(//input[@autocorrect='off'])[2]").send_keys("secret_sauce")
#time.sleep(2)

#relative xpath-basic xpath- xpath with attribute
#driver.get("https://testautomationpractice.blogspot.com/")
#driver.find_element("xpath","(//input[@class='form-control'])[1]").send_keys("vidhya")
#time.sleep(2)
#driver.find_element("xpath","(//input[@class='form-control'])[2]").send_keys("vidhya@gmail.com")
#time.sleep(2)
#driver.find_element("xpath","(//input[@class='form-control'])[3]").send_keys("9876543210")
#time.sleep(2)
#driver.find_element("xpath","//textarea[@class='form-control']").send_keys("test street")
#time.sleep(2)
#driver.find_element("xpath","(//input[@class='form-check-input'])[2]").click()
#time.sleep(2)
#driver.find_element("xpath","(//input[@type='checkbox'])[1]").click()
#time.sleep(2)
#driver.find_element("xpath","(//input[@type='checkbox'])[2]").click()
#time.sleep(2)

#relative xpath-basic xpath- xpath with text
#driver.get("https://www.facebook.com/")
#driver.find_element("xpath","//span[text()='Create new account']").click()
#time.sleep(2)
#driver.find_element("xpath","(//a[text()='Privacy Policy'])[1]").click()
#time.sleep(10)

#relative xpath-basic xpath- xpath with contains text()
#syntax://tagname[contains(text(),'partial attribute value')]
#driver.get("https://www.amazon.com/")
#time.sleep(2)
#driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
#time.sleep(1)
#driver.find_element("id","nav-search-submit-button").click()
#time.sleep(2)
#driver.find_element("xpath","(//span[contains(text(),'Apple iPhone 17 Pro,')])[1]").click()
#time.sleep(3)

#relative xpath-basic xpath- xpath with contains attribute
#syntax://tagname[contains(@attribute,'partial attribute value')]
#driver.get("https://www.instagram.com/")
#time.sleep(1)
#driver.find_element("xpath","//input[contains(@class,'xggy1nq')]").send_keys("test")
#time.sleep(2)
#driver.find_element("xpath","(//input[contains(@class,'xggy1nq')])[2]").send_keys("12345")
#time.sleep(2)

#if thr are spaces in starting or ending we use contains()
#contains with text()
#driver.get("https://demowebshop.tricentis.com/")
#time.sleep(4)
#driver.find_element("xpath","(//a[contains(text(),'Books')])[3]").click()
#time.sleep(4)

#advance xpath-traversing
#driver.get("https://www.amazon.com")
#time.sleep(8)
#driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
#driver.find_element("id","nav-search-submit-button").click()
#a=driver.find_element("xpath","//span[.='Apple iPhone 16 Pro Max, 512GB, Black Titanium - Unlocked (Renewed)']")
#print(a.text)
#time.sleep(5)
#b=driver.find_element("xpath","//span[.='Apple iPhone 16 Pro Max, 512GB, Black Titanium - Unlocked (Renewed)']/../../../../..//span[@class='a-price-whole']")
#print(b.text)
#c=driver.find_element("xpath","//span[.='Apple iPhone 16 Pro Max, 512GB, Black Titanium - Unlocked (Renewed)']/../../../..//span[@class='a-size-small a-color-base']")
#print(c.text)

#driver.get("https://www.flipkart.com")
#time.sleep(5)
#driver.find_element("xpath","(//input[@class='nw1UBF v1zwn25'])[1]").send_keys("iphone")
#driver.find_element("xpath","(//button[@class='XFwMiH'])[1]").click()
#time.sleep(2)
#a=driver.find_element("xpath","//div[.='Apple iPhone 17 Pro (Silver, 256 GB)']")
#print(a.text)
##b=driver.find_element("xpath","//div[.='Apple iPhone 17 Pro (Silver, 256 GB)']/../..//div[@class='hZ3P6w DeU9vF']")
#b=driver.find_element("xpath","//div[.='Apple iPhone 17 Pro (Silver, 256 GB)']/../..//div[@class='hZ3P6w DeU9vF']/../../../..//div[@class='col col-7-12']")
#print(b.text)

#advance xpath-xpath with axes
#parent-child relation
##driver.get("https://www.amazon.com")
##time.sleep(8)
##driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
##driver.find_element("id","nav-search-submit-button").click()
##time.sleep(2)
##a=driver.find_element("xpath","//span[.='Apple iPhone 16 Pro Max, 512GB, Black Titanium - Unlocked (Renewed)']/parent::h2/parent::a/parent::div/parent::div//span[@class='a-price-whole']")
##print(a.text)

#using ancestor and descendent
driver.get("https://www.flipkart.com/")
time.sleep(4)
driver.find_element("xpath","(//input[@class='nw1UBF v1zwn25'])[1]").send_keys("laptop")
driver.find_element("xpath","(//button[@class='XFwMiH'])[1]").click()
time.sleep(8)
# product=driver.find_element("xpath","//div[.='ASUS Vivobook 15 (2025) with Office 2024 + M365 Basic* Intel Core i3 13th Gen - (8 GB/512 GB SSD/Windo...']")
# print(product.text)
# price=driver.find_element("xpath","//div[.='ASUS Vivobook 15 (2025) with Office 2024 + M365 Basic* Intel Core i3 13th Gen - (8 GB/512 GB SSD/Windo...']/ancestor::div[@class='lvJbLV col-12-12']/descendant::div[@class='hZ3P6w DeU9vF']")
# print(price.text)

##rating=driver.find_element("xpath","//div[.='DELL 14 Microsoft Office Home 2024 Snapdragon X - (16 GB/512 GB SSD/Windows 11 Home) Inspiron 5441 Thi...']//ancestor::div[@class='lvJbLV col-12-12']//descendant::span[@id='productRating_LSTCOMHFSGXHHSXD7MFSS6YFV_COMHFSGXHHSXD7MF_']")
##print(rating.text)


#following-sibling
##driver.get("https://www.w3schools.com/html/html_tables.asp")
##time.sleep(5)
##a=driver.find_element("xpath","//td[.='Island Trading']//following-sibling::td")
##time.sleep(2)
##print(a.text)

#preceding-sibling
##driver.get("https://www.w3schools.com/html/html_tables.asp")
##time.sleep(5)
##a=driver.find_element("xpath","//td[.='Austria']/preceding-sibling::td[1]")
##time.sleep(2)
##print(a.text)



driver.quit()
