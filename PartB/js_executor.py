from selenium.webdriver import Chrome,ChromeOptions
obj=ChromeOptions()
obj.add_experimental_option("detach",True)
driver=Chrome(obj)
from time import sleep

driver.maximize_window()
sleep(3)

#scrollBy() method:syntax-driver.execute_script("window.scrollBy(x,y);")
##driver.get("https://mamaearth.in/")
##sleep(4)
##driver.execute_script("window.scrollBy(0,10000);")
##sleep(6)
##driver.execute_script("window.scrollBy(0,-10000);")
##sleep(6)

#scrollTo() method:syntax-driver.execute_script("window.scrollTo(x,y);")
##driver.get("https://mamaearth.in/")
##sleep(4)
##driver.execute_script("window.scrollTo(0,10000);")
##sleep(4)
##driver.execute_script("window.scrollTo(0,200);")
##sleep(6)

driver.get("https://mamaearth.in/")
sleep(4)
driver.execute_script("window.scrollTo(0,0);")
sleep(4)

#scrollIntoView() method:syntax-driver.execute_script("argument[arg].scrollIntoView(true);",webelements)
##driver.get("https://www.bigbasket.com/")
##sleep(10)
##a=driver.find_element("xpath","//span[.='Home and Kitchen']") #webelement
##sleep(10)
##b=driver.find_element("xpath","//span[@class='Label-sc-15v1nk5-0 jnBJRV']")
##sleep(4)
##driver.execute_script("arguments[1].scrollIntoView(true);",a,b)
##sleep(8)

#combination of scrollBy,scrollTo and scrollIntoView methods
##driver.get("https://www.sierratec.com/")
##sleep(4)
##driver.execute_script("window.scrollBy(0,1000);")
##sleep(8)
##a=driver.find_element("xpath","//span[.='HR & Finance']")
##sleep(5)
##driver.execute_script("arguments[0].scrollIntoView(true);",a)
##sleep(10)
##driver.execute_script("window.scrollTo(0,1000);")
##sleep(10)

#scrollHeight method:syntax-driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#it scroll the page upto bottom
##driver.get("https://www.sierratec.com/")
##sleep(5)
##driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
##sleep(10)

driver.quit()
