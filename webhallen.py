from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()   

url = "https://www.webhallen.com/"
browser.get(url)

acceptCookies = browser.find_element(By.XPATH, '//*[@id="cookie-banner"]/div/button[1]')
acceptCookies.click()

time.sleep(2)

searchInput = browser.find_element(By.XPATH, '//*[@id="main-header"]/div/div/div[2]/div/div/div/input')
searchInput.send_keys("laptop")
searchInput.send_keys(Keys.ENTER)
time.sleep(5)

list_of_product = browser.find_elements(By.XPATH, '//div[@class = "product-list-page"]/div/div/div/span/span/a')
list_of_product_text = []
for product in list_of_product:
    list_of_product_text.append(product.text)
    print(product.text)

number_of_products = len(list_of_product_text)
print(f"Number of products: ", number_of_products)

# searchButton = browser.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
# searchButton.click()

# findToy = browser.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[13]/div/div/span/div/div/div[2]/div[1]/h2/a/span')
# findToy.click()


# Don't forget to close the browser after your operation
browser.quit()



