
import unittest


def load_tests():
    suite=unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(test_HttpApiV1Repository.TestHttpApiV1Repository_test1))

    return suite

if __name__ == "__main__":
    runner=unittest.TextTestRunner(verbosite=2)
    runner.run(load_tests())