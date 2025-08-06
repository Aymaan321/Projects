class IntegerToRoman:

    def __init__(self):
        self.roman_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

    def convert_to_roman(self, num):
        roman_num = ''
        for i in sorted(self.roman_map.keys(), reverse=True):
            while num >= i:
                roman_num += self.roman_map[i]
                num -= i
        return roman_num


if __name__ == '__main__':
    int_to_roman = IntegerToRoman()
    number = int(input("Enter an integer: "))
    roman_numeral = int_to_roman.convert_to_roman(number)
    print(f"The roman numeral of {number} is {roman_numeral}")
