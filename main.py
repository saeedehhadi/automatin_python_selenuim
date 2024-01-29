from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
#first test to browse google and search on it

service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com/")
search_field = driver.find_element('id', 'APjFqb')
search_field.send_keys("hello world ")
search_field.send_keys(Keys.ENTER)

#second test for page element
Base_url ="https://play1.automationcamp.ir/"



