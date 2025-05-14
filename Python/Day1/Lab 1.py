# 1

var1 = (1)
var2 = [1,2,3,4,5]
var3 = (1,2,3,4,5)

print(type(var1))
print(type(var2))
print(type(var3))

#============================================================================================#
# 2

a,b,c = input("Enter Three Numbers Separated By Spaces: ").split()
print("a =", a)
print("b =", b)
print("c =", c)

#============================================================================================#
# 3

num = input("Enter a number : ")
num_str = str(num)
print("Length of the string: " , len(num_str))

#============================================================================================#
# 4

number = int(input("Please enter a number: "))
k = int(input("please enter a 'k' "))
result = number // 10 ** k
print(result)

#============================================================================================#
# 5 
numbers = input("Enter multiple numbers separated by space =: ")
numbers_list = numbers.split()
numbers_int = list(map(int ,numbers_list))

print("Maximum number: " , max(numbers_int))
print("Minimum number: " , min(numbers_int))

#============================================================================================#
# 6 

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

min_value = min(a, b)

print("The minimum value is: ", min_value)

#============================================================================================#
# 7 

salary = int(input("Enter your Salary: "))
if salary < 1000:
    print("You are poor")
elif 1000 <= salary < 20000:
    print ("Good Salary")
elif salary >= 20000:
    print ("You are rich")

#============================================================================================#
# 8     

age = int(input("Enter your age: "))
if age >= 18:
    print("You can drive a car.")
else:
    print("You cannot drive a car. You must be at least 18 yr old.")    



#============================================================================================#
#============================================================================================#   
#============================================================================================#