from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = 'C:\\Users\\User\\Desktop\\DataStudy\\Work\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://github.com/login')
print(driver.title)

elem_email = driver.find_element_by_id('login_field')
elem_email.send_keys('jaden7856')
elem_pass = driver.find_element_by_id('password')
elem_pass.send_keys('dkssudDKSSUD12')

elem_pass.send_keys(Keys.RETURN)

