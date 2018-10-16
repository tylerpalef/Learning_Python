# True and false boolean
# x = 2
# print(x == 2) # prints out True
# print(x == 3) # prints out False
# print(x < 3) # prints out True

# Boolean Operators: and | or
# name = "John"
# age = 23
# if name == "John" and age == 23:
#     print("Your name is John, and you are also 23 years old.")
#
# if name == "John" or name == "Rick":
#     print("Your name is either John or Rick.")

# # Boolean Operator: n
# name = "John"
# if name in ["John", "Rick"]:
#     print("Your name is either John or Rick.")
#

# # Code Blocks
# x = 2
# if x == 2:
#     print("x equals two!")
# else:
#     print("x does not equal to two.")

# Is operator
# x = [1,2,3]
# y = [1,2,3]
# print(x == y) # Prints out True
# print(x is y) # Prints out False

# # The not operator, to invert Boolean
# print(not False) # Prints out True
# print((not False) == (False)) # Prints out False

# change this code
number = 10
second_number = 10
first_array = []
second_array = [1,2,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
