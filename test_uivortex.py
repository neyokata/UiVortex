# test_uivortex.py
"""
Tests for UiVortex module.
"""

import unittest
from uivortex import UiVortex

class TestUiVortex(unittest.TestCase):
    """Test cases for UiVortex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UiVortex()
        self.assertIsInstance(instance, UiVortex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UiVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
