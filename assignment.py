# Question(1)- How do you concatenate two strings in python?
string1 ="Akanksha"
string2 ="verma"
string3 = string1+string2
print(string3) 
#Output- Akankshaverma

# Question(2)- What is the difference between the +operator and the join() method for concatenating strings?
#using +operator
a="Hello"
b="World"
print(a+b)
#Output-HelloWorld

#usingjoin() method
a="Hello"
b="World"
print("".join([a,b]))
#Output- HelloWorld

#Question(3)- How do you access individual characters in a string?
#Solution- You can access individual characters in a string by using indexing.
String="AKANKSHA"
print(String[3]) #find Character N
#output-N

#Question(4)- What method is used to find the length of a string in python?
#Solution- len()method is used  to find the length of the string.
#Example
string="Akanksha"
print(len(string))
#output- 8

#Question(5)- How can you convert a string to Uppercase in python?
#Solution- The upper()method is converts all lowercase characters in a string into uppercase characters and returns it.
string1="hello my friends."
string2=string1.upper()
print(string2)
#Output- HELLO MY FRIENDS.

#Question(6)- How can you convert a string to lowercase in python?
#Solution- The lower()method is converts all uppercase characters in a string into lowercase character and returns it.
string1="HELLO MY FRIENDS." 
string2=string1.lower()
print(string2)
#Output- hello my friends.

#Question(7)- What method is used to replace substring with in a string?
#Solution- We can use the replace() method is used to replace a substring with another substring in a string.
string1="I like Banana"
string2=string1.replace("Banana","Mango")
print(string2)
#Output- I like mango

#Question(8)- How can you split a string into a list of substring based on a delimiter?
#Solution- split() is a method that splits a string into a list of substring  based on whitespace by default or a specified delimiter.
string1="One,Two,Three,Four"
string2=string1.split(",")
print(string2)
#Output-['One','Two','Three','Four']

#Question(9)-How do you check if a string starts with a particuler substring?
#Solution- startswith() method returns true if a string starts with a specified string.otherwise it returns false.
string1="Welcome to the world"
string2=string1.startswith("Welcome")
print(string2)
#Output- True

#Question(10)-How do you check if a string ends with a particuler substring?
#Solution- endswith() method returns true if a string ends with a specified string .otherwise it returns false.
string1="Welcome to the World"
string2=string1.endswith("World")
print(string2)
#Output- True

#Question(11)-How can you remove leading and trailing whitespace from a string?
#Solution- Use the strip () method to remove leading and trailing whitespace from a string . 
string1="Apple"
string2=string1.strip()
print("of all fruits",string2,"is my favorite")
#output- of all fruits Apple is my favorite

#Question(12)- What method is used to find the index of the first occurence of a substring with in a string?
#Solution- "".index() method is the find the index of the first occurence of a substring with in a string.

#Question (13)- How can you count the number of occurences of a substring with in a string?
#Solution- count()method count the number of occurence of a substring with in a string.
string1="AKANKSHA"
string2=string1.count("A")
print(string2)
#Output- 3

#Question(14)-How do you check if a string contains only alphabetic characters?
#Solution- isalpha()method checks if all characters in a string are letters of the alphabet(a-z).if the string only contains letters of the alphabet,returns true .otherwise returns false.
string1="Akanksha"
string2=string1.isalpha()
print(string2)
#Output- True

#Question(15)- How do you check if a string contains only numeric characters?
#solution- isnumeric()method checks is all the characters in sa string are numeric(0-9).
string1="123567"
string2=string1.isnumeric()
print(string2)
#Output- True

#Question(17)-How can you reverse a string in python?
#Solution
variable="Hello World"[::-1]
print(variable)
#Output-dlroW olleH

#Question(18)-How do you format a string with placeholder for variable values?
#Solution- format()method formats the specified value and insert them inside the string's placeholder.
#first method
name="python"
city="Noida"
number=100
variable1="Name is %s and City is  %s and Number is %s"%(name,city,number)
print(variable1)
#Output-Name is python and City is Noida and Number is 100
#Second method
variable2=" Name is {} and City is {} and Number is {}".format(name,city,number)
print(variable2)
#Output- Name is python and City is Noida and Number is 100
#Third method
variable3=f"Name is {name} and City is {city} and Number is {number}"
print(variable3)
#Output- Name is python and City is Noida and Number is 100

#Question(19)- How do you access a substring of a string using slicing?
#Solution-Positive Indexing
data="Akanksha1234567890"
print(data[0:8:1])
print(data[8:18:1])
#Output-Akanksha
#1234567890
#Negative Indexing
data="Akanksha1234567890"
print(data[-10::1])
print(data[-18:-10:1])
#Output-1234567890
#Akanksha

#Question(20)- How can you remove specific character from a string in python?
#Solution- replace()method to remove a charcter form a string in python.
string1="Hello Sam"
string2=string1.replace("S","R")
print(string2)
#Output- Hello Ram






















