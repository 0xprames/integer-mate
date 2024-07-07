class I256:
    def __init__(self, bits):
        self.bits = bits

def wrapping_add(num1: I256, num2: I256) -> I256:
    sum_bits = num1.bits ^ num2.bits
    carry = (num1.bits & num2.bits) << 1

    while carry != 0:
        a = sum_bits
        b = carry
        sum_bits = a ^ b
        carry = (a & b) << 1

    return I256(sum_bits)

