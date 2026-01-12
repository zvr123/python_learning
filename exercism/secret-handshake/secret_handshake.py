binary_nums = [1,2,4,8,16]
secret_action = ["wink","double blink","close your eyes","jump","reverse"] # reverse the order of operations

def to_base_ten(str_digits):
    result_num = 0
    digits_len = len(str_digits)
    for i in range(digits_len,0,-1):
        result_num += int(str_digits[i-1]) * 2**(digits_len-i)
        print (i-1, str_digits[i-1], result_num)
    return result_num    

def commands(binary_str):
    result_actions = []
    is_reverse = False

    for i in range(len(binary_str)-1,-1,-1): # -1 as the last loop count is actually 0
        if (binary_str[i] == '1'):
            if (i == 0):
                result_actions.reverse()
            else:
                result_actions.append(secret_action[4-i]) #4 = len(binary_num)
    return result_actions


print (commands("10011"))