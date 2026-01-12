
def check_errors(input_base, digits, output_base):
    # for input.
    if (input_base < 2):
        raise ValueError("input base must be >= 2")

    # or, for output.
    if (output_base < 2):
        raise ValueError("output base must be >= 2")
    
    # another example for input.
    for i in range(len(digits)):
        if ((digits[i] < 0 ) or (digits[i] >= input_base)):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    # a different approach for the for loop above
    # if any(d >= input_base for d in digits):
    #     raise ValueError("all digits must satisfy 0 <= d < input base")
        
    # if any(d < 0 for d in digits):
    #     raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # number = sum(d*input_base**i for i,d in enumerate(digits[::-1]))
    # if number == 0:
    #     return [0]

def rebase(input_base, digits, output_base):
    check_errors(input_base, digits, output_base)

    number_base_ten = in_base_ten(input_base, digits)
    return in_output_base(number_base_ten, output_base)

def in_base_ten(input_base, digits):
    result_num = 0
    digits_len = len(digits)
    for i in range(digits_len,0,-1):
        result_num += int(digits[digits_len-i] * input_base**(i-1))
        print (i, result_num)
    return result_num
    
def in_output_base(in_base_ten, output_base):
    digits = []
    number = in_base_ten

    while int(number)/output_base > 0:
        digit = int(number) % output_base
        print ("digit: ",digit)
        digits.append(digit)
        number = int(number)/output_base
        print ("number: ",number)
    if number == 0:
        print ("number: ",number)
        digits.append(number)

    digits.reverse()
    return digits


print (rebase(10, [0], 2))
print (rebase(2, [1,0,1,0,1,0], 3))
print (rebase(3, [1,1,2,0], 10))