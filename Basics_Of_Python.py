print("Revision of basics of python programming language")
variable = int(input("Enter your input: "))
if (type(variable) == type(1)):
    print("The variable is of type 'int'")
else:
    print("The variable is NOT of type 'int'")

first_name = "Neeraj"
last_name = "Kumar"

print("The name of the author is {} and his surname is {}".format(
    first_name, last_name))
print("This is different way of string formatting by {first} whose surname is {last}".format(
    first=first_name, last=last_name))

my_str = "Neeraj Kumar"
print(my_str.isalnum())

lst = []
lst.append("This is appended")
print(lst)

lst.extend([1, 2, 3])
print(lst)
