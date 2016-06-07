from .program import run

import unittest
from unittest.mock import Mock, patch

class LookupMavenTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_run(self):
        pass

    def test_new_contribution(self):
        pass

    def test_run_no_contribution(self):
        pass

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(LookupMavenTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
