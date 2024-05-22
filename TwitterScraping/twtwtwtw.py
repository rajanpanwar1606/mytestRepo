# from django.http import JsonResponse
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
from time import sleep
from django.http import JsonResponse
import json
# user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
driver.maximize_window()

driver = webdriver.Chrome(options=options)
driver.get("https://twitter.com/i/flow/login")

sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("ExoticaLtd")
print("Username filled Successfully")

next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()
print("Next Clicked Successfully")

sleep(3)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("S5Us3/)pT$.H#yy")

print("Password filled Successfully")

log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
log_in.click()
print("Log in clicked Successfully")

sleep(10)

search_icon = driver.find_element(By.CSS_SELECTOR, 'svg.r-4qtqp9.r-yyyyoo.r-dnmrzs.r-bnwqim.r-lrvibr.r-m6rgpd.r-1nao33i.r-lwhw9o.r-cnnz9e')

# Click the SVG element
# ActionChains(driver).move_to_element(search_icon).click().perform()
search_icon.click()
# explore_btn.click()
print("click on explore")
sleep(5)
tradding_btn = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
tradding_btn.click()
sleep(5)
hashtags ='zxcxzcz'
trandding = []
print("click on explore")

trabdding = driver.find_elements(By.CLASS_NAME, 'css-175oi2r')
data = []
while True:
    tranding_name = driver.find_elements(By.CLASS_NAME, 'r-18u37iz')
    for article in trabdding:
        tranding_name = driver.find_element(By.CLASS_NAME, 'r-18u37iz').text

        data.append({
            "trading_number": tranding_name,
        })
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        trabdding\
            = driver.find_elements(By.CLASS_NAME, 'css-175oi2r')
        if len(data) > 5:
            break
    break
with open(f"{hashtags}.json", "w", encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

    driver.quit()
    print('tradding_btn is CLicked', trabdding)