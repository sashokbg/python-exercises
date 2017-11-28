import math

class Solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        digits = int(math.log10(num))+1

        if digits == 1:
            return num

        result = 0
        
        for i in range(digits):
            digit = num - (num % 10**i)

            print('digit = {}'.format(digit))

            result += digit
            

        self.addDigits(result)
