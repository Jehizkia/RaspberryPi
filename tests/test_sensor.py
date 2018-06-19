import unittest
import sys

sys.path.append('..')
from raspberry.modules.sensor import Sensor

class TestSensor(unittest.TestCase):

    def setUp(self):
        self.sensor = Sensor()
    
    def test_getDhtData(self):
        print self.sensor.getDhtData()
        self.assertIsInstance(self.sensor.getDhtData(), list)
        self.assertIsInstance(self.sensor.getDhtData()[0], float)
        self.assertIsInstance(self.sensor.getDhtData()[1], float)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSensor)
unittest.TextTestRunner(verbosity=2).run(suite)
