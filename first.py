#!/bin/python3

#STRINGS

#Print string
print("Hello, World!")
print('\n')
print("Did it work?")
print("This line is "+"awesome!")
print("""Neo...
The matrix has you
...""")

#MATH

print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with decimals
print(50 // 6) #no remainder


print('\n')
#VARIABLES AND METHODS

penis = "All is fair in love and war."
print(penis)

print(penis.upper()) #uppercase
print(penis.lower()) #lowercase
print(penis.title()) #title case
print(len(penis)) #counts characters

name = "Austin" #string
age = 33 #int
gpa = 3.8 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? No!

print("My name is " + name + " and I am " + str(age) + " years old.")


age +=1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
#FUNCTIONS

def who_am_i(): #This is a function without parameters
	name = "Austin"
	age = 33 + 1
	print("Hi, My name is " + name + " and I am almost " + str(age) + " years old.")
	
who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters
def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)


def nl():
	print('\n')
	
nl()

#Boolean expressions (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >=7
less_than_equal_to = 7 <= 7

test_and = True and True #True
test_and2 = True and False #False
test_or = True or True #True
test_or2 = True or False #True

test_not = not True #False


nl()

#Conditional Statements - if / else


def alcohol(age,money):
	if age >= 21 and money >= 2:
		return "We're getting a drink!"
	elif age >= 21 and money < 2:
		return "Come back with more cash!"
	elif age > 12 and age < 21 and money >= 25:
		return "Just this once, kid!"
	elif age < 21 and money >= 2:
		return "Nice try kid!"
	else:
		return "Get the hell out of here!"
		
print(alcohol(20,1))

nl()




#Lists - Have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #returns the second item in the list - index / indices
print(movies[0]) #returns the first item in the list
print(movies[1:3]) #returns the first number given until right before last number given
print(movies[1:4]) #returns all 
print(movies[1:]) #returns everything from number to end of list
print(movies[:1]) #everything before 1
print(movies[:2])
print(movies[-1]) #grabs last item

print(len(movies)) #counts items in list
movies.append("JAWS")
print(movies) #appends to end of list

movies.insert(2, "Hustle")
print(movies)

movies.pop() #removes last item
print(movies)

movies.pop(0) #removes first item 
print(movies)

amber_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(bobs_grade)
print(grades)
nl()
#Tuples - Do not change, ()
grades = ("a", "b", "c", "d", "f")

print(grades[1])

nl()

#For loops - start to finish of an iterate
vegetables = ["Carrots", "Cucumbers", "Tomatos", "Corn", "Spinich", "Peas", "Beans"]
for x in vegetables:
	print(x)

nl()
	
#While loops - execute as long as true
i = 1

while i < 10:
	print(i)
	i += 1


nl()

#Advanced Strings

my_name = "Austin"

print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence)

print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

#ADVANCED STRINGS

my_name = "Heath"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'" #- show example
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                       hello          "
print(too_much_space.strip())

print("A" in "Apple") #returns true
print("a" in "Apple") #returns false - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.")

nl()

#DICTIONARIES - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
employees['Legal'] = ["Mr. Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))




