class integer:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        if insinsitance(other, integer):
            return integer(self.num + other.num)
        else:
            raise ValueError('Invalid operator for addition: {}'.format(type(other)))
    
    def __sub__(self, other):
        if isinstance(other, integer):
            return integer(self.num - other.num)
        else:
            raise ValueError('Invalid operator for subtraction: {}'.format(type(other)))

    def __mul__(self, other):
        if isinstance(other, integer):
            return integer(self.num * other.num)
        else:
            raise ValueError('Invalid operator for multiplication: {}'.format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, integer):
            if other.num == 0:
                raise ValueError('Cannot divide by 0.')
            return integer(self.num // other.num)
        else:
            raise ValueError('Invalid operator for division: {}'.format(type(other)))


num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))


result_add = num1 + num2
print('Addition Result:', result_add)

result_sub = num1 - num2
print('Subtraction Result:', result_sub)

result_mul = num1 * num2
print('Multiplication Result:', result_mul)

result_div = num1 // num2
print('Division Result:', result_div)

combined_result = num1 + num2 - num2 * num1 / num2
print('Combined Result:', combined_result)


