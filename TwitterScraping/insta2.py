from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def scrape_insta_data(Profile_name):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    
    try:
        # Wait for the username field and fill it
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input"))).send_keys("exitsolutions7411")
        print("Username filled Successfully")

        # Wait for the password field and fill it
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input"))).send_keys("1996@Exotica")
        print("Password filled Successfully")

        # Wait for the login button and click it
        log_in = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")
        log_in.click()
        print("Log in clicked Successfuly")

        # Wait for the 'Not now' button and click it
        sleep(6)
        not_now_button_xpath = driver.find_element(By.XPATH,"//div[@role='button' and text()='Not now']").click()
        print("not now option clicked Successfuly")
        sleep(4)

        notification_button_off = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        print("notification_button_off option clicked Successfuly")

        sleep(6)
        # Wait for the search box and use it
        search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
        search_box.send_keys(Profile_name)
        sleep(2)  # Small sleep to allow search results to appear
        search_box.send_keys(Keys.ENTER)  # Hit enter again to go to the profile
        print("Entered the subject and clicked Successfully !!")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    Profile_name = 'elonmusk'
    scrape_insta_data(Profile_name)
