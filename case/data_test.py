# coding:utf-8
import unittest
import ddt


@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print('this is setup')

    def tearDown(self):
        print('this is teardown')

    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
        )
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()