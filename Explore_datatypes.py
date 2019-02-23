string1='abc'
print(type(string1))
print("100"+"100")

print(dir(__builtins__))

print(help(len))

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-3:-1])

print("Python is fun"[-3:][-1])


mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(mylist[-1])

person97 = {"name":"Jack", "surname":"Smith", "age":"29"}
person97.pop("name")
print(person97)