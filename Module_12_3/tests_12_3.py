import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        Ralf = Runner('Ralf')
        for i in range(10):
            Ralf.walk()
        self.assertEqual(Ralf.distance,50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        Usain = Runner('Usain')
        for i in range(10):
            Usain.run()
        self.assertEqual(Usain.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Pupa= Runner('Pupa')
        Lupa = Runner('Lupa')
        for i in range(10):
            Pupa.run()
            Lupa.walk()
        self.assertNotEqual(Pupa.distance, Lupa.distance)

if __name__ == '__main__':
    unittest.main()

from Tournament import Tournament as Event
from Tournament import Runner as Run


class tour_Test(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.Usain = Run("Usain", 10)
        self.Andrey = Run("Andrey", 9)
        self.Nick = Run("Nick", 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_try(self):
        Tournament = Event(90, self.Usain, self.Nick)
        tour_Test.all_result = Tournament.start()
        self.assertTrue(tour_Test.all_result[2], self.Nick)

    @classmethod
    def tearDownClass(cls):
        for place,name in cls.all_results.items():
            print(place,name)