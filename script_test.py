import unittest
from script import forbidden_pair, Receiver, get_receiver_list, get_pairings

class TestScriptFunctions(unittest.TestCase):

    def test_forbidden_pair1(self):
        p1 = Receiver(["Mikołaj", "Fitowski", "blabla", "blabla"])
        p2 = Receiver(["Klaudia", "Kowal", "blabla", "blabla"])
        self.assertTrue(forbidden_pair(p2, p1))
    
    def test_forbidden_pair2(self):
        p1 = Receiver(["Szymon", "Fus", "blabla", "blabla"])
        p2 = Receiver(["Katarzyna", "Kwiatkowska", "blabla", "blabla"])
        self.assertTrue(forbidden_pair(p2, p1))

    def test_get_pairings(self):
        receivers = get_receiver_list()
        pairings = list(get_pairings(receivers))

        for i, j in pairings:
            self.assertFalse(forbidden_pair(i, j))



if __name__ == '__main__':
    unittest.main()