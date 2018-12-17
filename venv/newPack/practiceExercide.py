from selenium import webdriver

class practice:

    def get_text_from_cell(self):
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        cell_value = driver.find_element_by_xpath("//table[@id='product']/tbody/tr[3]/td[3]").text
        print(cell_value)


object = practice()
object.get_text_from_cell()
