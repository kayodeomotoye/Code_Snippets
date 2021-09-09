def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    num_base = 2, 8
    func = bin(number), oct(number)
    converter = zip(num_base, func)
    first_digit = number // 216
    first_remainder = number % 216
    
    second_digit = first_remainder // 36
    second_remainder = first_remainder % 36

    third_digit = second_remainder // 6
    third_remainder = second_remainder % 6
    
    fourth_digit = third_remainder // 1
    fourth_remainder = third_remainder % 1

    for base_, func in converter:
        if base == 6:
            conv_number = (str(first_digit) + str(second_digit) +str(third_digit)
             + str(fourth_digit)).lstrip('0')
            return int(conv_number)
        elif base_ == base:
            return int(func[2:])



#pybites

def dec_to_base(number, base):
    if number < base:  # base case
        return number
    else:
        return 10 * dec_to_base(number//base, base) + (number % base)


if __name__ == '__main__':
    nums = [24, 177, 256, 1024, 2020]

    for num in nums:
        print(dec_to_base(num, 8))

    
    





    