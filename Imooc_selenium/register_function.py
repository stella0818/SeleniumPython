#coding=utf-8
import sys
sys.path.append('C:/Users/xiazh/PycharmProjects/Imooc_selenium')
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from find_element import FindElement

class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    # 获取driver并且打开url
    def get_driver(self,url,i):
        if i == 0:
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)



    # 定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
        return user_info

    # 获取验证码图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element('code_image')
        # print(code_element.location)#{'x':'123','y':"345"}
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img .save(file_name)

    # 解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","166211","a0459474e9f9489ab29a31ddb96bae51" )
        r.addFilePara("image", file_name)
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text



    def main(self):
        user_name_info = self.get_range_user()
        user_email = self.get_range_user()+'@163.com'
        file_name = 'D:/test.png'
        code_text = self.code_online(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_info)
        self.send_user_info('password','111111')
        self.send_user_info('code_text','11111')
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')
        if code_error == None:
            print('注册成功')
        else:
            self.driver.save_screenshot('D:/codeerror.png')
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(2):
        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()