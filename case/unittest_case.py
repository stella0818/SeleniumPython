# coding:utf-8
import unittest
class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('firstclass')

    @classmethod
    def tearDownClass(cls):
        print('lastclass')

    def setUp(self):
        print('firstmethod')

    def tearDown(self):
        print('lastmethod')

    # @unittest.skip('不执行第一条')
    def testfirst01(self):
        print('this is one case')

    def testfirst02(self):
        print('this is two case')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst01'))
    unittest.TextTestRunner().run(suite)



