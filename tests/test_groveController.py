import unittest
import sys

sys.path.append('..')
from raspberry.modules.groveController import GroveController

class TestGroveInputs(unittest.TestCase):

    def setUp(self):
        self.groveController = GroveController()
    
    def test_ifCurrentView(self):
        self.assertTrue(self.groveController.ifCurrentView(1,1))
        self.assertFalse(self.groveController.ifCurrentView(1,3))
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestGroveInputs)
unittest.TextTestRunner(verbosity=2).run(suite)
