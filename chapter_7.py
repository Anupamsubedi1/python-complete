for i in range(4):
    print(i)
    print("anupam")


## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "CHAD"
for i in s:
    print(i)

for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    


# This is a loop that does nothing
for i in range(645):
    pass


#multiplication table of user input
num = int(input("Enter a number: "))    
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

# Say hello to names starting with S

l = ["anupam", "Soham", "Sachin", "Raman", "Sita"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")   #end="" to avoid new line, so that next print comes in same line
    print("*"* (2*i-1), end="")
    print("")
