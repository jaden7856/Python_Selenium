from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = 'C:\\Users\\User\\Desktop\\DataStudy\\Work\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://facebook.com')
print(driver.title)

elem_email = driver.find_element_by_id('email')
elem_email.send_keys('jhg7856@naver.com')
elem_pass = driver.find_element_by_id('pass')
elem_pass.send_keys('dkssudDKSSUD12')
elem_pass.send_keys(Keys.RETURN)

profile_a = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a')
print("Profile A : ", profile_a.get_attribute('href'))

friends_a = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a')
print("Friends_a A : ", friends_a.get_attribute('href'))

driver.get(profile_a.get_attribute('href'))