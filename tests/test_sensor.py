import unittest
import sys

sys.path.append('..')
import raspberry.modules.sensor as sensor

class TestSensor(unittest.TestCase):
    
    def test_getDhtData(self):
        self.assertIsInstance(sensor.getDhtData(), list)
        self.assertIsInstance(sensor.getDhtData()[0], float)
        self.assertIsInstance(sensor.getDhtData()[1], float)

if __name__ == '__main__':
    print unittest.main()
