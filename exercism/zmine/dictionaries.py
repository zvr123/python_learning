
person = {"name":"Alice", "age":25,  "city":"Paris", "street":"Neveh Yarak", "number":99}
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