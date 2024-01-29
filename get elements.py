from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
#second test for page element
Base_url ="https://play1.automationcamp.ir/"

service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get(f"{Base_url}forms.html")
#checkbox
driver.find_element('id', 'check_python').click()
checked_python = driver.find_element('id','check_validate').text
assert checked_python == 'PYTHON'
#multline
text1="hello automation"
driver.find_element('id','notes').send_keys(text1)
multi_text= driver.find_element('id','area_notes_validate').text
assert multi_text == text1




