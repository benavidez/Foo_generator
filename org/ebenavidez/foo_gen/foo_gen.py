'''
Created on Apr 16, 2012

@author: eduardob
'''

#n is the sequence of number 1..n to check if div by 3 or 5
def foo(n):   
    for i in range(1, n+1):
        ret = ''
        if i != 0:            
            if i % 3 == 0:
                ret += 'fizz'
            if i % 5 == 0:
                ret += 'buzz'  
        yield ret + ','
 