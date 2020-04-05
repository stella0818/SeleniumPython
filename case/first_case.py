#coding=utf-8
import sys
sys.path.append('C:\\Users\\xiazh\\PycharmProjects\\Imooc_selenium')
from bussiness.register_bussiness import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time
from log.user_log import UserLog

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logging = UserLog()
        cls.log = cls.logging.get_log()

    @classmethod
    def tearDownClass(cls):
        cls.logging.close_handle()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.log.info('----->stella')
        
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
        
   
    def test_login_email_error01(self):
        email_error = self.login.login_email_error('123456','stella001','123456',self.file_name)
        self.assertFalse(email_error)
        # if email_error == True:
        #     print('fail')
        # else:
        #     print('success')
    def test_login_username_error02(self):
        username_error = self.login.login_username_error('1234567890abc@163.com','111','123456',self.file_name)
        self.assertFalse(username_error)

    def test_login_password_error03(self):
        password_error = self.login.login_password_error('1234567890ab@163.com','stella002','11',self.file_name)
        self.assertFalse(password_error)

    def test_login_code_error04(self):
        code_error = self.login.login_code_error('1234567890cd@163.com','stella003','123456',self.file_name)
        self.assertFalse(code_error)

    def test_login_success05(self):
        success = self.login.register_success('xiazhou.a213@gmail.com','stella004','123456',self.file_name)
        self.assertFalse(success)
'''
    def main(self):
        case = FirstCase()
        case.test_login_email_error()
        case.test_login_username_error()
        case.test_login_password_error()
        case.test_login_code_error()
        case.test_login_success()
'''
if __name__ == '__main__':
    # unittest.main()
    file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
    file_path = os.path.join(file_path_father+'/report/'+'testreport.html')
    fd = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error01'))
    suite.addTest(FirstCase('test_login_username_error02'))
    suite.addTest(FirstCase('test_login_password_error03'))
    suite.addTest(FirstCase('test_login_code_error04'))
    suite.addTest(FirstCase('test_login_success05'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fd,title='this is first report',description=u'这是第一个测试报告',verbosity=2)
    runner.run(suite)