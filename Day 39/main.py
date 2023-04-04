class MyClass:
    pass

my_instance = MyClass()

if type(my_instance) == bool:
    print("It is a boolean")
elif type(my_instance) == int:
    print("It is an integer")
elif type(my_instance) == str:
    print("It is a string")
elif type(my_instance) == list:
    print("It is list")
elif type(my_instance) == type:
    print("data is a class object")
else:
    print("Data type cannot be identified")
x = "2867"

try:
    if x.isdigit():
        raise TypeError("The data provided must not be a number")
except Exception as error:
    print(f"Error:{error}")

def throw(num):
    for i in range(1,num+1):
        yield i
for i in throw(10):
    print(i)
