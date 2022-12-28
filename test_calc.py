import calc
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,15),25)
        self.assertEqual(calc.add(15,15),30)

    def test_sub(self):
        self.assertEqual(calc.sub(20,10),10)
        self.assertEqual(calc.sub(90,30),60)

    def test_mul(self):
        self.assertEqual(calc.mul(2,7),14)
        self.assertEqual(calc.mul(3,5),15)

    def test_div(self):
        self.assertEqual(calc.div(10,2),5)
        self.assertEqual(calc.div(21,7),3)

    def test_Is(self):
        j=calc.add(2,3)
        self.assertIs(j,5)



if __name__ == "__main__":
    unittest.main()
