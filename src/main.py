import selenium
import selenium.webdriver as web
from selenium.webdriver.common.by import By

driver = web.Firefox()

driver.get("https://web.eitaa.com/")
driver.implicitly_wait(1)

input_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]")
input_field.send_keys("+989118035743")

button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/button")
button.click()