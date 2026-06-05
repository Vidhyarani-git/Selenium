# TEST CASE: 1. Open the Browser.
# 2. Apply Implicit wait of 10s.
# 3. Open the application. ("https://testautomationpractice.blogspot.com/").
# 4. Enter Name, Email, Phone and Address.Apply explicit wait
# 5. Select Gender and Days (Monday, Tuesday, Wednesday, Thursday, Friday).
# 6. Select India from the dropdown with red and blue color from colors dropdown and select two animals as well from sorted list dropdown.
# 7. Perform Drag and Drop, Drag and Drop by Offset by sliding 50 pixels.
# 8. Close the Browser

from selenium.webdriver import Chrome,ChromeOptions
obj=ChromeOptions()
obj.add_experimental_option("detach",True)
driver=Chrome(obj)
from time import sleep

# 1. Open the Browser.
# 2. Apply Implicit wait of 10s.
# 3. Open the application. ("https://testautomationpractice.blogspot.com/").
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

# 4. Enter Name, Email, Phone and Address.Apply explicit wait
driver.implicitly_wait(10)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
obj1=WebDriverWait(driver,30)
# obj.until(EC.element_to_be_clickable(a))
a=driver.find_elements("xpath","//input[@class='form-control']")
a[0].send_keys("Vidhya")
a[1].send_keys("vidhya@gmail.com")
a[2].send_keys("9876543210")
driver.find_element("xpath","//textarea[@class='form-control']").send_keys("Salem,Tamil Nadu")

# 5. Select Gender and Days (Monday, Tuesday, Wednesday, Thursday, Friday).
b=driver.find_elements("xpath","//input[@class='form-check-input']")
b[1].click()
b[3].click()
b[4].click()
b[5].click()
b[6].click()
b[7].click()

# 6. Select India from the dropdown with red and blue color from colors dropdown and select two animals as well from sorted list dropdown. 7. Perform Drag and Drop, Drag and Drop by Offset by sliding 50 pixels.
from selenium.webdriver.support.select import Select
c=driver.find_elements("xpath","//select[@class='form-control']")
s1=Select(c[0])
s2=Select(c[1])
s3=Select(c[2])
s1.select_by_value("india")
s2.select_by_index(0)
s2.select_by_index(1)
s3.select_by_visible_text("Cheetah")
s3.select_by_visible_text("Deer")

# 7. Perform Drag and Drop, Drag and Drop by Offset by sliding 50 pixels.
from selenium.webdriver.common.action_chains import ActionChains
obj2=ActionChains(driver)
source=driver.find_element("xpath","//div[@id='draggable']")
destination=driver.find_element("xpath","//div[@id='droppable']")
obj2.drag_and_drop(source,destination).perform()
slider=driver.find_element("xpath","//div[@id='slider-range']/..//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
obj2.drag_and_drop_by_offset(slider,50,0).perform()
sleep(4)

# 8. Close the Browser
driver.close()