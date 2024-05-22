from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pymongo import MongoClient

# Set up Chrome WebDriver
def scrape_twitter_data(Profile_name):
    
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")

    sleep(3)
    username = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
    username.send_keys("exitsolutions7411")
    print("Username filled Successfuly")

    sleep(3)
    password = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
    password.send_keys("1996@Exotica")
    print("Password filled Successfuly")

    log_in = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")
    log_in.click()
    print("Log in clicked Successfuly")

    sleep(6)
    not_now_button_xpath = driver.find_element(By.XPATH,"//div[@role='button' and text()='Not now']").click()
    print("not now option clicked Successfuly")
    sleep(4)

    notification_button_off = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
    print("notification_button_off option clicked Successfuly")

    sleep(5)
    # search_box = driver.find_element(By.CLASS_NAME, "x1lliihq")
    search_box = driver.find_element(By.XPATH,"//*[@id='mount_0_0_u0']/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div")
    print("bhittr bro !!!! gjjbs")
    search_box.click()
    print(" clicked Successfully !!")
    sleep(6)
    box = driver.find_element(By.XPATH,"//*[@id='mount_0_0_sr']/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
    box.send_keys(Profile_name)
    box.send_keys(Keys.ENTER)   
    sleep(7)

if __name__ == "__main__":
    Profile_name = 'Elon mask'
    # Profile_name = input("Kuch likhiye kisi reputed ka name: ")
    sleep(10)
    Profile = scrape_twitter_data(Profile_name)
