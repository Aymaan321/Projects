tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

def tuple_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

result = tuple_product(tup1)
print('The product of the 1st tuple elements is:', result)
result2 = tuple_product(tup2)
print('The result of the 2nd tuple elements is:', result2)
