from unittest import TextTestRunner, TestLoader
from QA1 import SampleTest
from QA2 import SampleTest2

suite = TestLoader().loadTestsFromTestCase(SampleTest)
suite.addTest(TestLoader().loadTestsFromTestCase(SampleTest2))

runner = TextTestRunner(verbosity=3)

results = runner.run(suite)
