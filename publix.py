
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

class User :

    def __init__(self, username, password) :
        self.username = username 
        self.password = password
        
        options = webdriver.ChromeOptions() 
        options.add_argument("--no-sandbox")
        options.add_argument('--headless=new')
        options.add_argument('--disable-dev-shm-usage') 
        options.add_argument('--remote-debugging-pipe') 

        driver = webdriver.Chrome(options=options)
        
        driver.get("https://www.publix.org") 
        
        print('logging in')

        def waitUntilVis(contentType, value) :
            while True :

                if len(driver.find_elements(contentType, value)) > 0 :
                    break

        # go to login page
        waitUntilVis(By.XPATH, "/html/body/main/div[4]/div/div/form/button")
        driver.find_element(By.XPATH, "/html/body/main/div[4]/div/div/form/button").click()

        #login
        waitUntilVis(By.ID, "i0116") 
        driver.find_element(By.ID, "i0116").send_keys(username)
        driver.find_element(By.ID, "idSIButton9").click() 
        
        print("username")
        
        time.sleep(2)
        waitUntilVis(By.ID, "i0118")
        driver.find_element(By.ID, "i0118").send_keys(password)
        
        waitUntilVis(By.ID, "idSIButton9")
        driver.find_element(By.ID, 'idSIButton9').click()
        
        print("password")

        waitUntilVis(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div")
        
        driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div").click()

        # 2FA 
        authcode = input("Enter Code Recieved by SMS: ")
        
        waitUntilVis(By.ID,  "idTxtBx_SAOTCC_OTC")
        driver.find_element(By.ID, "idTxtBx_SAOTCC_OTC").send_keys(authcode)  
        driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()
       
        self.driver = driver
        
        self.waitUntilVis(By.ID, "nav")


    def waitUntilVis(self, contentType, value) :
        while True :

            if len(self.driver.find_elements(contentType, value)) > 0 :
                break

    def close(self) :
        self.driver.close() 
   
    def getSchedule(self) :
        self.driver.get("https://www.publix.org/passport/scheduling/schedule")

        returnDic = {} 

        self.waitUntilVis(By.ID, "scheduledweek")
        
        while True :
            if len(self.driver.find_elements(By.XPATH, "/html/body/main/div[3]/div[1]/div/div[1]/div[3]/a/i")) < 1 :
                break

            week = self.driver.find_element(By.ID, "scheduledweek").text

            week = week.split("\n")[4:]
            
            week = [i for i in week if i != "Show details" and i != "Schedule change"]
            
            pointer = 1 

            while pointer < len(week) - 1 :
                returnDic[week[pointer - 1] + " " + week[pointer]] = week[pointer + 1]
                pointer += 3
            
            self.driver.find_element(By.XPATH, "/html/body/main/div[3]/div[1]/div/div[1]/div[3]/a/i").click()
            
            while True :

                if len(self.driver.find_elements(By.XPATH, "/html/body/div[10]")) > 0 :
                    continue

                else :
                    break

        self.driver.get("https://www.publix.org/passport")

        return returnDic


    def payStatementHistory(self) :
        
        self.driver.get("https://www.publix.org/passport/pay/statements")

        self.waitUntilVis(By.ID, "DataTables_Table_0") 

        data = self.driver.find_element(By.ID, "DataTables_Table_0") 
        
        data = data.text.replace("View", "").split("\n")

        data = [i for i in data if i != ""]

        self.driver.get("https://www.publix.org/passport")
        
        return data


