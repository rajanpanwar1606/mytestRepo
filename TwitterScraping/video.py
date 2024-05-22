from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# import getpass as getpass

# Set up Chrome WebDriver
def scrape_twitter_data(Profile_name):
    
    driver = webdriver.Chrome()

    # Open Twitter login page
    driver.get("https://twitter.com/i/flow/login")

    #now enter the details in username bar
    sleep(3)
    username = driver.find_element(By.XPATH,"//input[@name='text']")
    username.send_keys("RAJANGURJAR1606")
    print("Username filled Successfuly")

    #now try to click on the next button 
    next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
    next_button.click()
    print("Next Clicked Successfuly")

    #now enter the details in password bar
    sleep(3)
    password = driver.find_element(By.XPATH,"//input[@name='password']")
    password.send_keys("RAAZgujjar@123")
    print("Password filled Successfuly")

    #now try to click on the log_in button 
    log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
    log_in.click()
    print("Log in clicked Successfuly")

    sleep(6)

    #now fill the subject which i want to search on twitter
    # search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
    # search_box = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
    search_box = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
    search_box.send_keys(Profile_name)
    search_box.send_keys(Keys.ENTER)
    print("Entered the subject and clicked Successfully !!")
    sleep(3)

    #now search for the people of that subject 
    # people = driver.find_element(By.XPATH,"//span[contains(text(),'People']")
    people = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div/span")
    people.click()
    sleep(3)
    print("Clicked on people Successfully !!")

    # now go on profile of the subject
    profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div")
    profile.click()
    sleep(5)
    print("Went on profile Man ")

    # now start the scraping 
    # user_tag = driver.find_element(By.XPATH,"//input[@data-testid='UserName']").text
    # user_tag = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]").text
    # print("User -> ",user_tag)
    # timestamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
    # print("Post Timestamp -> ",timestamp)
    # tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
    # print("Tweet Text -> ",tweet)
    # reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
    # print("Replies -> ",reply)
    # retweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
    # print("Retweets -> ",retweet)
    # like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text
    # print("Likes -> ",like)

    # sleep(5)

    Usertags = []
    Timestamps =[]
    Tweets =[]
    Replys =[]
    Retweets = []
    Likes = []
    articles = driver.find_elements(By.XPATH,"//article[@class ='css-175oi2r r-18u37iz r-1udh08x r-i023vh r-1qhn6m8 r-o7ynqc r-6416eg r-1ny4l3l r-1loqt21']")
    # articles = driver.find_element(By.XPATH,"//article[@data-testid='tweet']")
    # print(len(articles))
    while True:
        for article in articles:
            user_tag = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]").text
            Usertags.append(user_tag)
            print("done 1",Usertags)

            timestamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
            Timestamps.append(timestamp)
            print("done 2", Timestamps)

            tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
            Tweets.append(tweet)
            print("done 3", Tweets)

            reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
            Replys.append(reply)
            print("done 4",Replys)

            retweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
            Retweets.append(retweet)
            print("done 5", Retweets)

            like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text
            Likes.append(like)
            print("done 6", Likes)

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        # print("scolled")
        articles = driver.find_elements(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[10]/div/div/article")
        Tweets2 = list(set(Tweets))
        if len (Tweets2) > 5:
            break

    print(len(Usertags),len(Timestamps),len(Tweets),len(Replys),len(Retweets),len(Likes))


#   MAIN FUNCTION >>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    # Profile_name = 'Elon mask'
    Profile_name = input("Kuch likhiye kisi reputed ka name: ")
    sleep(10)
    Profile = scrape_twitter_data(Profile_name)
    if Profile:
        save_to_mongodb(Profile_name, Profile)
        print("Profile scraped and saved to MongoDB Atlas successfully!")
    else:
        print("No Profile found or unable to scrape.")