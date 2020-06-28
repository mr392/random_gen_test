import unittest
import RandomGenerators.RandomGenerators

class MyTestCase(unittest.TestCase):
    def test_something(self):
        """List evaluates to False if empty"""
        test_list = RandomGenerators.RandomGenerators.list_generator(2)

        self.assertTrue(test_list)





if __name__ == '__main__':
    unittest.main()
