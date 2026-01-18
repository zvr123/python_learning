
person = {"name":"Alice", "age":25,  "city":"Paris", "street":"Neveh Yarak", "number":99}
scores = {"Alice": 82, "Bob": 91, "Charlie": 78}
student = {"name": "Alice",
    "grades": {
        "math": 90,
        "english": 85,
        "science": 92
    }
}

# level 1 - Basic
def first_dict():
    name = "Alice"
    age = 25
    city = "Paris"
    dict1 = {"name":"Alice", "age":25,  "city":"Paris"}
    return dict1

def name_age():
    dict1 = {"name":"Alice", "age":25,  "city":"Paris"}
    return (dict1["name"], dict1["age"])

def add_to_person(key1, value1):
    person[key1] = value1
    return (person)

def change_age_to(value1):
    person["age"] = value1
    return (person)

def remove_key(value1):
    person.pop(value1)
    return (person)

def remove_last():
    person.popitem()
    return (person)

# Level 2 - Common Options
def check_key_exist(key1):
    if (key1 in person):
        return (f"{key1} was found")
    else:
        return (f"Couldn't find {key1}")

def loop_key(dict1):
    #person = dict1
    for k in person:
        print (f"{k}->{person[k]}")
    return "Done"

def dict_keys_length():
    return (f"The dict length: {len(person)}")

def get_value_of(key1):
    if (key1 in person):
        return (f"Found it - {person.get(key1)}")
    else:
        return (f"{key1}, wasn't found in the Dictionary")

# Level 3 - Thinking in Directories
def count_occurs(list1):
    dict1 = {}
    for i in list1:
        if (i in dict1):
            dict1[i]+=1
        else:
            dict1.update({i:1})
            # OR
            dict1[i] = 1
    return dict1

def dir_combine():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    c = a.copy()
    for i in b:
        c.update({i:b[i]})
    return c

def dir_combine2():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    merged = a.copy()
    merged.update(b)
    return merged

def dir_combine3():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    merge = a | b       #Combine 2 directories, like Union: {1, 2} | {2, 3} => {1, 2, 3}
    return merge

def dir_combine4():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    merge = {**a, **b}
    return merge

def max_values():
    return max(scores.values())

def max_keys():
    return max(scores.keys())

def above_80():
    above = {}
    for i in scores:
        if (scores[i]>80):
            above.update({i:scores[i]})
    return above

def above_80_2():
    high_scorers = {
    name: score
    for name, score in scores.items()
    if score >= 80
    }   
    return high_scorers

# Level 4- Hard (Nested dictionaries)
def nested_score():
    return student["grades"]["science"]

def nested_average():
    count = 0
    sum = 0
    for key,score in student["grades"].items():
        count += 1
        sum += score
    return (f"Average is: {sum/count}")

def update_nested(math_score):
    student["grades"].update({"math":math_score})
    return (f'math:{student["grades"]["math"]}')

# Level 5 — Advanced (Real-world patterns)


print (first_dict())
print (name_age())
print (add_to_person("email", "alice@example.com"))
print (change_age_to(26))
print (remove_key("city"))
print (remove_last())
print (check_key_exist("email"))
print (check_key_exist("age"))
print (loop_key({"name":"Alice", "age":25,  "city":"Paris"}))
print (dict_keys_length())
print (get_value_of("phone"))
print (get_value_of("age"))

print (count_occurs(["apple", "banana", "apple", "orange", "banana", "apple"]))
print (dir_combine())
print (dir_combine2())
print (dir_combine3())
print (dir_combine4())
print (max_values())
print (max_keys())
print (above_80())
print (above_80_2())


print (nested_score())
print (nested_average())
print (update_nested(100))