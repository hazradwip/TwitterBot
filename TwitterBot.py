from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time

class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()

    def Login(self):
        bot=self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)


ed=TwitterBot('')
ed.Login()


