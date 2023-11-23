#upper
a="hello sowje"
b=a.upper()
print(b)

#lower
a="HELLO sowje"
b=a.lower()
print(b)

#captalize
a = "hello world"
b = a.capitalize()
print(b)

#title
a="welcome to company"
b=a.title()
print(b)

#strip
a="  hello world  "
b=a.strip()
print(b)

#replace
s = "hello world"
result = s.replace("hello", "welcome to my")
print(result)

#find
s = "hello world"
index = s.find("world")
print(index)

#split
s = "hello,world"
result = s.split(",")
print(result)

#casefold
txt = "Hello, And Welcome To My HAPPY World!"
x = txt.casefold()
print(x)

#count
txt = "I love kiwi, kiwi are my favorite fruit"
x = txt.count("kiwi")
print(x)

#isalpha
txt = "CompanyX"
x = txt.isalpha()
print(x)


#join
myTuple = ("ravi", "yashu", "siva")
x = "#".ravi(myTuple)
print(x)

#isstrip
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

#swapcase
txt = "Hello My Name Is siva"
x = txt.swapcase()
print(x)