
from math import prod
from products import *

# Fetch the parent table for all products
parent_table = driver.find_element(by=By.XPATH,value='//*[@id="productSection"]/div[2]')
products = parent_table.find_elements(by=By.TAG_NAME, value = 'a')

brand_name = []
product_name = []
ratings = []
product_attributes = []

current_window = get_product_window()

for pages in range(total_search_results):
    for item in products:
        product_detail, product_attribute = get_product_details(parent_table)
        brand = get_brand_name(product_detail)
        name = get_product_name(product_detail)
        rating = get_rating(product_detail)
        attributes = get_product_attribute(product_attribute)

        driver.close()
        driver.switch_to.window(current_window)
        



# Fetch brand name


# Fetch product name

# Fetch rating

# Get the product attributes

# Go back to the main page and continue with the other products on all pages

# Save all that information in a list or Dict

# Go to the next product link and repeat 

