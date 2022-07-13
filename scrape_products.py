import pandas as pd
from links import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from links import *
# from selenium.webdriver.support.select import Select
import os.path

# Check if file exists
file_exists = os.path.exists('products_data.csv')
if file_exists == False:
    with open('products_data.csv', 'w') as file:
        file.write("Brand,Product_name,Product_rating,Product_attributes,\n")# Headers
    print('File created!')
    
# Open link
driver = webdriver.Chrome(executable_path='/Users/Toby_Py/Documents/chromedriver')
driver.get(product_links[6])
driver.maximize_window()
time.sleep(1)


# A function to get base window for search results
def get_product_window():
    product_window = driver.window_handles[0]
    return product_window

main_product_window = get_product_window()

# A function to get the totla number of search results
def total_search_results():
    total_search_results = int(driver.find_element(by=By.XPATH, value = '//*[@id="productSection"]/div[1]/p').text.split(" ")[0])
    return total_search_results


for page in range(0,total_search_results()):
    parent_table = driver.find_element(by=By.XPATH,value='//*[@id="productSection"]/div[2]')
    print('Parent Table found!!')
    time.sleep(2)
    product = parent_table.find_elements(by=By.TAG_NAME, value = 'a')
    for p in product:
        # Open product link in new tab
        ActionChains(driver).move_to_element(p).key_down(Keys.COMMAND).click(p).key_up(Keys.COMMAND).perform()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        product_details = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div[1]/div/div[3]')
        product_attributes = driver.find_element(by=By.XPATH, value = '//*[@id="simple-tabpanel-0"]/div/div/div/div[2]/div')
        print('Product Details found')
        try:
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

            string_attrs = ';'.join(str(item) for item in attrs)
            print('Product Attributes scraped')
            time.sleep(3)

            with open('products_data.csv', 'a') as file:
                file.write(product_brand+","+product_name+","+rating+","+string_attrs+"\n")
            
            print('Product details written to file')
            # Close product link tab and get back to previous tab
            driver.close()
            driver.switch_to.window(main_product_window)
            time.sleep(3)
        except:
            print('Could not fetch Product details!')
            pass
       
    print('Page ' + str(page + 1) + ' Done')
    time.sleep(3)
    try:
        next_page = driver.find_element(by=By.XPATH, value = '//*[@id="__next"]/main/div[3]/div/div/nav/ul/li[7]/button')
        next_page.click()
    except:
        print('No next page')
        break
    time.sleep(5)

print('Scraping completed!')
driver.close()