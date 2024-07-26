import unittest

from py2plpy import transform

class Test(unittest.TestCase):

    def test(self):
        r = transform('py2plpy/tests/fixture.py')
        with open('py2plpy/tests/fixture.sql') as f:
            self.assertEqual(r, f.read())


if __name__ == '__main__':
    unittest.main()