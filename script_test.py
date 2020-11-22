import unittest
from Santa import Santa, Receiver

class TestScriptFunctions(unittest.TestCase):
    santa = Santa()

    def test_forbidden_pair1(self):
        p1 = Receiver(["John", "Smith", "blabla", "blabla"])
        p2 = Receiver(["Jan", "Nowak", "blabla", "blabla"])
        self.assertTrue(self.santa.forbidden_pair(p1, p2))
    
    def test_forbidden_pair2(self):
        p1 = Receiver(["May", "Hew", "blabla", "blabla"])
        p2 = Receiver(["Janurary", "West", "blabla", "blabla"])
        self.assertTrue(self.santa.forbidden_pair(p2, p1))

    def test_get_pairings(self):
        self.santa.get_receiver_list()
        for i in range(10):
            pairings = list(self.santa.get_pairings())

            for i, j in pairings:
                self.assertFalse(self.santa.forbidden_pair(i, j))


if __name__ == '__main__':
    unittest.main()