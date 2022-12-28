from student import Student
import unittest

class TestStudent(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_email(self):
        print("test_email")
        student1=Student("Vasavi","konka",40)
        self.assertEqual(student1.email,'Vasavi.konka@gmail.com')
        student2=Student("Abhi","konka",50)
        self.assertEqual(student2.email,'Abhi.konka@gmail.com')

    def test_fullname(self):
        print("test_fullname")
        student1=Student("Vasavi","konka",40)
        self.assertEqual(student1.fullname,'Vasavi konka')

    def test_apply_bonus(self):
        print("test_apply_bonus")
        student1=Student("Vasavi","konka",40)
        self.assertEqual(student1.marks,50,40)
        student1.apply_bonus()
        self.assertEqual(student1.marks,60,60)

    def test_details(self):
        std1 = Student("Vasavi", "konka", 40)
        self.assertEqual(std1.someage,"")
        std1.details("3")
        self.assertEqual(std1.someage,"Vasavi.konka@gmail.comVasavi konka3")













if __name__ == "__main__":
    unittest.main(verbosity=2)




