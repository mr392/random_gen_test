import unittest
import RandomGenerators

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_list = RandomGenerators.list_generator(1)

        self.assertTrue(test_list)




if __name__ == '__main__':
    unittest.main()
