from unittest import TextTestRunner, TestLoader
from QAPI1 import SampleTest
from QAPI2 import SampleTest2

"""
The endpoints were not reachable. I tested using postman to verify. Anyway I have included my test scripts.
"""

suite = TestLoader().loadTestsFromTestCase(SampleTest)
suite.addTest(TestLoader().loadTestsFromTestCase(SampleTest2))

runner = TextTestRunner(verbosity=3)

results = runner.run(suite)
