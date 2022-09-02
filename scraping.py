
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait(selector, value, time:int=20):
    WebDriverWait(driver,time).until(EC.presence_of_element_located((selector,value)))
def seperateString(aString):
    strList = aString.split(" ")
    if (len(strList) > 1):
        str = aString.replace(" ","+")
        return str
    else:
        return aString
def scrollPage(size):
    jscommand = """
    window.scrollTo(0, {});
    """.format(size)

    driver.execute_script(jscommand)



driver = webdriver.Chrome(executable_path=r"C:\Users\deniz\Downloads\chromedriver_win32\chromedriver.exe")



class Scraping:
    def __init__(self,itemName):
        self.driver = driver
        self.itemName = itemName
        self.searchForItem()
    def searchForItem(self):
        itemN = seperateString(self.itemName)
        self.driver.get("https://www.akakce.com/arama/?q=" + itemN)
        wait(By.XPATH,'//*[@id="APL"]/li[1]')
        self.driver.find_element(By.XPATH,'//*[@id="APL"]/li[1]/a/figure/img').click()
        sleep(3)
        self.verifySearched()
    def verifySearched(self):
        try:
            self.driver.find_element(By.XPATH,'//*[@id="DT_w"]')
            self.getPrices()
            self.getAttributes()
            self.getComments()
            self.getDeviceImg()
        # except:
        #     print("Cannot get device page, Plase try again later....")
        #     return
        finally:
            print("oh no")
    def getPrices(self):
        prices = self.driver.find_elements(By.XPATH,'//*[@id="PL"]/li')
        with open("project3/prices.txt","w") as file:
            i = 1
            for price in prices:
                price = self.driver.find_element(By.XPATH,'//*[@id="PL"]/li[{i}]//*[@class="pt_v8"]'.format(i = i)).text
                pricehrf = str(self.driver.find_element(By.XPATH,'//*[@id="PL"]/li[{i}]/a'.format(i = i)).get_attribute("href"))
                file.write(price + "_" + pricehrf + "\n")
                i += 1
    def getAttributes(self):
        attributes = self.driver.find_element(By.XPATH,'//*[@id="DT_w"]').text
        with open("project3/attributes.txt","w",encoding="UTF-8") as file:
            list = attributes.split("\n")
            for element in list:
                if element.endswith(":"):
                    element = element + " Var"
                file.write(element + "\n")

    def getComments(self):
        comments = self.driver.find_elements(By.XPATH,'//*[@id="UCL"]//*[@class="cm"]')
        with open("project3/comments.txt","w",encoding="UTF-8") as file:
            for com in comments:
                file.write(com.text + "\n") 
    def getDeviceImg(self):
        scrollPage(190)
        image = self.driver.find_element(By.XPATH,'//*[@id="PI_v8"]/a/img').screenshot_as_png
        with open('project3/static/filename.png', 'wb') as file:
            file.write(image)
    # def detailedAttributes(self):
    #     try:
    #         detailedAtt = self.driver.find_element(By.XPATH,"//div[@class='icSTw_v8 wbb_v8']").text
    #         with open("details.txt","w",encoding="UTF-8") as file:
    #             file.write(detailedAtt)
    #     except Exception:
    #         return "There is no more attribute...."
