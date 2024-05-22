from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open the page
driver.get("https://twitter.com/login")

# Wait for the parent element containing the username field to appear
parent_element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[1]/div/span'))
)

# Once the parent element appears, locate the username field within it
username_field = parent_element.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')

# Type the username
username_field.send_keys("rajneeshpanwar17@gmail.com")

# Press the Next button
next_button = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')[2]
next_button.click()

# Wait for network idle
driver.implicitly_wait(1.5)  # This waits for 1.5 seconds, equivalent to waitForNetworkIdle
