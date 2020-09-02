from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup as bs
import tweepy
import requests
import facebook-sdk


class TwitterBot:
    def __init__(self, username, pw):
        self.username = username
        self.pw = pw
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://twitter.com/login")
        sleep(5)
        email = self.driver.find_element_by_name("session[username_or_email]")
        pw = self.driver.find_element_by_name("session[password]")
        email.clear()
        pw.clear()
        email.send_keys(self.username)
        pw.send_keys(self.pw)
        pw.send_keys(Keys.RETURN)
        sleep(3)



    def like_tweet(self, hashtag):
        bot = self.driver
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        sleep(3)
        for i in range(0,20):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(2)
            #tweets1 = bot.find_elements_by_xpath("//div[@data-testid='tweet']")@class='css-1dbjc4n'
            # links = [elem.get_attribute('data-permalink-path') for elem in tweets1] and @aria-label='Timeline: Search timeline'
            # print(links)
            tweets2 = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
            print(tweets2)
            links = [elem.find_element_by_xpath("//a[@role='link' and @class ='css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']").get_attribute('href') for elem in tweets2]
            #links = [elem.find_element_by_xpath("//a[@role='link' and @class ='css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']").get_attribute('href') for elem in tweets2]
            links = list(set(links))

            print(links)
            for link in links:
                bot.get(link)
                try:
                    sleep(3)
                    bot.find_element_by_xpath( "//div[@aria-label='Like']").click()
                    sleep(10)
                except Exception as ex:
                    print(ex)
                    sleep(10)


    def delete_tweets(self):
        bot = self.driver

        last_ht, ht = 0, 1

        last_height = bot.execute_script("return document.body.scrollHeight")

        sleep(2)
        l = []
        while True:
        #for i in range(0,3):
            # Scroll down to bottom


            bot.find_element_by_xpath("//a[contains(@href,'/{}')][2]".format(self.username)).click()
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            #bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            sleep(7)
            tweets1 = bot.find_elements_by_class_name('css-1dbjc4n r-18u37iz r-thb0q2')
            print(tweets1)
            tweets2 = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
            print(tweets2)


            sleep(7)
            links = [elem.find_element_by_xpath(
                "//a[@role='link' and @class ='css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']").get_attribute(
                'href') for elem in tweets2]

            links = list(set(links))

            #links = list(set(links))
            print(links)
            l.extend(links)


            for link in links:
                bot.get(link)
                if self.username in link:
                    try:
                        sleep(3)
                        bot.find_element_by_xpath( "//div[@aria-label='More']").click()
                        sleep(2)
                        bot.find_element_by_xpath("//div[@role='menuitem'][1]").click()
                        #bot.find_element_by_xpath("//*[contains(text(), 'Delete')]").click()
                        sleep(2)
                        bot.find_element_by_xpath("//div[@role='button'][2]").click()
                        sleep(10)

                    except Exception as ex:
                        print(ex)
                else:
                    try:
                        sleep(3)
                        bot.find_element_by_xpath("//div[@aria-label='Retweeted']").click()
                        sleep(1)
                        bot.find_element_by_xpath("//div[@data-testid='unretweetConfirm'][1]").click()
                        sleep(1)
                    except Exception as ex:
                        print(ex)

            new_height = bot.execute_script("return document.body.scrollHeight")
            sleep(4)
            # break condition
            if new_height == last_height:
                break
            last_height = new_height
        print(len(l))



    def test(self):
        bot = self.driver
        bot.find_element_by_xpath("//a[contains(@href,'/{}')][2]".format(self.username)).click()
        soup = bs(bot.page_source, 'html.parser')
        print(soup.find_all("div", {"data-testid":"tweet"}))

    def marketsanddatatest(self, hashtag):
        bot = self.driver
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')
        sleep(2)

        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(2)
            # tweets1 = bot.find_elements_by_xpath("//div[@data-testid='tweet']")@class='css-1dbjc4n'
            # links = [elem.get_attribute('data-permalink-path') for elem in tweets1] and @aria-label='Timeline: Search timeline'
            # print(links)
            tweets2 = bot.find_elements_by_class_name("css-1dbjc4n")
            print(tweets2)
            sleep(2)
            links = [print(elem.get_attribute('innerHTML')) for elem in tweets2]
            #links = [elem.find_element_by_xpath("//a[@role='link' and @class ='css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']").get_attribute('href') for elem in tweets2]

            sleep(4)


            # for link in links:
            #     bot.get(link)
            #     try:
            #         sleep(3)
            #         bot.find_element_by_xpath("//div[@aria-label='Like']").click()
            #         sleep(10)
            #     except Exception as ex:
            #         print(ex)
            #         sleep(10)
    def mine(self):
        bot = self.driver
        bot.find_element_by_xpath("//a[contains(@href,'/{}')][2]".format(self.username)).click()
        sleep(2)
        last_height = bot.execute_script("return document.body.scrollHeight")
        i = 0
        while True:
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(2)
            tweets1 = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
            # links = [elem.get_attribute('data-permalink-path') for elem in tweets1] and @aria-label='Timeline: Search timeline'
            # print(links)
            tweets2 = bot.find_elements_by_class_name("css-1dbjc4n")
            print(tweets1)
            sleep(2)
            #links = [elem.get_attribute('innerHTML') for elem in tweets2]
            i += len(tweets1)
            print(i)
            sleep(4)
            new_height = bot.execute_script("return document.body.scrollHeight")
            # break condition
            if new_height == last_height:
                break
            last_height = new_height

        print('totla',i)


    def delete_tweets_attempt_two(self):
        bot = self.driver

        last_height = bot.execute_script("return document.body.scrollHeight")

        sleep(2)

        bot.find_element_by_xpath("//a[contains(@href,'/{}')][2]".format(self.username)).click()
        while True:
        #for i in range(0,3):
            # Scroll down to bottom



            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            #bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            sleep(10)
            # tweets1 = bot.find_elements_by_class_name('css-1dbjc4n r-18u37iz r-thb0q2')
            # print(tweets1)
            tweets2 = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
            print(tweets2)
            for t in tweets2:
                try:
                    sleep(3)
                    t.find_element_by_xpath("//div[@data-testid='unretweet']").click()
                    sleep(1)
                    t.find_element_by_xpath("//div[@data-testid='unretweetConfirm'][1]").click()
                    sleep(1)
                except Exception as ex:
                    print(ex)
                try:
                    sleep(3)
                    t.find_element_by_xpath("//div[@aria-label='More']").click()
                    sleep(2)
                    t.find_element_by_xpath("//div[@role='menuitem'][1]").click()
                    # bot.find_element_by_xpath("//*[contains(text(), 'Delete')]").click()
                    sleep(2)
                    t.find_element_by_xpath("//div[@role='button'][2]").click()
                    sleep(10)
                except Exception as ex:
                    print(ex)

            sleep(7)

            new_height = bot.execute_script("return document.body.scrollHeight")
            #sleep(12)
            # break condition
            if new_height == last_height:
                break
            last_height = new_height


class TweepyTwitter:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(self.auth)


    def delete(self):
        for status in tweepy.Cursor(self.api.user_timeline).items():
            try:
                self.api.destroy_status(status.id)
                print('success:'+str(status.id))
            # Process the status here
            except Exception as ex:
                print('Unable to print:'+str(status.id))
        for favourite in tweepy.Cursor(self.api.favorites).items():
            try:
                self.api.destroy_favorite(favourite.id)
                print('success:' + str(favourite.id))
            except Exception as ex:
                print('Unable to unlike:' + str(favourite.id))

    class FacebookCleaner:
        def __init__(self):
            pass


        def delete_posts(self):





#destroy_favorite(id)


#my_bot = TwitterBot('username', 'password')
#my_bot.login()
#my_bot.delete_tweets_attempt_two()

access_token = '******'
access_token_secret = '******'
consumer_key ='******'
consumer_secret = '******'

#tt = TweepyTwitter(consumer_key, consumer_secret, access_token,access_token_secret)
#tt.delete()






