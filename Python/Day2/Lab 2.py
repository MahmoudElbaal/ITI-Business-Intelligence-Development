#1 

total = 10

def add_to_total(n):
    global total
    total += n 
    local_total = 10
    print(local_total)
    print(total)
add_to_total(5)

#============================================================================================#
#2
balance = 5000

def withdraw(amount):
    global balance  
    if amount > balance:
        return
    withdrawn_amount = amount
    balance -= withdrawn_amount
    print(withdrawn_amount)
    print(balance)
withdraw(1000)    

#============================================================================================#
# 3

count = 10

def modify_global_var():
    count = 20
    
print("Inside function: count =", count)
print("Outside function (before): count =", count)
modify_global_var()
print("Outside function (after): count =", count)

#============================================================================================#
# 4

def print_items_with_index(items):
    for nd , i in enumerate(items):
        print(nd, i)

lst = ["A", "B", "C", "D"]
print_items_with_index(lst)

#============================================================================================#
# 5

def print_items_with_index(items):
    for nd, i in enumerate(items, start=1):
        print(nd, i)
lst = ["A", "B", "C", "D"]
print_items_with_index(lst)

#============================================================================================#
# 6

square = lambda x: x ** 2
lst = [2,4,6,8,10]
sq_lst = list(map(square, lst))
print("Result:", sq_lst)

#============================================================================================#
# 7

fun = lambda x: x % 2 == 0
lst2 = [11,12,13,14,15,16,17,18,19,20]
new_numbers = list(filter(fun, lst2))
print(new_numbers)

#============================================================================================#
# 8

reverse_string = lambda s: s[::-1]

input = "This Is A Test"
new_result = reverse_string(input)

print(input)
print(new_result)

#============================================================================================#
# 9

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name)
        print(self.age)
student1 = Student("Mahmoud Saied", 26)
print("Student Details:"),student1.details()

#============================================================================================#
# 10

class Stundent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return self.name, self.age

    def details(self):
        print(self.get_details())

student1 = Student("Mahmoud Saied", 26)

print("Student Details:"),student1.details()



#============================================================================================#
#============================================================================================#
#============================================================================================#


