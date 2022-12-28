#assertIs()
#assertIsNone()
#assertIsNotNone()

import unittest

class sample_unittest_Class(unittest.TestCase):
    def test_basicunittest(self):
        self.assertTrue(True)

    def setup(self):
        pass

#returns true if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')

#returns true if it is upper
    def test_upper(self):
        self.assertEqual("VASAVI".isupper(),False)

#returns if the concat is True
    def test_concat(self):
        self.assertEqual("a"+"b", "ab")

#Returns True if the string is in upperCase
#else returns false
    def test_isupper(self):
        self.assertTrue("VASAVI".isupper())
        self.assertFalse("vasavi".isupper())

#returns true if the string is stripped and
#matches the given output
    def test_strip(self):
        s="python"
        self.assertEqual(s.strip(), 'py'+'thon')

#returns true if the string splits and matches
#the given output
    def test_split(self):
        vasavi=""



