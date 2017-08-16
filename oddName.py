""" Cain McDonald"""
name = input("Please enter your name:")
if len(name) <= 0:
    print("Invalid Name")
    name = input("Please enter your name:")
for char in name[::2]:
    print("{}".format(char))
