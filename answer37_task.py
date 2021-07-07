
import unittest
from l37_Task import developer

class developer_tests(unittest.TestCase):
    def get_info(self):
        dev1 = developer("Asliddin","Eliboyev",2001,None,"norm",200,__price = "Software")
        self.assertIsNotNone(dev1.yoshi)
        self.assertIsNotNone(dev1.ism)
        self.assertEqual("Software",dev1.__price())
unittest.main()
