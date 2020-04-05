#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get('http://www.5itest.cn/register')
time.sleep(5)
# 判断title是否包含“注册”
# print(EC.title_contains('注册'))

# driver.save_screenshot('D:/imooc.png')
# code_element = driver.find_element_by_id('getcode_num')
# print(code_element.location)#{'x':'123','y':"345"}
# left = code_element.location['x']
# top = code_element.location['y']
# right = code_element.size['width']+left
# height = code_element.size['height']+top
# im = Image.open('D:/imooc.png')
# img = im.crop((left,top,right,height))
# img .save('D:/imooc1.png')

# r = ShowapiRequest("http://route.showapi.com/184-4","166211","a0459474e9f9489ab29a31ddb96bae51" )
# r.addFilePara("image", "D:/imooc1.png")
# r.addBodyPara("typeId", "35")
# r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
# res = r.post()
# text = res.json()['showapi_res_body']['Result']
# print(text) # 返回信息
# time.sleep(2)
# driver.find_element_by_id('captcha_code').send_keys(text)

driver.find_element_by_id('register_email').send_keys('111')
driver.find_element_by_id('register_password').send_keys('111111')
print(driver.find_element_by_id('register_email-error').text)

# 判断元素是否可见

# EC.Visibility_of_element_located()
# for i in range(5):
#     user_email = ''.join(random.sample('1234567890abcdefg',8))+'@163.com'
#     print(user_email)

# time.sleep(5)


# element = driver.find_elements_by_class_name('controls')
# locate = (By.CLASS_NAME,'controls')
# WebDriverWait(driver,10).until(EC.visibility_of_element_located(locate))
# email_element = driver.find_element_by_id('register_email')
# print(email_element.get_attribute('placeholder'))
# email_element.send_keys('xiazhou.a2@gamil.com')
# print(email_element.get_attribute('value'))
driver.close()
# driver.find_element_by_id('register_email').send_keys('xiazhou.a2@gmail.com')
# classone = driver.find_elements_by_class_name('controls')[1]
# classone.find_element_by_class_name('form-control').send_keys('stella')
# driver.find_element_by_name('password').send_keys('123456')
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys('11111')