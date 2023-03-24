import unittest
import cap


class Mytests(unittest.TestCase):
    """
    units tests for the function cap_func()
    """

    def test_cap_one_word(self):
        input_text = 'python'
        result = cap.cap_func(input_text)
        self.assertEqual(result, 'Python')

    def test_cap_multiple_words(self):
        input_text = 'learning python'
        result = cap.cap_func(input_text)
        self.assertEqual(result, 'Learning python')


if __name__ == '__main__':
    unittest.main()
