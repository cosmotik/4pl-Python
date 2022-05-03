from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://nkkm.lt"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

# menu = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul")
# events = menu.find_elements(By.CSS_SELECTOR, "li a")
# for event in events:
#    print(event.text)

driver.find_element(By.ID, "menu-item-401").click()

rugsejis_field = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/article/div/div/div/div/div[2]"
                                     "/div/div/div[3]/ul/li[2]/a")
rugsejis_field.send_keys(Keys.ENTER)

time.sleep(1)

name_field = driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]"
                                 "/div/div/form/p[1]/label/span[2]/input")
name_field.send_keys("Tony")

surname_field = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]"
                                    "/div/div/form/p[2]/label/span[2]/input")
surname_field.send_keys("Stark")

age_field = driver.find_element(By.XPATH,
                                "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]"
                                "/div/div/form/p[3]/label/span[2]/input")
age_field.send_keys("18")

phone_field = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]"
                                  "/div/div/form/p[4]/label/span[2]/input")
phone_field.send_keys("+37068355210")

email_field = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]"
                                  "/div/div/form/p[5]/label/span[2]/input")
email_field.send_keys("Tonys@gmail.com")

driver.find_element(By.XPATH,"/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div"
                             "/div/form/p[6]/span/span/span/input").click()

# titles = driver.find_elements(By.TAG_NAME, "h3")

# for title in titles:
#    print(title.text)

# driver.quit()
