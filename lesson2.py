#Declear Variables

temperature = 6

#conditionals
if temperature > 30:
    print("It is warm")
    print("Drink Water")


#String Formatting
first_name = "Favour"
last_name = "Ori"

#Format & Print out Fullname


#conditionals - If Statements

# age = int(input("What is your age : "))

# if age < 18 :
#     print("Sorry, but you can't get into the Club because you're underage :(")

# elif age == 18:
#     print("Hehe, you're so lucky. Come on in!")

# else:
#     print('Welcome! You can  come in!')


#Loops : ForLoop


# friends = ["David", "Mercy", "Grace", "John"]

# for friend in friends:
#     print(friend)


#While Loops 


#Ranges
burgers = ["Chicken", "Pork","Beef","Big Mac"]

# for n in range(len(burgers)):
#     print(n, burgers[n])




#Functions in Python
#Covered the basics of Data Types!


def greet(name):
    print(f"Welcome to Python, {name}")

def add(a,b):
    print(a+b)




#Functions with Default Params
# def greetDefault(name="Python 101"):
#     print(f"Good morning, {name}")




# # greet("Favour Ori")
# # add(10,6)
# greetDefault("Favour Theophilus Ori")


#Dictonaries


student = {
    "name": "David",
    "age": 22,
    "school": "Southern Arkansas University"
}

print(student["school"])