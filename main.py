import unittest


# An iterator over the fibonacci sequence
class Fib:

    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


class TestFib(unittest.TestCase):

    # Test the first five numbers of fibonoacci sequence
    def test_five(self):
        fibs = Fib()
        first_five = [next(fibs) for _ in range(5)]
        self.assertEqual(first_five, [1, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
