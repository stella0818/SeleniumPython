# coding:utf-8
import unittest
class FirstCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('firstclass02')

    @classmethod
    def tearDownClass(cls):
        print('lastclass02')

    def setUp(self):
        print('firstmethod02')

    def tearDown(self):
        print('lastmethod02')

    # @unittest.skip('不执行第一条')
    def testfirst001(self):
        print('this is one case')

    def testfirst002(self):
        print('this is two case')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst001'))
    unittest.TextTestRunner().run(suite)
