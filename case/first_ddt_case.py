# coding:utf-8
import sys
sys.path.append('C:\\Users\\xiazh\\PycharmProjects\\Imooc_selenium')
from bussiness.register_bussiness import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time
import ddt
from util.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data()

# 邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)
        self.file_name = 'C:\\Users\\xiazh\\PycharmProjects\\Imooc_selenium\\Image\\test001.png'

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
                file_path = os.path.join(file_path_father+'/report/'+case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    '''
    @ddt.data(
        ['12','stella0101','111111','code','user_email_error','请输入有效的电子邮件地址'],
        ['@qq.com','stella0101','111111','code','user_email_error','请输入有效的电子邮件地址'],
        ['12@qq.com','stella0101','111111','code','user_email_error','请输入有效的电子邮件地址']
        )

    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,code,assertCode,assertText = data
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error)

if __name__ == '__main__':
    file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
    file_path = os.path.join(file_path_father+'/report/'+'testreport1.html')
    fd = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fd,title='this is first report',description=u'这是第一个测试报告',verbosity=2)
    runner.run(suite)