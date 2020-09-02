from selenium import webdriver
from time import sleep

class TwitterBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com/login")
        sleep(7)
        self.driver.find_element_by_name("session[username_or_email]").send_keys(username)
        self.driver.find_element_by_name("session[password]").send_keys(pw)
        self.driver.find_element_by_xpath("//div[@role='button']").click()

        self.username = username


        self.pw = pw
        sleep(1)

    def delete_all_tweets(self):
        tweets = self.driver.find_elements_by_xpath("(//div[aria-label='More'])[1]/following-sibling::*")
        print(tweets)
        for i in range(0,len(tweets)):
            if tweets[i].is_displayed():
                tweets[i].click()
                print(tweets[i])

        # tweet = self.driver.find_elements_by_xpath("//div[@data-testid='tweet']")
        # print(tweet)
        # more = self.driver.find_element_by_xpath("(//div[aria-label='More'])[1]/../following-sibling::*")
        # more.find_element_by_link_text('Delete').click()



    def load_page(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')][2]".format(self.username)).click()
        # last_ht, ht = 0, 1

        last_height = self.driver.execute_script("return document.body.scrollHeight")
        path =[]
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            # Wait to load page
            sleep(3)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            # break condition
            if new_height == last_height:
                break
            last_height = new_height



my_bot =TwitterBot('username', 'password')
my_bot.load_page()
my_bot.delete_all_tweets()