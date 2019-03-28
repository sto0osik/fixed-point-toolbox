import numpy as np


class FixedNum():
    def __init__(self, value, word_length, frac_bits):
        self.word_length = word_length
        self.frac_bits = frac_bits
        self.value = self.assign_type(value)

    def __repr__(self):
        return (f'Binary value: {np.binary_repr(self.value, width=self.word_length)}\n'+
        f'Decimal value: {self.value}\n'+
        f'Word length: {self.word_length}\n'+
        f'Fractional bits: {self.frac_bits}')

    def __add__(self, other):
        return FixedNum(self.value+other.value, self.word_length, self.frac_bits)

    def assign_type(self, value):
        if self.word_length == 8:
            assigned_type = np.int8(value)
        elif self.word_length == 16:
            assigned_type = np.int16(value)
        elif self.word_length == 32:
            assigned_type = np.int32(value)
        elif self.word_length == 64:
            assigned_type = np.int64(value)
        return assigned_type


if __name__ == '__main__':
    x = FixedNum(32000, 16, 1)
    y = FixedNum(32000, 16, 1)
    z = x + y
    print(z)
    print(type(z))
