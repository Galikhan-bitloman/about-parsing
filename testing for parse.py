import unittest
from parse import get_number_from_site, get_amountprice_from_site


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.get_dataset = get_number_from_site()
        self.get_dataset1 = get_amountprice_from_site()


    def test_get_number_from_site(self):
        self.assertEqual(self.get_dataset, '')

    def test_get_amountprice_from_site(self):
       self.assertEqual(self.get_dataset1, None)

if __name__ == '__main__':
    unittest.main()
