import math
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os


driver = webdriver.Chrome(executable_path='C:\Selenium Chrome\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://suninjuly.github.io/explicit_wait2.html')

counter = WebDriverWait(driver,4).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
button =  driver.find_element_by_id('book').click()
time.sleep(2)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
unswer_field = driver.find_element_by_id('answer')
unswer_field.click()
unswer_field.send_keys(y)
submit = driver.find_element_by_id('solve').click()




