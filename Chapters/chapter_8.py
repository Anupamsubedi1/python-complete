# Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c)/3
    print(average)


avg() # Function Call

# Default Argument
def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("anupam", "Thanks")
goodDay("sujal")  # ending will take default value



# program factorial of a number using recursion 


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

#multiplication table of a number using funciton
def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

# program ro remove a word from a list of words using function
def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["harian", "Rohan", "Shubham", "an"]

print(rem(l, "an"))

# Convert inches to cms using function
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")


#PATTERN PRINTING USING FUNCTION
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)


pattern(3)
#OUTPUT OF ABOVE PATTER IS
# ***
# **    
# *

# Sum of n natural numbers using recursion
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))

# Convert Fahrenheit to Celsius using function
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")