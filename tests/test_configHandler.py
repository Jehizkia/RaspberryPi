import unittest
import ConfigParser
import sys

sys.path.append('..')
from raspberry.modules.configHandler import Configuration

class TestConfigHandlerRead(unittest.TestCase):

    def setUp(self):
        self.config = Configuration()
        self.config.savePath = '/home/pi/Desktop/test_rpiConfig.cfg'
        self.config.configRead.read(self.config.savePath)
        
    def test_getData_instance(self):        
        self.assertIsInstance(self.config.getData('app_data', 'rpi_id', 'int'), int)
        self.assertIsInstance(self.config.getData('app_data', 'room'), str)
        self.assertIsInstance(self.config.getData('app_data', 'float_test', 'float'), float)
        self.assertIsInstance(self.config.getData('app_data', 'bool_test' , 'bool'), bool)

    def test_getData_equal(self):
        self.assertEqual(self.config.getData('app_data', 'rpi_id', 'int'),1)
        self.assertEqual(self.config.getData('app_data', 'room'), 'H.1.110')
        self.assertEqual(self.config.getData('app_data', 'float_test', 'float'), 23.4)
        self.assertEqual(self.config.getData('app_data', 'bool_test', 'bool'), False)

    def test_configHasRequiredSections(self):
        self.assertTrue(self.config.configHasRequiredSections())
        
        self.config.savePath = '/home/pi/Desktop/test_rpiConfig_incomplete.cfg'
        self.config.configRead = ConfigParser.RawConfigParser()
        self.config.configRead.read(self.config.savePath)
        
        self.assertFalse(self.config.configHasRequiredSections())

suite = unittest.TestLoader().loadTestsFromTestCase(TestConfigHandlerRead)
unittest.TextTestRunner(verbosity=2).run(suite)
