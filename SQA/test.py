import unittest
import Five
class testFib(unittest.TestCase):
    def test_1(self):
        result= Five.fib(1)
        self.assertEquals(result,0,"Bad Code Bud")

class testAdd(unittest.TestCase):
    def test_1(self):
        result= Five.sum(1,2)
        self.assertEquals(result,3,"Bad Code Bud")

class testSub(unittest.TestCase):
    def test_1(self):
        result= Five.sub(1,2)
        self.assertEquals(result,-1,"Bad Code Bud")

class testMul(unittest.TestCase):
    def test_1(self):
        result= Five.mul(1,2)
        self.assertEquals(result,2,"Bad Code Bud")

class testDiv(unittest.TestCase):
    def test_1(self):
        result= Five.div(1,2)
        self.assertEquals(result,1/2,"Bad Code Bud")


def fibSuite():
    suite = unittest.TestSuite()
    suite.addTest(testFib('test_1'))
    return suite
def sumSuite():
    suite = unittest.TestSuite()
    suite.addTest(testAdd('test_1'))
    return suite
def subSuite():
    suite = unittest.TestSuite()
    suite.addTest(testSub('test_1'))
    return suite
def mulSuite():
    suite = unittest.TestSuite()
    suite.addTest(testMul('test_1'))
    return suite
def divSuite():
    suite = unittest.TestSuite()
    suite.addTest(testDiv('test_1'))
    return suite
def main():
    suite = unittest.TestSuite([fibSuite(), sumSuite(), subSuite(), mulSuite(), divSuite()])
    unittest.TextTestRunner(verbosity = 2).run(suite)
if __name__ == '__main__':
    main()
