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


# A function to get base window for search results
def get_product_window():
    product_window = driver.window_handles[0]
    return product_window

# A function to get the totla number of search results
def total_search_results():
    total_search_results = int(driver.find_element(by=By.XPATH, value = '//*[@id="productSection"]/div[1]/p').text.split(" ")[0])
    return total_search_results

# open product link
driver.get(product_links[1])
# Get the current window handle
main_product_window = get_product_window()

# Create an empty dict to hold all scraping results
product_dict = {}

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
        product_dict[product.index(p)] = {'brand':product_brand, 'product_name':product_name, 'product_rating':rating, 'product_attributes':attrs}

        # Close product link tab and get back to previous tab
        driver.close()
        driver.switch_to.window(main_product_window)
        time.sleep(5)


    print('Page ' + str(page + 1) + ' Done')
    print('The dictionary now contains ' + str(len(product_dict)) + ' products')

    next_page = driver.find_element(by=By.XPATH, value = '//*[@id="__next"]/main/div[3]/div/div/nav/ul/li[7]/button')
    print("Next page button found")
    next_page.click()
    time.sleep(2)
    driver.refresh()
    time.sleep(3) # Refresh page

    
print('Scraping Done')

print(product_dict)
#Create a dataframe from product_dict
# df = pd.DataFrame.from_dict(product_dict, orient='index')

