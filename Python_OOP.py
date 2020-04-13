## Python Object Oriented
## Content:
##   1- EXCEPTIONS
##   2- Python Classes
##   3- Getters and setters
##   4- Inheritance
##   5- Method overriding && overloading 
##   6- Class variable





## EXCEPTIONS
## when procedure execution hits an unexpected condition

## Types of exceptions:

##   SyntaxError : Python can’t parse program
##   NameError : local or global name not found
##   IndexError
##   AttributeError: attribute reference fails
##   TypeError : operand doesn’t have correct type
##   ValueError: operand type okay, but value is illegal
##   ZeroDivisionError


## Name error 

# print(pp)







## IndexError 

# l = [1, 2, 3]
# print(l[4])






## AttributeError

# a = 5
# a.append(3)







## TypeError 

# s = "This is string"
# a = s / 5
# def func(a,b):
#     return a + b

# func(5,"hossam")





## zero division error
    
# a = 5
# b = 0
# print(a/b)






# # Dealing with exception


# try:
#     # type your code here
#     a = 5
#     b = 0
#     print(a/b)
# except:
#     print("There is abug in code")
    





# # # Separate except clauses
# try:
#     # type your code here
#     a = 5
#     b = 1
#     print(a/0)
    
# except ZeroDivisionError:
#     print("There is a zero division error here")
    
# except ValueError:
#     print("There is a Value error here")
    
# except TypeError:
#     print("There is a type error here")
    
# except:
#     print("There is a bug here")
    
# # else:
# #     print("This code excute if there is no error") 
    
# finally:
#     print("This code excute if there is an error")







# OOP [EVERYTHING IN PYTHON IS AN OBJECT]

# # Creating a class

# class Coordinate():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    

# c = Coordinate(3, 5)
# origin = Coordinate(0, 0)

# print(c.x)
# print(origin.y)





# class Coordinate():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def distance(self, other):
#         x_diff = (self.x - other.x) ** 2
#         y_diff = (self.y - other.y) ** 2
#         return (x_diff + y_diff) ** .5
    

# c = Coordinate(3, 5)
# zero = Coordinate(0, 0)

# print(c.distance(zero))
# print(c.distance(c))

# print(Coordinate.distance(c, zero))





# Getter and setter methods

# class Animal():
#     def __init__(self, age):
#         self.age = age
#         self.name = None
    
#     # Getters method
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
    
#     # Setters Method
#     def set_age(self,age):
#         self.age = age
#     def set_name(self,name):
#         self.name = name
        
#     # Speacial method : print(some description of the function)
#     def __str__(self):
#         return "ِAnimal: " + str(self.name) + " : " + str(self.age)
    



# cat = Animal(5)

# print(cat.age)      # allowed but not recommended
# print(cat.get_age())  # recommended


# print(cat.name)

# cat.set_age(10)
# cat.set_name("Tom")

# print(cat.get_age())
# print(cat.get_name())

# print(cat)








# ## Inheritance

# class Animal():
#     def __init__(self, age):
#         self.age = age
#         self.name = None
    
#     # Getters method
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
    
#     # Setters Method
#     def set_age(self,age):
#         self.age = age
#     def set_name(self,name):
#         self.name = name
        
#     # Speacial method : print(some description of the function)
#     def __str__(self):
#         return "ِAnimal: " + str(self.name) + " : " + str(self.age)
    
    

# class Cat(Animal):
#     def speak(self):
#         print("Mewo")
    
#     def say_your_type(self):
#         print("I'm a cat")
    

# tom = Cat(2)

# print(tom.age)
# print(tom.get_age())

# tom.set_name("Tom")

# print(tom.get_name())

# tom.say_your_type()
# tom.speak()

# print(tom)    







## Mathod overloading and overriding


## Overloading

## Wrong way

# def add(a, b):
#     return a + b

# def add(a, b, c):
#     return a + b + c


## right way

# def add(a, b, c = 0):
#     return a + b + c


# print(add(5, 6, 7))





## Overriding


# class Animal():
#     def __init__(self, age):
#         self.age = age
#         self.name = None
    
#     # Getters method
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
    
#     # Setters Method
#     def set_age(self,age):
#         self.age = age
#     def set_name(self,name):
#         self.name = name
        
#     # Speacial method : print(some description of the function)
#     def __str__(self):
#         return "ِAnimal: " + str(self.name) + " : " + str(self.age)
    
    

# class Cat(Animal):
    
#    # def __init__(self, name, age):
#    #     Animal.__init__(self, age)
#    #     self.name = name
        
#     def speak(self):
#         print("Mewo")
    
#     def say_your_type(self):
#         print("I'm a cat")
        
#     def __str__(self):
#         return "CAT: " + str(self.name) + " : " + str(self.age)


# tom = Cat(15)
# print(tom)
        
    
## tom = Cat("Tom", 2)
## print(tom)



# class Person():
#     num_setting_name = 0
    
#     def __init__(self, name):
#         self.name = name
        
#     def set_name(self, name):
#         self.name = name
#         Person.num_setting_name += 1
        
#     def get_num_of_setting(self):
#         return Person.num_setting_name
        
    
# hossam = Person("Hossam")
# print(hossam.get_num_of_setting())

# hossam.set_name("Asaad")
# print(hossam.get_num_of_setting())

# hossam.set_name("Asaad")
# print(hossam.get_num_of_setting())
