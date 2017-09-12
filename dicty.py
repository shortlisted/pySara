import random

# creates an empty dictionary with no keys and no values
abc = {}
print("We have an empty dictionary!")
print(abc)
input("Enter to continue.")

# a loop for creating keys in the dictionary that contain empty lists
ALFABET = "abcdefghijklmnopqrstuvxyzåäö"
for letter in ALFABET:
    abc[letter] = []
print("We have keys in dictionary!")
print(abc)
input("Enter to continue.")

# assign the keys random values with abc.items and list.append
for k, v in abc.items():
    abc[k].append(random.randint(0,256))

print("We have random numbers as values!")
print(abc)
input("Enter to exit.")
