import pandas as pd
from links import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from links import *


driver = webdriver.Chrome(executable_path='/Users/Toby_Py/Documents/chromedriver')



# def get_product_window():
#     restaurant_window = driver.window_handles[0]
#     return restaurant_window

# open product link
driver.get(product_links[0])

# Get parent table containing all products
parent_table = driver.find_element(by=By.XPATH,value='//*[@id="productSection"]/div[2]')
time.sleep(3)
product = parent_table.find_elements(by=By.TAG_NAME, value = 'a')

# Create an empty dict
product_dict = {}

for p in product:
    # Open product link in new tab
    ActionChains(driver).move_to_element(product[p]).key_down(Keys.COMMAND).click(product[p]).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    # Find product details and brands
    product_details = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div[1]/div/div[3]')
    product_attributes = driver.find_element(by=By.XPATH, value = '//*[@id="simple-tabpanel-0"]/div/div/div/div[2]/div')
    print('Product Details found')

    # Extract details from product details and attributes
    product_brand = product_details.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div[1]/div/div[3]/div[1]/div[1]/p').text
    product_name = product_details.find_element(by=By.XPATH, value = '//*[@id="__next"]/main/div[1]/div/div[3]/h1').text
    rating = product_details.find_element(by=By.XPATH, value = '//*[@id="__next"]/main/div[1]/div/div[3]/div[3]/p[1]').text
    product_attribute = product_attributes.find_elements(by=By.TAG_NAME, value = 'p')
    attrs = [] # List to hold all attributes

    # Extract product attributes and append to list
    for attr in product_attribute:
        attrss = attr.text
        attrs.append(attrss)
    # Include each product detail in product_dict
    product_dict[p] = {'brand':product_brand, 'name':product_name, 'rating':rating, 'attributes':attrs}



