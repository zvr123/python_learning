"""Practice returning one liner with loops and lists inside """

#Basic
def add_5(numbers):
    return [new_numbers+5 for new_numbers in numbers]

def num_2_str(numbers):
    return [str(new_numbers) for new_numbers in numbers]

def round_to_one_dec(numbers):
    return [round(new_numbers,1) for new_numbers in numbers]

#filtering
#       [new_item for item in old_list if some_condition]
def odd_nums(numbers):
    return [odds for odds in numbers if odds%2==1]

def chars_strs(strings):
    return [three_chars for three_chars in strings if len(three_chars)>3]

def negative_nums(numbers):
    return [negative for negative in numbers if negative<0]

#filtering + transformation
#       [new_item_with_function for item in old_list if some_condition]
def even_nums_squared(numbers):
    return [even**2 for even in numbers if even%2==0]

def lower_cap(strings):
    return [lower_cap.casefold() for lower_cap in strings if lower_cap[0]==lower_cap[0].upper()]

def a_words(strings):
    return [len(a_words) for a_words in strings if a_words.find('a')==True]

# Conditional expressions
#       [new_value_if_true if condition else new_value_if_false for item in nums]
def negative_zeroes(numbers):
    return [0 if negative<0 else negative for negative in numbers]

def even_odd(numbers):
    return ['even' if num%2==0 else 'odd' for num in numbers]

def end_with_y(strings):
    return ['!' if is_y[-1]=='y' else is_y for is_y in strings]

# Nested list Comprehenssion
#       You need two for parts in the comprehension.
#           [item for inner_list in outer_list for item in inner_list]
def flatten_lists(lists):
    return [element for lst in lists for element in lst]

def flat_times_ten(nested_numbers):
    return [number*10 for sublist in nested_numbers for number in sublist]

def times_ten(nested_numbers):
    return [[num*10 for num in sub_list] for sub_list in nested_numbers]

def row_sum(nested_numbers):
    return [sum(sub_list) for sub_list in nested_numbers]

# Slightly Tricky
def initials(names):
    #return [name for name in names]     #['John Doe', 'Alice Smith']
    #return [name.split() for name in names]     #[['John', 'Doe'], ['Alice', 'Smith']]
    #return [word[0] for name in names for word in name.split() ]        # ['J', 'D', 'A', 'S']
    return ["".join([word[0] for word in name.split()]) for name in names]      #['JD', 'AS']



print (add_5([1,2,3]))
print (num_2_str([1,2,3]))
print (round_to_one_dec([1.111,2.222,3.333]))

print (odd_nums([1,2,3,4]))
print (chars_strs(["aaa","bb","cccc","dddddddddd","eee"]))
print (negative_nums([1,-2,-3,4]))

print (even_nums_squared([1,-2,-3,4]))
print (lower_cap(["Aaa","bB","Cccc","dddddDdddd","Eee"]))
print (a_words(["Aaa","bB","Cccc","dddddDdddd","Eee"]))

print (negative_zeroes([1,-2,-3,4]))
print (even_odd([1,2,3,4]))
print (end_with_y(["Aaya","bBy","Ccccy","dddddDddddY","Eeey"]))

print (flatten_lists([[1,-2],[-3,4]]))
print (flat_times_ten([[1,-2],[-3,4]]))
print (times_ten([[1,-2],[-3,4]]))
print (row_sum([[1,-2],[-3,4]]))

print (initials(["John Doe", "Alice Smith"]))
