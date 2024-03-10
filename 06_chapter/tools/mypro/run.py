import unittest

suit = unittest.defaultTestLoader.discover("test_dir", "test_*.py")

runner = unittest.TextTestRunner()
runner.run(suit)

