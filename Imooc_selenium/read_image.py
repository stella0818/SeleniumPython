# coding:utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
# image = Image.open('D:/imooc1.png')
# text = pytesseract.image_to_string(image)

r = ShowapiRequest("http://route.showapi.com/184-4","166211","a0459474e9f9489ab29a31ddb96bae51" )
r.addFilePara("image", "D:/imooc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
