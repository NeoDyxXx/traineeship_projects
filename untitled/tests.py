import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        print('run test 1')
        self.assertEqual("hello".capitalize(), "hello")

    def test_2(self):
        print('run test 2')
        self.assertTrue("hello".islower())

    def test_3(self):
        print("run test 3")
        with self.assertRaises(TypeError):
            '2' + 2

if __name__ == '__main__':
    unittest.main()
