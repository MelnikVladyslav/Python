# ������ 1
age_str = input("How you year? ")
age = int(age_str)
if age >= 18:
    print("You adult.")
else:
    print("You not adult.")

# ������ 2
fruits = ["apple", "potato", "banana"]
for i in fruits:
    print(i)

# ������ 3
def greet(name):
    print("Hello, " + name + "!")

greet("Vlad")
