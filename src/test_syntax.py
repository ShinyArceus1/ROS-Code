import unittest as ut
import syntax as s

class TestCode(ut.TestCase):

    def test_colourcode(self):
        self.assertEqual(s.colourcode("#212121", "hex", True), '#212121')

    def test_changecolour(self):
        self.assertEqual(str(s.changecolour("#212121", "red", 10)), '#192121')

    def test_catwalk(self):
        self.assertEqual(s.catwalk("this     is    some    text"), "this is some text")

    def test_isprime(self):
        self.assertEqual(s.isprime(1), False)
        self.assertEqual(s.isprime(27), False)
        self.assertEqual(s.isprime(52), False)
        self.assertEqual(s.isprime(7), True)
        self.assertEqual(s.isprime(3), True)

if __name__ == '__main__':
    ut.main()
