# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Adding elements to the list
fruits.append('orange')
fruits.insert(1, 'grape')

# Accessing elements by index
first_fruit = fruits[0]
last_fruit = fruits[-1]

# Iterating through the list
print("List of fruits:")
for fruit in fruits:
    print(fruit)

# Finding the length of the list
num_fruits = len(fruits)

# Removing an element by value
fruits.remove('banana')

# Sorting the list
fruits.sort()

# Reversing the list
fruits.reverse()

# Displaying the modified list
print("\nModified list of fruits:")
for fruit in fruits:
    print(fruit)

# Checking if an element exists in the list
if 'kiwi' in fruits:
    print("\nKiwi is in the list.")
else:
    print("\nKiwi is not in the list.")
    
    
    
    
    
    
    #join
    
    list = ["Kapeel",  "Kanwar",  "Naresh",
        "Sartaj"]
# for item in list:
#     print(item, "is my classmate ")
a = "and".join(list)
print(a , "are classmates")

