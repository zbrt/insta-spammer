#script.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import jokes

class InstaScript:
    def __init__(self, username, password, victim_username, number):
        self.username = username
        self.password = password
        self.victim_username = victim_username
        self.number = number
        self.browser = webdriver.Firefox()

    def login(self):

        browser = self.browser
        browser.implicitly_wait(5)
        browser.set_window_size(1024, 600)
        browser.maximize_window()
        #opening instagram.com
        browser.get('https://www.instagram.com/')

         #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        browser = self.browser

        browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        #findind login button and clicking it
        browser.find_element_by_xpath("//button[@type='submit']").click()
        #-------login process ends 
        sleep(5)

    def new(self):
        
        browser = self.browser
        browser.get("https://www.instagram.com/klsiy") 
       

#
    #def accountfind(self):
        #browser = self.browser
       # browser.navigate().to("https://www.instagram.com/klsiy") 
       # sleep(3)       
   
    def follow(self):
        browser = self.browser
        
        #followbutton
        followbutton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/div/div/a/button")                                
        followbutton.click()                                        
        time.sleep(1)

    def messagenew(self):
        browser = self.browser

       #Now comes the part i was struglig on

        browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button").click()

    def notnow(self):
        browser = self.browser

        #Now Not now touching this aslo
        browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()   
            
    def spamming(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #-------spamming begins
        #click message buttom
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").click()
        #input random messages 100 times
        message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_area.click()
        message_area.send_keys("YOUR A GAY LOLLLLLLLLL", Keys.ENTER)
        for _ in range(0, self.number):
            message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
            message_area.click()
            message_area.send_keys(jokes.get_msg(), Keys.ENTER)

        browser.close()



if __name__ == '__main__':
        Instagram_Spam_Bot = InstaScript('bugfinder_', 'Oggysir@123', 'klsiy', 95)
        Instagram_Spam_Bot.login()
        Instagram_Spam_Bot.new()
        Instagram_Spam_Bot.messagenew()
        Instagram_Spam_Bot.notnow()
        Instagram_Spam_Bot.spamming()