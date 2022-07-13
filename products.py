import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from links import *
# import time
driver = webdriver.Chrome(executable_path='/Users/Toby_Py/Documents/chromedriver')
driver.get(product_links[0])


def total_search_results():
    total_search_results = int(driver.find_element(by=By.XPATH, value = '//*[@id="productSection"]/div[1]/p').text.split(" ")[0])
    return total_search_results


def get_product_window():
    restaurant_window = driver.window_handles[0]
    return restaurant_window

# parent_table = driver.find_element(by=By.XPATH,value='//*[@id="productSection"]/div[2]')
def get_product_details(parent_table):
    # product = parent_table.find_element(by=By.TAG_NAME, value = 'a')
    
    ActionChains(driver).move_to_element(product).key_down(Keys.COMMAND).click(product).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[1])
    try:
        product_details = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div[1]/div/div[3]')
        product_attributes = driver.find_element(by=By.XPATH, value = '//*[@id="simple-tabpanel-0"]/div/div/div/div[2]/div')
        print('Product Detail and Atrribute found')
    except:
        print('There was an issue locating the Product information')
    return product_details, product_attributes



def get_brand_name(product_details):
    product_brand = product_details.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div[1]/div/div[3]/div[1]/div[1]/p').text
    return product_brand

def get_product_name(product_details):
    product_name = product_details.find_element(by=By.XPATH, value = '//*[@id="__next"]/main/div[1]/div/div[3]/h1').text
    return product_name

def get_rating(product_details):
    rating = product_details.find_element(by=By.XPATH, value = '//*[@id="__next"]/main/div[1]/div/div[3]/div[3]/p[1]').text
    return rating

def get_product_attribute(product_attributes):
    product_attributes = product_attributes.find_elements(by=By.TAG_NAME, value = 'p')
    attribute_list = []
    for attributes in product_attributes:
        attr = attributes.text
        attribute_list.append(attr)

