from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://learn.letskodeit.com/p/practice")
number_of_links = driver.find_elements_by_tag_name("a")
count = len(number_of_links)
print("Number of links on the page are {}".format(count))