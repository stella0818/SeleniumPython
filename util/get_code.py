# coding:utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time

class GetCode(object):
    def __init__(self,driver):
        self.driver = driver
    # 获取验证码图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        # print(code_element.location)#{'x':'123','y':"345"}
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img .save(file_name)
        time.sleep(2)

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
        time.sleep(2)
        return text