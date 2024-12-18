import Runner
import unittest

class runner_test(unittest.TestCase):
    
    def test_run(self):
        unit = Runner.Runner("Ruslan")
        for _ in range(10):
            unit.run()
        self.assertEqual(unit.distance, 100)
        
    def test_walk(self):
        unit = Runner.Runner("Ruslan")
        for _ in range(10):
            unit.run()
        self.assertEqual(unit.distance, 100)


    def test_challenge(self):
        unit = Runner.Runner("Ruslan")
        unit_1 = Runner.Runner("Ruslan")
        for _ in range(10):
            unit.walk()
            unit_1.run()
        self.assertNotEqual(unit.distance, unit_1.distance)

if __name__ == "__main__":
    unittest.main()
