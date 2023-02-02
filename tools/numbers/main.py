from simp import Simp
from comp import Comp
import sys
from dotenv import load_dotenv
import os
load_dotenv()
from tools.col import Col

if __name__ == '__main__':
    s=Simp()
    c=Comp()
    c2=Col()
    #print(s.add(3,4))
    print(s.sub(3,3))
    try:
        print(c.sum_of_digits(234))
    except:
        print('must use function add or sub first')
    #print(c.ispl(312133))
    ls=['a.txt','b.txt']
    print(c2.compress(ls))