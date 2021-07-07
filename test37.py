import unittest
from f37_Task import Shaxs
#from d37_2_task import Talaba


class Shahstests(unittest.TestCase):

    def setUp(self):
        ism="Shukurali"
        familiya ="Rezamonov"
        passport = 4990299
        tyil=2002
        self.shaxs1 = Shaxs(ism,familiya,passport,tyil)
    def test_1(self):

        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.tyil)
unittest.main()
# class Talaba_1(unittest.Case):
#     def setUp(self):
#         ism = "Anvar"
#         familiya ="Saidov"
#         passport = 47577845
#         idraqam= 72344233234234234
#         self.talaba1= Talaba(ism,familiya,passport,idraqam)
#     def test1(self):
#         self.assertIsNotNone(self.talaba1.ism)

    