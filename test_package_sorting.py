import unittest
from package_sorting import sort

class TestPackageSorting(unittest.TestCase):
    
    def test_standard_package(self):
        # Not bulky or heavy
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        
    def test_bulky_by_volume(self):
        # Bulky due to volume
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        
    def test_bulky_by_dimension(self):
        # Bulky due to one big dimension
        self.assertEqual(sort(160, 50, 50, 10), "SPECIAL")
        
    def test_heavy_package(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        
    def test_rejected_package(self):
        # Both heavy and bulky
        self.assertEqual(sort(150, 150, 150, 30), "REJECTED")
        
    # Edge cases at the boundaries
    def test_edge_cases(self):
        # At volume threshold
        self.assertEqual(sort(100, 100, 100, 15), "SPECIAL")
        
        # At dimension threshold
        self.assertEqual(sort(150, 50, 50, 15), "SPECIAL")
        
        # At mass threshold
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        
if __name__ == '__main__':
    unittest.main()