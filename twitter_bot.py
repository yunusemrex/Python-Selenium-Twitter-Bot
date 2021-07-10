from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.keys import Keys
from twitteruserinfo import username, password
import time

"""
    This is a twitter bot that allows you to do automate a variety of basic twitter tasks. 
    1 - Auto Login With Your @userame and password
    2 - Shows Followed Profiles
    3 - Shows Profiles of Your Followers
    4 - Auto Unfollow
    5 - Auto Tweet
    6 - Log Out
"""

class Twitter:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def LogIn(self):
        self.browser.get('https://twitter.com/login')
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
        btnSubmit.click()
        time.sleep(2)

    def LogOut(self):
        LogOut = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[2]/div/div")
        LogOut.click()
        time.sleep(2)
        LogOut2 = self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]")
        LogOut2.click()
        LogOut3 = self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]")
        LogOut3.click()
    
    def Show_Following(self):
        self.browser.get(f'https://twitter.com/{username}')
        time.sleep(3)
        FollowingList = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a")
        FollowingList.click()
        time.sleep(3)

    def Show_Followers(self):
        self.browser.get(f'https://twitter.com/{username}')
        time.sleep(3)
        FollowersList = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a")
        FollowersList.click()
        time.sleep(3)


    def Unfollow(self):
        unfollow = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div/div[2]/div")
        unfollow.click()
        time.sleep(3)
        unfollowButton = self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]")
        unfollowButton.click()
        time.sleep(2)
        

    def Scroll(self):
        LoopCounter = 0
        last_height =  self.browser.execute_script("return document.documentElement.scrollHeight")

        while True:            
            if LoopCounter > 10:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(3)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            LoopCounter += 1

    def TweetDraft(self):
        tweet = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        tweet.click()
        

    def TweetSomething(self):
        TweetSomething = self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div")
        TweetSomething.send_keys("""Hello World!""")
        Send_Tweet = self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
        Send_Tweet.click()




twitter = Twitter(username,password)

# twitter.LogIn()
# twitter.LogOut()
# twitter.Show_Following()
# twitter.Show_Followers()
# twitter.Unfollow()
# twitter.TweetDraft()
# twitter.TweetSomething()
# twitter.Scroll()
