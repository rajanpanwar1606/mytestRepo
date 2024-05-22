from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scrape_twitter_data(person_name):
    try:
        # Start Chrome webdriver
        driver = webdriver.Chrome()
        print("Good Morning bro webdriver Chrome is running properly CONGRATS !!!!!!")
        
        # Open Twitter page
        driver.get("https://twitter.com/login")

        # Replace 'your_username' and 'your_password' with your Twitter username and password
        username = "RAJANGURJAR1606"   #gujjar_rajan_
        password = "RAAZgujjar@123"

        # Find username and password input fields and enter the credentials
        username_input = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input")
        password_input = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        # Wait for a few seconds for the page to load
        time.sleep(5)

        # Verify if login was successful
        if "twitter.com/home" in driver.current_url:
            print("Login Successful!")
        else:
            print("Login Failed!")
            return None

        # You can add more scraping logic here

    except Exception as e:
        print("An error occurred:", str(e))
        return None

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    person_name = 'Narendra Modi'
    data = scrape_twitter_data(person_name)

    if data:
        # save_to_mongodb(person_name, data)  # Call to save data to MongoDB
        print("Data scraped and saved to MongoDB Atlas successfully!")
    else:
        print("No data found or unable to scrape.")
