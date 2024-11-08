from Tournament import Tournament as Event
from Tournament import Runner as Run
import unittest


class tour_Test(unittest.TestCase):
    def SetUp(self):
        self.Usain = Run(Usain, 10)
        self.Andrey = Run(Andrey, 9)
        self.Nick = Run(Nick, 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for place,name in cls.all_results.items():
            print(place,name)

    def test_try(self):
        Tournament = Event(90, self.Usain, self.Nick)
        tour_Test.all_result = Event.start()
        self.assertTrue(tour_Test.all_result[-1], Nick)

if __name__ == "__name__":
    unittest.main()
