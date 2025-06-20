import unittest

from src.SemanticNetsAgent import State


class StateTest(unittest.TestCase):

    def test_get_signature(self):
        state = State(1, 1, 1, 1, "left")
        self.assertEqual("ls:1,lw:1,rs:1,rw:1,d:left", state.get_signature())

    def test_isvalid(self):
        state = State(2, 3, 1, 0, "left")
        res = state.is_valid()
        self.assertEqual(False, res)

    def test_isvalid1(self):
        state = State(2, 1, 1, 2, "left")
        res = state.is_valid()
        self.assertEqual(False, res)

    def test_isvalid2(self):
        state = State(0, 1, 3, 2, "left")
        res = state.is_valid()
        self.assertEqual(True, res)

    def test_isvalid3(self):
        state = State(3, 0, 0, 3, "left")
        res = state.is_valid()
        self.assertEqual(True, res)
