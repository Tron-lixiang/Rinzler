from selenium import webdriver
import time
from requests import Session

req=Session()
driver = webdriver.Chrome('./chromedriver') #填写chromedriver的路径
driver.get("http://www.weibo.com/login.php")

elem = driver.find_element_by_xpath('//*[@id="loginname"]') #通过xpath寻找账号输入框
elem.clear()
elem.send_keys("nidezhanghao") #输入账号
password = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input') #也可以通过寻找元素找到密码输入框
password.clear()
password.send_keys("nidemimaxd") #输入密码
login=driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
#input('如果有验证码请手工输入后，在此输入任意继续')
login.click()
#time.sleep(10) #这里可以sleep
cookies=driver.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])
    print(cookie)
req.headers.clear()
#driver.quit()
