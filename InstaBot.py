from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self, userName, Password):
        self.userName = userName
        self.Password = Password
        self.Browser = webdriver.Chrome("C:\chromedriver")
        self.Browser.get("https://www.instagram.com/")
        self.PicLinks = []
        time.sleep(6)

    def login(self):
        self.Browser.find_element_by_link_text("Log in").click()
        time.sleep(2)
        name = self.Browser.find_element_by_name("username")
        pas = self.Browser.find_element_by_name("password")
        name.send_keys(self.userName)
        pas.send_keys(self.Password)
        pas.send_keys(Keys.ENTER)
        time.sleep(2)
        self.Browser.find_element_by_css_selector(".HoLwm").click()


    def getLinks(self,InstaUserName):
        #Insta User Name of The person you want Like his or her Pics , it should be correct
        self.PicLinks = []
        self.Browser.get(f"https://www.instagram.com/{InstaUserName}")
        S = 6000
        ATag = self.Browser.find_elements_by_css_selector(".v1Nh3 > a")
        self.PicLinks = [hrfPic.get_attribute("href") for hrfPic in ATag]
        Old = self.PicLinks[-1]
        for i in range(300):
            self.Browser.execute_script(f"window.scrollTo(0,{S});")
            S += 6000
            time.sleep(3)
            ATag = self.Browser.find_elements_by_css_selector(".v1Nh3 > a")
            for hrfPic in ATag:
                if hrfPic.get_attribute("href") not in self.PicLinks:
                    self.PicLinks.append(hrfPic.get_attribute("href"))
            if Old != self.PicLinks[-1]:
                Old = self.PicLinks[-1]
            else:
                break

    def AutoLiker(self,NumberOfLikes):
        #Number of Likes = Number Pics you want Like Starting from the top
        n = 1
        for PicLink in self.PicLinks:
            self.Browser.get(PicLink)
            time.sleep(3)
            self.Browser.find_element_by_css_selector(".dCJp8").click()
            if n > NumberOfLikes:
                break
            else:
                n = n+1

UserName = input("UserName : ")
Password= input("Password : ")
Fa = InstaBot(UserName, Password)
#Your User Name and Password
Fa.login()
UserN1 = input("User You Want Like its Pics : ")
Num = input("How Many Likes : ")
Fa.getLinks(UserN1)
Fa.AutoLiker(int(Num))
