from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pymongo import MongoClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
def scrape_twitter_data(Profile_name):

    driver = webdriver.Chrome()

    driver.get("https://www.facebook.com/")

    sleep(3)
    username = driver.find_element(By.XPATH,"//input[@name='email']")
    username.send_keys("9412354092")
    print("Username filled Successfuly")

       #now enter the details in password bar
    sleep(3)
    password = driver.find_element(By.XPATH,"//input[@name='pass']")
    password.send_keys("ritika")
    print("Password filled Successfuly")

    #     #now try to click on the log_in button 
    log_in = driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]")
    log_in.click()
    print("Log in clicked Successfuly")

    sleep(3)

    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    search_box = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='search']")))
    # search_box.click()
    print("shi hai Dude !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # //*[@id='mount_0_0_N8']/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/label
    search_box.send_keys(Profile_name)
    search_box.send_keys(Keys.ENTER)
    print("Entered the subject and clicked Successfully !!")
    sleep(13)

    # people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
    # # //*[@id=":r1d:"]/span
    # people.click()
    # sleep(3)
    # print("Clicked on people Successfully !!")

        # now go on profile of the subject
    profile = driver.find_element(By.XPATH,"//*[@id='mount_0_0_bK']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/h2/span/span/span/a/span[1]")
    profile.click()
    sleep(10)
    print("Went on profile Man ")


    Usertags = []
    Timestamps =[]
    Tweets =[]
    Replys =[]
    Retweets = []
    Likes = []

    articles = driver.find_elements(By.XPATH,"//*[@id='mount_0_0_/t']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[13]/div/div")
    print("Gone on article")
    sleep(5)
    while True:
        print("inside 1")
        for article in articles:
            print("inside 2")
            user_tag = driver.find_element(By.XPATH,"//*[@id=':r1oe:'']/span[1]/a/strong/span").text
            Usertags.append(user_tag)
            print("done 1",user_tag)
            sleep(3)
            # timestamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
            # Timestamps.append(timestamp)
            # print("done 2",timestamp)

            # tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
            # Tweets.append(tweet)
            # print("done 3")

            # reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
            # Replys.append(reply)
            # print("done 4")

            # retweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
            # Retweets.append(retweet)
            # print("done 5")

            # like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text
            # Likes.append(like)
            # print("done 6")

            # print("Saving the data to MongoDB Atlas...")
            # review_docs = []
            # review_doc = {
            #     "NAME ->": Profile_name,
            #     "Name :": user_tag,
            #     "Timestamp :": timestamp,
            #     "Tweet :": tweet,
            #     "Reply :": reply,
            #     "Retweet": retweet,
            #     "Likes :": like
            # }
            # review_docs.append(dict(review_doc))
            # collection.insert_many(review_docs)
            # print("Reviews saved to MongoDB Atlas successfully!",review_docs)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            # print("scrolled")
            articles = driver.find_elements(By.XPATH,"//*[@id='mount_0_0_/t']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[13]/div/div")
            # Tweets2 = list(set(Tweets))
            # if len (Tweets2) > 5:
            #     break
        break
if __name__ == "__main__":
    Profile_name = "myogiadityanath"
    Profile = scrape_twitter_data(Profile_name)
    if Profile:
        # save_to_mongodb(Profile_name, Profile)
        print("Profile scraped and saved to MongoDB Atlas successfully!")
    else:
        print("No Profile found or unable to scrape.")
