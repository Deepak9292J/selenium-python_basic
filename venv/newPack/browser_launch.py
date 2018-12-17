from selenium import webdriver

class Browser_Tests_Standard:

    def launch_firefox(self):
        driver = webdriver.Firefox(executable_path="C:\\selenium-java-3.13.0\\Drivers\\Firefox\\geckodriver.exe")
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("//input[@title='Search']").send_keys("test")
        driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()
        driver.close()

    def launch_chrome(self):
        driver = webdriver.Chrome(executable_path="C:\\selenium-java-3.13.0\\Drivers\\ChromeDriver\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("//input[@title='Search']").send_keys("test")
        driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()
        driver.close()

    def launch_IE(self):
        driver = webdriver.Ie(executable_path="C:\\selenium-java-3.13.0\\Drivers\\IE\\IEDriverServer.exe")
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("//input[@title='Search']").send_keys("test")
        driver.find_element_by_xpath("//a[contains(text(),'Images')]").click()
        driver.close()

browser = Browser_Tests_Standard()
browser.launch_IE()
browser.launch_firefox()
browser.launch_chrome()
