from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#question 1
##driver.get("https://testautomationpractice.blogspot.com/")
##sleep(3)
##driver.find_element("xpath","(//input[@class='form-control'])[1]").send_keys("Vidhya")
##sleep(3)
##driver.find_element("xpath","(//input[@class='form-control'])[2]").send_keys("vidhya@gmail.com")
##sleep(3)
##driver.find_element("xpath","(//input[@class='form-control'])[3]").send_keys("9876543210")
##sleep(3)
##driver.find_element("xpath","//textarea[@class='form-control']").send_keys("GK layout Bengaluru")
##sleep(3)
##driver.find_element("xpath","//input[@id='female']").click()
##sleep(3)
##a=driver.find_elements("xpath","//input[@class='form-check-input']")
##a[2].click()
##a[3].click()
##a[4].click()
##a[5].click()
##a[6].click()
##a[7].click()
##a[8].click()
##driver.find_element("xpath","(//select[@class='form-control'])[1]/..//option[contains(text(),'India')]").click()
##sleep(2)
##driver.find_element("xpath","(//select[@class='form-control'])[2]/..//option[contains(text(),'Red')]").click()
##sleep(2)
##driver.find_element("xpath","(//select[@class='form-control'])[2]/..//option[contains(text(),'Blue')]").click()
##sleep(2)
##driver.find_element("xpath","(//select[@class='form-control'])[2]/..//option[contains(text(),'Green')]").click()
##sleep(3)
##a=driver.find_element("xpath","(//select[@class='form-control'])[3]")
##print("Sorted list options:\n",a.text)

#question 2
##driver.get("https://blinkit.com/")
##sleep(2)
##driver.find_element("name","select-locality").send_keys("Bengaluru")
##sleep(2)
##driver.find_element("xpath","(//div[@class='LocationSearchList__LocationListContainer-sc-93rfr7-0 lcVvPT'])[2]").click()
##sleep(2)
##driver.find_element("xpath","//div[@class='SearchBar__AnimationWrapper-sc-16lps2d-1 iJnYYS']").click()
##sleep(2)
##driver.find_element("xpath","//input[@class='SearchBarContainer__Input-sc-hl8pft-3 irVxjq']").send_keys("sunpure refined oil")
##sleep(2)
##driver.find_element("xpath","//input[@class='SearchBarContainer__Input-sc-hl8pft-3 irVxjq']/../../../../../..//div[@class='tw-mt-1 tw-flex tw-flex-col tw-justify-center']").click()
##sleep(2)
##driver.find_element("xpath","(//div[contains(text(),'ADD')])[1]").click()
##sleep(4)

#question 3
##driver.get("https://qaplayground.com/practice/dropdowns")
##sleep(2)
##driver.find_element("xpath","//button[@id='dropdown-fruit']").click()
##sleep(4)
##driver.find_element("xpath","//span[contains(text(),'Banana')]").click()
##sleep(6)

#question 4
##driver.get("https://demowebshop.tricentis.com/")
##sleep(2)
##driver.find_element("xpath","(//a[contains(text(),'Books')])[1]").click()
##sleep(2)
##driver.find_element("xpath","(//div[@class='item-box'])[3]").click()
##sleep(4)
##driver.find_element("id","add-to-cart-button-45").click()
##sleep(2)
##driver.find_element("xpath","//a[contains(text(),'shopping cart')]").click()
##sleep(2)
##driver.find_element("id","termsofservice").click()
##sleep(2)
##driver.find_element("id","checkout").click()
##sleep(6)

#question 5
driver.get("https://www.amazon.com/")
sleep(6)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
driver.find_element("css selector","input#nav-search-submit-button").click()
sleep(4)
a=driver.find_elements("xpath","//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")
print("List of iphone names: ")
for i in a:
    print(i.text)
sleep(4)


driver.quit()

