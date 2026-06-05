from excel_utilities import *

file=r"C:\Users\Saravanan\Desktop\selenium\PartC\Test_excel1.xlsx"

#write the datas in FD_calculator sheet
# writeData(file,"FD_calculator",1,1,"Amount")
# writeData(file,"FD_calculator",1,2,"Period")
# writeData(file,"FD_calculator",1,3,"Frequency")
# writeData(file,"FD_calculator",1,4,"Interest")
# writeData(file,"FD_calculator",1,5,"Expected EMI")
# writeData(file,"FD_calculator",1,6,"Expected Result")
# writeData(file,"FD_calculator",1,7,"Actual Result")
#
# writeData(file,"FD_calculator",2,1,"250000")
# writeData(file,"FD_calculator",2,2,"5")
# writeData(file,"FD_calculator",2,3,"Yearly")
# writeData(file,"FD_calculator",2,4,"10")
# writeData(file,"FD_calculator",2,5,"402628")
# writeData(file,"FD_calculator",2,6,"Pass")
#
# writeData(file,"FD_calculator",3,1,"500000")
# writeData(file,"FD_calculator",3,2,"7")
# writeData(file,"FD_calculator",3,3,"Yearly")
# writeData(file,"FD_calculator",3,4,"12")
# writeData(file,"FD_calculator",3,5,"1105341")
# writeData(file,"FD_calculator",3,6,"Fail")
#
# writeData(file,"FD_calculator",4,1,"1000000")
# writeData(file,"FD_calculator",4,2,"5")
# writeData(file,"FD_calculator",4,3,"Yearly")
# writeData(file,"FD_calculator",4,4,"7")
# writeData(file,"FD_calculator",4,5,"1402553")
# writeData(file,"FD_calculator",4,6,"Pass")
#
# writeData(file,"FD_calculator",5,1,"1500000")
# writeData(file,"FD_calculator",5,2,"6")
# writeData(file,"FD_calculator",5,3,"Yearly")
# writeData(file,"FD_calculator",5,4,"9")
# writeData(file,"FD_calculator",5,5,"2515650")
# writeData(file,"FD_calculator",5,6,"Pass")
#
# writeData(file,"FD_calculator",6,1,"4000000")
# writeData(file,"FD_calculator",6,2,"8")
# writeData(file,"FD_calculator",6,3,"Yearly")
# writeData(file,"FD_calculator",6,4,"10")
# writeData(file,"FD_calculator",6,5,"8574355")
# writeData(file,"FD_calculator",6,6,"Fail")

#change the font style
# fillFont(file,"FD_calculator")

#fill the yellow colors for header
# fillPattern(file,"FD_calculator",1,1)
# fillPattern(file,"FD_calculator",1,2)
# fillPattern(file,"FD_calculator",1,3)
# fillPattern(file,"FD_calculator",1,4)
# fillPattern(file,"FD_calculator",1,5)
# fillPattern(file,"FD_calculator",1,6)
# fillPattern(file,"FD_calculator",1,7)

#fill the colors for expected results column
# fillPattern(file,"FD_calculator",2,6,"Pass")

from selenium.webdriver import Edge,EdgeOptions
obj=EdgeOptions()
obj.add_experimental_option("detach",True)
driver=Edge(obj)
from time import sleep
from selenium.webdriver.support.select import Select

driver.implicitly_wait(30)

driver.get("https://www.sbisecurities.in/calculators/fd-calculator")
driver.maximize_window()
sleep(4)
for row in range(2,rowNum(file,"FD_calculator")+1):
    Principal = readData(file, "FD_calculator", row, 1)
    Period = readData(file, "FD_calculator", row, 2)
    Interest = readData(file, "FD_calculator", row, 4)
    Frequency = readData(file, "FD_calculator", row, 3)
    Expected_EMI= readData(file,"FD_calculator",row,5)

    driver.find_element("xpath", "//input[@name='fd_investment']").send_keys(Principal)
    driver.find_element("xpath", "(//input[@id='input_fd_investment'])[2]").send_keys(Period)
    driver.find_element("xpath", "//input[@id='input_interest']").send_keys(Interest)
    a = Select(driver.find_element("xpath", "//select[@id='frequency']"))
    a.select_by_visible_text("Yearly")
    sleep(4)
    b=driver.find_element("xpath","//button[@class='btn btn-primary']")
    b.click()
    amt=driver.find_element("xpath","//div[@class='container result-container']//span").text
    calculated_amt=amt.replace("₹","").replace(",","")
    if float(Expected_EMI)==float(calculated_amt):
        print(Principal, Period, Frequency, Interest,Expected_EMI,calculated_amt,"Pass")
        writeData(file,"FD_calculator",row,7,"Pass")
        fillPattern(file,"FD_calculator",row,7,"Pass")
    else:
        print(Principal, Period, Frequency, Interest,Expected_EMI,calculated_amt,"Fail")
        writeData(file,"FD_calculator",row,7,"Fail")
        fillPattern(file, "FD_calculator", row, 7, "Fail")

    driver.refresh()
driver.quit()