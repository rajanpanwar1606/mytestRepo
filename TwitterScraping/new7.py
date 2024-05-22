import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open Twitter login page
driver.get("https://twitter.com/login")

# Find username field and fill it with your credentials
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input"))
    )
    username_field.send_keys("YOUR_USERNAME")
except Exception as e:
    print("Failed to find or fill username field:", e)

# Find password field and fill it with your credentials
try:
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "session[password]"))
    )
    password_field.send_keys("YOUR_PASSWORD")
    password_field.submit()
except Exception as e:
    print("Failed to find or fill password field:", e)

# Wait for the login process to complete
try:
    WebDriverWait(driver, 10).until(EC.url_contains("https://twitter.com/home"))
    print("Login successful!")
except Exception as e:
    print("Login failed:", e)

# Now you are logged in and can perform further actions on Twitter

# Don't forget to quit the WebDriver when you're done
driver.quit()
