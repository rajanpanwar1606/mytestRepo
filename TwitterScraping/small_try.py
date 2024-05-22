from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome webdriver
driver = webdriver.Chrome()

try:
    # Open Twitter page
    driver.get("https://twitter.com/?lang=en-in")

    # Wait for the element to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span'))
    )

    # Click on the element
    element.click()

    print("Element clicked successfully!")

    # Wait for the page to load
    time.sleep(5)  # Adjust the time as needed

    print("Page fully loaded!")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser
    driver.quit()
