'''
Testing guess_2b using unittest

The trick here is to use the near-magical "patch" decorator from
unittest.mock to replace random.randint and test with specific values.

We do not test the class Guesser, leaving it as something for
someone learning from this code to try on their own, using
the current tests as a model.

'''

import unittest
from unittest import mock

import guess_2b  # module to be tested


class TestsChooser(unittest.TestCase):

    @mock.patch('random.randint')
    def test_init(self, randint_call):
        for value in [1, 42, 50, 100]:
            randint_call.return_value = value
            ch = guess_2b.Chooser()
            self.assertEqual(ch.number, value)

    @mock.patch('random.randint')
    def test_guess_correct(self, randint_call):
        for value in [1, 42, 50, 100]:
            randint_call.return_value = value
            ch = guess_2b.Chooser()
            self.assertEqual(ch.analyze(value), "correct")

    @mock.patch('random.randint')
    def test_guess_low(self, randint_call):
        for value in [1, 42, 50, 100]:
            randint_call.return_value = value
            ch = guess_2b.Chooser()
            self.assertEqual(ch.analyze(value - 1), "low")

    @mock.patch('random.randint')
    def test_guess_high(self, randint_call):
        for value in [1, 42, 50, 100]:
            randint_call.return_value = value
            ch = guess_2b.Chooser()
            self.assertEqual(ch.analyze(value + 1), "high")

if __name__ == '__main__':
    unittest.main()
