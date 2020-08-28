import unittest
from name_function import get_formated_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formated_name = get_formated_name('steve', 'jobs')
        self.assertEqual(formated_name, 'Steve Jobs')

    def test_fisrt_middle_last_name(self):
        formated_name = get_formated_name('mzp', 'mao', 'xxx')
        self.assertEqual(formated_name, 'Mzp Mao Xxx')


if __name__ == '__main__':
    unittest.main()
