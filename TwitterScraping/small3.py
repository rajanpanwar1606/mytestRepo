from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open Twitter login page
driver.get("https://www.facebook.com/")

# Find username and password fields and fill them with your credentials
try:
    print("Good Morning bro try 1 is running properly CONGRATS !!!!!!")
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input"))
        )
except:
    username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "session[Email address or phone number]")))
    
username_field.send_keys("RAJANGURJAR1606")
username_field.submit()
time.sleep(10)


try:
    print("Good Morning bro try 2 is running properly CONGRATS !!!!!!")
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autofocus='autofocus']"))
        )
except:
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "session[Password]")))
    
password_field.send_keys("raazGUJJAR@123")
password_field.submit()
password_field.send_keys(Keys.RETURN)
time.sleep(10)


    # Submit the login form

    # Wait for the login process to complete (you might need to adjust the time depending on your internet speed)
WebDriverWait(driver, 10).until(EC.url_contains("https://www.facebook.com/"))

# Now you are logged in and can perform further actions on Twitter
