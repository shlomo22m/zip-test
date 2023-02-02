import pytest
from  service import Service
from comp import Comp
from simp import Simp
from  tools.col import Col
from dotenv import load_dotenv
import os




load_dotenv()
log = Service()
num1=int(os.getenv('NUM1'))
num2=int(os.getenv('NUM2'))
add_result=int(os.getenv('RESULT_ADD'))
sub_result=int(os.getenv('RESULT_SUB'))
sum_of_digit=int(os.getenv('SUM_OF_DIGIT'))
sum_of_digit_result=int(os.getenv('SUM_OF_DIGIT_RESULT'))
ispl=int(os.getenv('ISPL'))
ispl_result=os.getenv('ISPL_RESULT')
files=os.getenv('FILES')
files=list(map(str, files.split(',')))
exception_pass=os.getenv('EXCEPTION_PASS')
exception_fail=os.getenv('EXCEPTION_FAIL')
exception_rooms=os.getenv('EXCEPTION_ROOMS_TESTS')
test_pass=os.getenv('TEST_PASS')
test_fail=os.getenv('TEST_FAIL')

s=Simp()
f=Col()

@pytest.fixture()
def comp():
    return Comp()



def test_add():
    try:
        assert s.add(num1,num2)==add_result
        log.testwriteToFile(f'add of digit {test_pass} expected {add_result} actual {num1+num2}')
    except:
        log.testwriteToFile(f'add of digit {test_fail} expected {add_result} actual {num1+num2}')

def test_sub():
    try:
        assert s.sub(num1,num2)==sub_result
        log.testwriteToFile(f'sub {test_pass} expected {sub_result} actual {num1-num2}')
    except:
        log.testwriteToFile(f'sub {test_fail} expected {sub_result} actual {num1-num2}')


def test_sum_of_digits(comp):
    Simp.function_flag = True
    #result=comp.sum_of_digits(sum_of_digit)
    try:
        assert comp.sum_of_digits(sum_of_digit) == sum_of_digit_result
        log.testwriteToFile(f'sum of digit {test_pass} expected {sum_of_digit_result}')
    except:
        log.testwriteToFile(f'sum of digit {test_fail} expected {sum_of_digit_result}')


    try:
        Simp.function_flag = True
        with pytest.raises(Exception):
             assert comp.sum_of_digits(sum_of_digit)==sum_of_digit_result
        log.testwriteToFile(f'sum of digit {exception_pass}')
    except:
        log.testwriteToFile(f'sum of digit {exception_fail}')


def test_ispl(comp):
     Simp.function_flag=True
     try:
        assert comp.ispl(ispl) == True
        log.testwriteToFile(f'ispl {test_pass}')
     except:
         log.testwriteToFile(f'ispl {test_fail}')

     try:
        Simp.function_flag = False
        with pytest.raises(Exception):
             assert comp.ispl(ispl)==ispl_result
        log.testwriteToFile(f'ispl {exception_pass}')
     except:
         log.testwriteToFile(f'ispl {exception_fail}')

def test_compress():
    try:
        assert f.compress(files)==1
        log.testwriteToFile(f'compress {test_pass}')
    except:
        log.testwriteToFile(f'compress {test_fail}')

    try:
        with pytest.raises(Exception):
            assert f.compress(files)==1
        log.testwriteToFile(f'compress {exception_pass}')
    except:
        log.testwriteToFile(f'compress {exception_fail}')