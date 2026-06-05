from selenium.webdriver import Chrome,ChromeOptions
obj=ChromeOptions()
obj.add_experimental_option("detach",True)
driver=Chrome(obj)
from time import sleep

driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()
print(driver.title)

#screenshot saved same folder
##sleep(5)
##driver.save_screenshot("screenshot1.png")

#screenshot saved different folder
##sleep(5)
##driver.save_screenshot(r"C:\Users\Saravanan\Desktop\screenshots\screenshot1.png")

#multiple screenshots
for i in range(1,11):
    sleep(6)
    driver.save_screenshot(rf"C:\Users\Saravanan\Desktop\screenshots\screenshot_{i}.png")
    
driver.quit()
