from selenium.webdriver.common import keys
import selenium
from selenium import webdriver
from InstagramUserInfo import email,password
import time
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self,email,password):
        browser=webdriver.Chrome("C:\\chromedriver.exe")
        self.email=email
        self.password=password
        browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        emailInput=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput=browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
       
       
        emailInput.send_keys(email)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
        browser.get("https://www.instagram.com/enmuzkir/")
        time.sleep(2)
        fallowInput=browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
        fallowInput.click()
        time.sleep(4)
        dialog=browser.find_element_by_css_selector("div[role=dialog] ul")
        fallowerscount=len(dialog.find_elements_by_css_selector("li"))
        print(fallowerscount)
        action=webdriver.ActionChains(browser)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(3)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newcount=len(dialog.find_elements_by_css_selector("li"))
            if fallowerscount !=newcount:
                fallowerscount=newcount
                print(f"second count : {newcount}")
                time.sleep(1)
            else:
                break
        fallowers=dialog.find_elements_by_css_selector("li")
        fallowerList=[]
        for user in fallowers:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            print(link)
            fallowerList.append(link)
        with open("fallowers.text","w",encoding="UTF-8")as file:
            for item in fallowerList:
                file.write(item + "\n")
        
        time.sleep(22)
instgrm=Instagram(email,password)
