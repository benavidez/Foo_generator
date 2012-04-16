'''
Created on Apr 16, 2012

@author: eduardob
'''
import unittest
import foo_gen

class Test(unittest.TestCase):    
    def testFoo(self):
        str = ''
        for i in foo_gen.foo(20):
            str = str + i     
        print str       
        self.assertEqual(',,fizz,,buzz,fizz,,,fizz,buzz,,fizz,,,fizzbuzz,,,fizz,,buzz,', str, '')
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
