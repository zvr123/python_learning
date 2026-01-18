🟢 Level 1 — Very Easy (Basics)
Exercise 1: Create a dictionary

Create a dictionary called person with:

name = "Alice"

age = 25

city = "Paris"

Print the dictionary.

Exercise 2: Access values

Given:

person = {"name": "Alice", "age": 25, "city": "Paris"}


Print:

the name

the age

Exercise 3: Add a new key

Add a key "email" with value "alice@example.com" to person.

Print the updated dictionary.

Exercise 4: Update a value

Change the age to 26.

Exercise 5: Delete a key

Remove the "city" key from the dictionary.

🟡 Level 2 — Easy (Common operations)
Exercise 6: Check if key exists

Given:

person = {"name": "Alice", "age": 26}


Check if "email" exists:

If yes, print it

If not, print "No email found"

Exercise 7: Loop through keys and values

Loop through the dictionary and print:

key -> value


Example:

name -> Alice
age -> 26

Exercise 8: Dictionary length

Print how many keys are in the dictionary.

Exercise 9: Default value

Use .get() to safely get "phone".
If it doesn’t exist, print "Unknown phone".

🟠 Level 3 — Medium (Thinking in dictionaries)
Exercise 10: Count occurrences

Given a list:

words = ["apple", "banana", "apple", "orange", "banana", "apple"]


Create a dictionary that counts how many times each word appears.

Expected idea:

{"apple": 3, "banana": 2, "orange": 1}

Exercise 11: Merge dictionaries

Given:

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}


Create a new dictionary that merges them.
If keys overlap, use the value from b.

Exercise 12: Find max value

Given:

scores = {"Alice": 82, "Bob": 91, "Charlie": 78}


Print the name of the person with the highest score.

Exercise 13: Filter dictionary

Create a new dictionary with only people who scored 80 or above.

🔵 Level 4 — Hard (Nested dictionaries)
Exercise 14: Nested access

Given:

student = {
    "name": "Alice",
    "grades": {
        "math": 90,
        "english": 85,
        "science": 92
    }
}


Print the science grade.

Exercise 15: Average from nested dictionary

Calculate and print the average grade.

Exercise 16: Update nested value

Change the math grade to 95.

🔴 Level 5 — Advanced (Real-world patterns)
Exercise 17: Group data

Given:

students = [
    {"name": "Alice", "city": "Paris"},
    {"name": "Bob", "city": "London"},
    {"name": "Charlie", "city": "Paris"}
]


Create a dictionary grouped by city:

{
  "Paris": ["Alice", "Charlie"],
  "London": ["Bob"]
}

Exercise 18: Dictionary comprehension

Using dictionary comprehension, create:

{"a": 1, "b": 4, "c": 9}


From:

letters = ["a", "b", "c"]

Exercise 19: Invert a dictionary

Given:

d = {"a": 1, "b": 2, "c": 3}


Create:

{1: "a", 2: "b", 3: "c"}

Exercise 20: Real-world scenario

You’re tracking API calls:

logs = ["GET", "POST", "GET", "DELETE", "GET", "POST"]


Create a dictionary that counts how many times each HTTP method was used.