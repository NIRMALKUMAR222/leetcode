class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0
        limit = 2**31 - 1 if sign == 1 else 2**31

        while x:
            digit = x % 10
            x //= 10

            if result > limit // 10:
                return 0

            if result == limit // 10 and digit > limit % 10:
                return 0

            result = result * 10 + digit

        return sign * result