from  simp import Simp
class Comp(object):

    def sum_of_digits(self,number):
        """shlomo mhadker
            1.2.23
            function that get a number and sum all its digits function will not work if  add or sub func didnt activeted before
            """

        if not Simp.function_flag:
            raise Exception
        sum = 0
        while number != 0:
            sum += number % 10
            number = number // 10
            Simp.function_flag=False
        return sum

    def ispl(self,number):
        """shlomo mhadker
            1.2.23
            function that check if a number is palindrome function will not work if  add or sub func didnt activeted before"""

        if not Simp.function_flag:
            raise Exception
        Simp.function_flag = False
        return str(number) == str(number)[::-1]
