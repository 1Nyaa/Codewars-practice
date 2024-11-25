
# Write two functions that convert a roman numeral to and from an integer value.
# Multiple roman numeral values will be tested for each function.

# Modern Roman numerals are written by expressing each digit separately
# starting with the left most digit and skipping any digit with a value of zero.

numbs = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}


class RomanNumerals:


    @staticmethod
    def to_roman(val: int) -> str:

        answ = ''

        for v, k in numbs.items():
            while val >= k:
                answ += v
                val -= k
        return answ

    @staticmethod
    def from_roman(roman_num: str) -> int:

        answ = 0
        pr_numb = 0

        for i in range(len(roman_num) - 1, -1, -1):
            numb = numbs.get(roman_num[i])
            if numb < pr_numb:
                answ -= numb
            else:
                answ += numb
            pr_numb = numb
        return answ
