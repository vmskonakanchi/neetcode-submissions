class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        seen_numbers = set()

        for i in str(n):
            total = total + (int(i) ** 2)
        
        while total != 1:
            if total in seen_numbers:
                return False

            seen_numbers.add(total)

            if total >= 10:
                # we know that there is need to split and compute
                str_num = str(total)
                total = 0
                for i in str_num:
                    total = total + (int(i) ** 2)
            else:
                # we have less then 10 number so compute it normally
                total = total ** 2

        return True