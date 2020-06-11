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
        email = bot.find_element_by_name('session[username_or_email]')
        pasword=bot.find_element_by_name('session[password]')
        email.clear()
        pasword.clear()
        email.send_keys(self.username)
        pasword.send_keys(self.password)
        pasword.send_keys(Keys.RETURN)
        time.sleep(3)


    def Auto_like(self,hashtag):
        bot=self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typeahead_click')
        time.sleep(3)
        for i in range(1,10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            tweets= bot.find_elements_by_id('tweet')
            links=[elem.get_atrribute('data-permalink-path')for elem in tweets]
            for link in links:
                bot.get('https://twitter.com'+link)
                try:
                    bot.find_elements_by_id('like').click()
                    time.sleep(2)
                except Exception as ex:
                    time.sleep(60)




ed=TwitterBot('your-Username','your-Password')
ed.Login()
ed.Auto_like('Hastag you want to search')


