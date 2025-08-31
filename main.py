from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

time.sleep(20)
driver.quit()