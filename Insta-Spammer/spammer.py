#script.py
#EDITED BY KLSIY 
#SOCIALS instagram.com/klsiy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randit
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

        #opening instagram.com
        browser.set_window_size(1024, 600)
        browser.maximize_window()
        sleep(6)
        browser.get('https://www.instagram.com/klsiy/') #change id to your 
       
    def following(self):
        browser = self.browser
        browser.implicitly_wait(5)

        # following begins here
        Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']")

        Follow_Button.click() 
        time.sleep(1)
        
        #SPAMS BEGIN RIGHT HERE
    def spamming(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #-------spamming begins
        #click message buttom
        browser.find_element_by_xpath("//button[@type='button']").click()
       
       
        #input random messages 100 times   
        message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_area.click()
        message_area.send_keys("{comments}", Keys.ENTER)
        for _ in range(0, self.number):
            message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
            message_area.click()
            message_area.send_keys(jokes.get_msg(), Keys.ENTER)

        browser.close()



if __name__ == '__main__':
        Instagram_Spam_Bot = InstaScript('YOUR ID', 'PASSWORD', 'VICTIM ID', NMBR OF MESSAGE COUNT)
        Instagram_Spam_Bot.spamming()