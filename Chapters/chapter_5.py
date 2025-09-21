#disctionary in python is a collection of key value pairs
mydict = {
    "fast": "In a quick manner", 
    "anupam": "A coder",
    "marks": [1, 2, 5],
    "anotherdict": {'samir': 'player'},
    1: 2
}

#to access the value of fast
print(mydict['fast'])
#to access the value of anupam
print(mydict['anupam'])
#to access the value of samir
print(mydict['anotherdict']['samir'])


print(mydict.keys()) #prints all the keys of the disctionary
print(mydict.values()) #prints all the values of the disctionary

#IMPORTANT NOTEE ,DONOT USE S={} TO CREATE DISTIONARY AS IT WILL CREATE AN EMPTY DICTIONARY
#INSTEAD USE S=set() TO CREATE AN EMPTY SET

SET= set()
print(type(SET))
SET = {1, 2, 3, 4, 5, 5, 5}
#sets do not allow duplicate values

#WHEN THE SET VALUE IS PRINTED THE VALUE COMES WITHOUT THE DUPLICATION

print(SET)
#OUTPUT WILL BE {1, 2, 3, 4, 5}

#SETS ARE IMMUTABLE , MEANING WE CANNOT CHANGE THE VALUES OF A SET
#BUT WE CAN ADD OR REMOVE VALUES FROM A SET
SET.add(6)

#SET METHODS , UNION AND INTERSECTION
s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))