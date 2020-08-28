import unittest
from name_function import get_formated_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formated_name = get_formated_name('steve', 'jobs')
        self.assertEqual(formated_name, 'Steve Jobs')


if __name__ == '__main__':
    unittest.main()
