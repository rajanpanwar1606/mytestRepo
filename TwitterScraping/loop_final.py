from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pymongo import MongoClient

# Set up Chrome WebDriver
def scrape_twitter_data(Profile_name):
    
    # mongo connection and db ,reviews definition
    client = MongoClient("mongodb+srv://rajanrajneesh1606:panwar123@cluster0.u2nqsx1.mongodb.net/")
    db = client["Sample_Twitter"] 
    collection = db[Profile_name]

    # #making it all headless 
    chrome_options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")

    # # Set up Chrome WebDriver
    driver = webdriver.Chrome(chrome_options)
    # driver = webdriver.Chrome()

    # Profile_name="narendra modi"
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
    search_box = driver.find_element((By.XPATH, "//input[@aria-label='Search query']"))
    # search_box = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
    search_box.send_keys(Profile_name)
    search_box.send_keys(Keys.ENTER)
    print("Entered the subject and clicked Successfully !!")
    sleep(3)

    people = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div/span")
    people.click()
    sleep(3)
    print("Clicked on people Successfully !!")

        # now go on profile of the subject
    profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div")
    profile.click()
    sleep(5)
    print("Went on profile Man ")

    #for storage variable

    #for data scraping
    Usertags = []
    Timestamps =[]
    Tweets =[]
    Replys =[]
    Retweets = []
    Likes = []
    articles = driver.find_elements(By.CLASS_NAME,'css-175oi2r')

    while True:
        for article in articles:
            user_tag = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]").text
            Usertags.append(user_tag)
            print("done 1",user_tag)

            timestamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
            Timestamps.append(timestamp)
            print("done 2",timestamp)

            tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
            Tweets.append(tweet)
            print("done 3")

            reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
            Replys.append(reply)
            print("done 4")

            retweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
            Retweets.append(retweet)
            print("done 5")

            like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text
            Likes.append(like)
            print("done 6")

            print("Saving the data to MongoDB Atlas...")
            review_docs = []
            review_doc = {
                "NAME ->": Profile_name,
                "Name :": user_tag,
                "Timestamp :": timestamp,
                "Tweet :": tweet,
                "Reply :": reply,
                "Retweet": retweet,
                "Likes :": like
            }
            review_docs.append(dict(review_doc))
            collection.insert_many(review_docs)
            print("Reviews saved to MongoDB Atlas successfully!",review_docs)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            print("scrolled")
            articles = driver.find_elements(By.CLASS_NAME,'css-175oi2r')
            Tweets2 = list(set(Tweets))
            # if len (Tweets2) > 5:
            #     break
        break


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
