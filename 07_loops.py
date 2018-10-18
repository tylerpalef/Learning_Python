# primes = [2, 3, 5, 7]
# for prime in primes:
#     print(prime)

# for x in range(5): # starts at 0, counts up until 5
#     print(x) # Prints out the numbers 0,1,2,3,4

# for x in range(3, 6):
#     print(x) # # Prints out 3,4,5

# for x in range(3, 8, 2):
#    print(x) # Prints out 3,5,7


# count = 0
# while count < 5:
#     print(count) # Prints out 0,1,2,3,4
#     count += 1  # This is the same as count = count + 1

count = 0
while True:
    print(count) # Prints out 0,1,2,3,4
    count += 1
    if count >= 5:
        break

for x in range(10):
    # Check if x is even
    if x % 2 == 0: # Prints out only odd numbers - 1,3,5,7,9
        continue
    print(x)
