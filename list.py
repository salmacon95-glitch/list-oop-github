students = ["Kaisamba", "Foday", "Sharon"]
print(students)

# accessing an item in a list

print(f"My best friend is {students[0]}")
print(f"My best friend is {students[1]}")
print(f"My best friend is {students[2]}")

# Get the index of an item in a list
print(students.index("Kaisamba"))
print(students.index("Sharon"))

# know the number of items in a list
# print(f"The total items in the list is: {len{students}}")
print(len(students))

# Add items to a list
students.append ("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]

print(students)
students.insert(4,"Donald")
print(students)

# Extending a list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

# Fruit remove
fruits.remove("Mango")
print(fruits)

# 
students.pop()
print(students)
students.pop()
thirdItem = students.pop
print(students)
print(thirdItem)