from selenium import webdriver

class Browser_Tests_With_pathVariable:

    def launch_firefox(self):
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("//input[@title='Search']").send_keys("test")
        driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()
        driver.close()

    def launch_chrome(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("//input[@title='Search']").send_keys("test")
        driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()
        driver.close()

    def launch_IE(self):
        driver = webdriver.Ie()
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("//input[@title='Search']").send_keys("test")
        driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()
        driver.close()


browser = Browser_Tests_With_pathVariable()
browser.launch_IE()
browser.launch_firefox()
browser.launch_chrome()
