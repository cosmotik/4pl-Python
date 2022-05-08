from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


URL1 = "https://www.atea.lt/eshop/"
URL2 = "https://www.kainos.lt/"
URL3 = "https://www.kilobaitas.lt/"

DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver_win32\chromedriver.exe"

driver1 = webdriver.Chrome(executable_path=DRIVER_PATH)
driver1.get(URL1)
driver2 = webdriver.Chrome(executable_path=DRIVER_PATH)
driver2.get(URL2)
driver3 = webdriver.Chrome(executable_path=DRIVER_PATH)
driver3.get(URL3)

query_field1 = driver1.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[4]/div/form/div/input")
query_field1.send_keys("MSI GeForce RTX 3090 VENTUS 3X")
time.sleep(1)
driver1.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[4]/div/form/div/span/button").click()
time.sleep(1)
price1 = driver1.find_element(By.XPATH, "/html/body/div[2]/div/main/div[2]/div[2]/div[3]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div[3]/div/span")
print("Atea - Kaina: " + price1.text)
driver1.close()

query_field2 = driver2.find_element(By.NAME, "q")
query_field2.send_keys("MSI GeForce RTX 3090 VENTUS 3X")
query_field2.find_element(By.XPATH, "/html/body/div[9]/div[3]/div/div[1]/div/div[2]/div/button[1]").click()
time.sleep(1)
driver2.find_element(By.XPATH, "/html/body/div[2]/div/form/div/button").click()
time.sleep(1)
price2 = driver2.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/a/div[3]")
print("Kainos lt - Kaina: " + price2.text)
driver2.close()

query_field3 = driver3.find_element(By.NAME, "lytA$ctl23$search")
query_field3.send_keys("MSI GeForce RTX 3090 VENTUS 3X")
time.sleep(1)
driver3.find_element(By.XPATH, "/html/body/form/div[4]/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/a").click()
time.sleep(1)
price3 = driver3.find_element(By.CLASS_NAME, "price")
print("Kilobaitas - " + price3.text)
driver3.close()





