import unittest
import calc_tests


testCases = []
testCases.append(calc_tests.CalcBasicTests)
testCases.append(calc_tests.CalcExTests)

testLoad = unittest.TestLoader()

suites = []
for tc in testCases:
    suites.append(testLoad.loadTestsFromTestCase(tc))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)

# calcTestSuite = unittest.TestSuite()
# calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcBasicTests))
# calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcExTests))
# print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(calcTestSuite)
