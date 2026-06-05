from selenium.webdriver import Chrome,ChromeOptions
obj=ChromeOptions()
obj.add_experimental_option("detach",True)
driver=Chrome(obj)
from time import sleep

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

#print table name
# header=driver.find_element("xpath","//table[@name='BookTable']//tr[1]")
# print(header.text)
#
# #print total no of rows and columns
# rowscount=len(driver.find_elements("xpath","//table[@name='BookTable']//tr"))
# columnscount=len(driver.find_elements("xpath","//table[@name='BookTable']//th"))
# print("Total no of rows: ",rowscount)
# print("Total no of columns: ",columnscount)

td_tags=driver.find_elements("xpath","//table[@name='BookTable']//td")
for td in td_tags:
   print(td.text)

# noofRows=7
# noofColumns=4
# for row in range(2,noofRows+1):
#    for col in range(1,noofColumns+1):
#        print(driver.find_element("xpath",f"//table[@name='BookTable']//tr[{row}]/td[{col}]").text,end='  ')
# sleep(3)


#print book of amit
# noofRows=7
# for row in range(2,noofRows+1):
#     if driver.find_element("xpath",f"//table[@name='BookTable']//tr[{row}]/td[2]").text.lower=='amit':
#         print(driver.find_element("xpath",f"//table[@name='BookTable']//tr[{row}]/td[1]").text,end='-')
# sleep(4)
driver.quit()
