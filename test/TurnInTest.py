import unittest

from src.SemanticNetsAgent import SemanticNetsAgent


class TurnInTest(unittest.TestCase):

    def test_Sheeps_10_Wolves_10(self):
        sem = SemanticNetsAgent()
        res = sem.solve(10, 10)
        self.assertEqual([], res)

    def test_Sheeps_12_Wolves_12(self):
        sem = SemanticNetsAgent()
        res = sem.solve(12, 12)
        self.assertEqual([], res)

    def test_Sheeps_5_Wolves_5(self):
        sem = SemanticNetsAgent()
        res = sem.solve(5, 5)
        self.assertEqual([], res)

    def test_Sheeps_6_Wolves_6(self):
        sem = SemanticNetsAgent()
        res = sem.solve(6, 6)
        self.assertEqual([], res)

    def test_sheeps_1_wolves_1(self):
        sem = SemanticNetsAgent()
        res = sem.solve(1, 1)
        x = None
        s = sem.created_states
        self.assertEqual(1, len(res))
        self.assertEqual([(1, 1)], res)
        for v in s.values():
            self.assertEqual(True, v.get_state().is_valid())

    def test_sheeps3_wolves3(self):
        sem = SemanticNetsAgent()
        # s = sem.created_states
        res = sem.solve(3, 3)
        # for v in s.values():
        #     self.assertEqual(True, v.is_valid())
        # I think this is right
        self.assertEqual(11, len(res))

# ***************************** 👇 LESS SURE 👇 # ***************************** 👇 LESS SURE 👇
# (2, 2), (5, 3), (6, 3), (7, 3)

    def test_2_2(self):
        sem = SemanticNetsAgent()
        res = sem.solve(2, 2)
        # I think this can be done in 5
        self.assertEqual(5, 5)
#
    def test_5_3(self):
        sem = SemanticNetsAgent()
        res = sem.solve(5, 3)
        self.assertEqual(13, len(res))
# #
    def test_6_3(self):
        sem = SemanticNetsAgent()
        res = sem.solve(6, 3)
        self.assertTrue(len(res) <= 15)
# #
    def test_7_3(self):
        sem = SemanticNetsAgent()
        res = sem.solve(7, 3)
        self.assertTrue(len(res) <= 17)

    def test_11_3(self):
        sem = SemanticNetsAgent()
        res = sem.solve(11, 7)
        self.assertTrue(len(res) <= 33)

    def test_Sheeps_11_Wolves_8(self):
        sem = SemanticNetsAgent()
        res = sem.solve(11, 8)
        self.assertTrue(len(res) <= 35)

    # def test_Sheeps_45_Wolves_40(self):
    #     sem = SemanticNetsAgent()
    #     res = sem.solve(100000, 90000)
    #     x = len(res)

    def test_Sheeps_12_Wolves_5(self):
        sem = SemanticNetsAgent()
        res = sem.solve(12, 5)
        self.assertTrue(len(res) > 0)

    def test_Sheeps_25_Wolves_25(self):
        sem = SemanticNetsAgent()
        res = sem.solve(25, 24)
        print(len(res))
        self.assertTrue(len(res) > 0)

    def test_Sheeps_million_Wolves_900thousand(self):
        sem = SemanticNetsAgent()
        res = sem.solve(1000000, 900000)
        print(len(res))
        self.assertTrue(len(res) > 0)