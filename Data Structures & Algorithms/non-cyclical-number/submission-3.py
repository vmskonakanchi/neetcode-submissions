class Solution:
    def isHappy(self, n: int) -> bool:
        str_num = str(n)
        total = 0
        iters = 0

        seen_numbers = {}

        for i in str_num:
            total = total + (int(i) ** 2)
        
        while total != 1:
            if total in seen_numbers:
                return False
                
            seen_numbers[total] = True

            if total >= 10:
                print('total greater than 10', total)
                # we know that there is need to split and compute
                str_num = str(total)
                total = 0
                for i in str_num:
                    total = total + (int(i) ** 2)
            else:
                print('total less than 10', total)
                # we have less then 10 number so compute it normally
                total = total ** 2


        return True