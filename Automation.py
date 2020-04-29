# importing webdriver from selenium module
from selenium import webdriver

# Storing chrome driver in a variable (put chrome driver in current working directory or provide location where it is stored
chromedriver = "chromedriver.exe"

# creating object of webdriver with chrome driver app
driver = webdriver.Chrome(chromedriver)

# Target url to be accessed
driver.get("https://www.google.com/")

# finding search bar using xpath
search_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
# sending "python" into search bar
search_bar.send_keys("python")

# finding search button using xpath
search_button = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
# pressing search button with click function
search_button.click()
