friends = ["Apple", "banana", 5, 3.14, False, "Anupam", "sujal", "Ankit"]

print(friends[0])
friends[0] = "Grapes" 
#strings are immutable but lists are mutable

print(friends[0])
print(friends[1:4])

value = friends.pop(3)
print(value)
print(value)
print(friends)


#tuples are immutable

a = (22,"anupam", False, 3.14, 5)
print(a)
print(type(a))


a = (7, 0, 8, 0, 0, 9)

n = a.count(0)
print(n)

#take input from user and convert it into list
userinput = input("Enter numbers separated by space: ")
userlist = userinput.split(" ")#converts string into list where each element is separated by space
print(userlist) 