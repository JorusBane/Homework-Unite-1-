import Tournament
import unittest


class tour_Test(unittest.TestCase):
    def SetUp(self):
        Usain = Runner(Usain, 10)
        Andrey = Andrey(Andrey, 9)
        Nick = Nick(Nick, 3)
    @classmethod
    def SetUpClass(cls):
        all_result = []


    def tearDown(self):
        place = 1
        for runner in all_result:
            print(f"{place}: {runner}.")
        place += 1

    def test_try(self):
        Tournament = Runner_and_tournament(90, Usain, Nick)
        all_result = Tournament.start()
        self.assertTrue(all_result[-1], Nick)

if __name__ == "__name__":
    unittest.main()