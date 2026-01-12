"""Practice returning one liner with loops and lists inside """

#Level 1 - Basic
def first(tuple):
    return tuple[0]

def last(tuple):
    return tuple[-1]

def middle(tuple):
    print (f"len={len(tuple)}")
    mid = int(len(tuple)//2)
    return tuple[mid]

def single(tuple):
    return type(tuple), tuple

def upper_tupple(tuple):
    for i in tuple:
        print (i.upper())
    return "DONE!"

#Level 2 - List conversions
def mod_tupple(tuple1, tuple2):
    list1 = list(tuple1)
    list2 = list(tuple2)
    list1[len(list1):len(list1)+1]=list2

    tuple1 = tuple(list1)
    return tuple1

def remove_duplicates(tuple1):
    list1 = []
    for t in tuple1:
        if t not in list1:
            list1.append(t)
    tuple1 = tuple(list1)
    return tuple1

def sort_tuple(tuple1):
    list1 = list(tuple1)
    list1.sort()
    tuple1 = tuple(list1)
    return tuple1

#level 3 - string conversions
def tuple2string(tuple1):
    string1 = ''
    for letter in tuple1:
        string1+=letter
 
    return string1

def sentance2words(sentance):
    words = sentance.split()
    tuple1 = tuple(words)

    return tuple1

def csv2tuple(csv_line):
    words = csv_line.split(',')
    tuple1 = tuple(words)

    return tuple1

#level 4 - Tuple Unpacking & Packing
def basic_unpack(tuple1):
    (a,b,c) = tuple1
    return (f"{tuple1} => {a},{b},{c}")

def swap(tuple1):
    (a,b) = tuple1
    tuple1 = (b,a)  # It's ok since tuple1 is actually a new tuple instance (with the same name)
    #tuple1[0] = b  => this is ERROR since it tries to change the original tuple
    return tuple1

def extended_swap(tuple1):
    a = tuple1[0]
    b = tuple1[-1]          # or tuple1[len(tuple)-1]
    middle = tuple1[1:-1]
    return (b,middle,a) 

def ignore_mid_values(tuple1):
    a = tuple1[0]
    b = tuple1[-1]          # or tuple1[len(tuple)-1]
    #middle = tuple1[1:-1]
    tuple1 = (a,b)
    return tuple1

#Level 5: Nested Tuples
def access_nested_data(nested_tuple):
    return nested_tuple[0], nested_tuple[1][0], nested_tuple[2][1]

def flatten_tuple(nested_tuple):
    tuple1 = ()
    for t in nested_tuple:
        # print (t)     (1,2) + (3,4) + (5, ) =>  (1, 2, 3, 4, 5)
        tuple1+=t
    return tuple1

#Level 6: Tuples in Logic & Algorithms
def tuple_counter(tuple1):
    tuple2 = ()
    final_tuple = ()
    for i in tuple1:
        if i not in tuple2:
            inner_tuple = (i, tuple1.count(i))
            tuple2+=inner_tuple
    for i in range(0,len(tuple2),2):
        final_tuple += (tuple2[i:i+2],)
    return final_tuple

#level 7: Advanced Tuple Usage
def immutable_challenge(tuple1):
    list2 = []
    tuple2 = ()

    list2 = list(tuple1)
    list2[1] = 99
    tuple2 = tuple(list2)
    return tuple2

def myScore(num):
    return num[0][1]
def tuple_sorting_by_score(tuple1):
    tuple2 = ()
    list_scores = list(tuple1)
    list_scores.sort(key=myScore)  #from upper to lower scores => (key=myScore, reverse=True)
    tuple2 = tuple(list_scores)
    return tuple2

def combined_lists_tuple(names, scores):
    combined_tuple = ()
    for i in range(len(names)):
        inner_tuple = (names[i], scores[i])
        combined_tuple += (inner_tuple, )
    return combined_tuple

def temp_stats_tuple(tuple1):
    ave_temp = 0
    min_temp = 100
    max_temp = 0 
    list_temps = list(tuple1)
    count = len(list_temps)

    for i in range(len(list_temps)):
        ave_temp += list_temps[i]
        if (list_temps[i] < min_temp):
            min_temp = list_temps[i]
        if (list_temps[i] > max_temp):
            max_temp = list_temps[i]
        
    ave_temp /= count
    return ((min_temp, ave_temp, max_temp))

def temp_stats2_tuple(tuple1):
 
    list_temps = list(tuple1)
    ave_temp = sum(list_temps) / len(list_temps)
    min_temp = min(list_temps)
    max_temp = max(list_temps)
    return ((min_temp, ave_temp, max_temp))


print (first((1,2,3,4,5,6,7)))
print (middle((1,2,3,4,5,6,7)))
print (middle((1,2,3,4,5,6)))
print (middle((1,)))
print (last((1,2,3,4,5,6,7)))
print (single((1,)))
print (upper_tupple(('asdf', 'fgjhf', 'tyutuy')))

print (mod_tupple((1,2,3,4,5,6,7),(1,2)))
print (remove_duplicates((1,2,3,4,5,4,3,3,2,1,1,1,6,7)))
print (sort_tuple((1,2,3,4,5,4,3,3,2,1,1,1,6,7)))

print (tuple2string(('H', 'e', 'l', 'l', 'o'))) 
print (sentance2words('You can specify the separator, default separator is any whitespace.')) 
print (csv2tuple("apple,banana,orange")) 

print (basic_unpack((10,20,30)))
print (swap((10,20)))
print (extended_swap((1, 2, 3, 4, 5, 6)))
print (ignore_mid_values((1, 2, 3, 4, 5, 6)))

print (access_nested_data(("Alex", (16, "Grade 10"), ("Math", "Science"))))
print (flatten_tuple(((1, 2), (3, 4), (5,))))

print (tuple_counter((1, 6,2, 3, 2, 4, 3, 5, 4,4, 5,5,6,7)))

print (immutable_challenge((1, 2, 3, 4)))
print (tuple_sorting_by_score((("Alice", 85), ("Bob", 92), ("Charlie", 78))))

print (combined_lists_tuple(["A", "B", "C"], [90, 85, 88]))
print (temp_stats_tuple((22, 24, 19, 21, 25, 23, 20)))
print (temp_stats2_tuple((22, 24, 19, 21, 25, 23, 20)))