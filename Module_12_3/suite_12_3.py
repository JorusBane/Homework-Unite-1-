import unittest
import Module_12_2

tour_test = unittest.TestSuite()
tour_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.tour_Test))

runner = unittest.TextTestRunner()
runner.run(tour_test)

runner = unittest.TextTestRunner(verbosity=2)