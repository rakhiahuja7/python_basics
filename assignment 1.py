
##question 1 modulus of two numbers
print(15//2)
##question 2 difference b/w == and !=
##== means equal to and != means not equal to
print(2==3)
print(2!=3)
#question 3 declaration of a string variable and printing it
name='Rakhi'
print(name)
##question 4 length of a variable
print(len(name))
##question 5 'in'?
##'in' is a membership operator which is used to tell if one is the member of other
x=[1,2,3]
print(1 in x)
##question 6 declaration and printing of a list
fruits=['apple','banana','orange']
print(fruits)
##question 7 index in a list
b=fruits.index('banana')
print(b)
##question 8 adding a string variable in a list
fruits.append('grape')
print(fruits)
##question 9 declaration of a set
unique_numbers={1,2,3,4,5}
print(type(unique_numbers))
#question 10 difference b/w list and set
##i)list is represented in [] and set is represnted in {}
l=[1,2,3]
print(type(l))
s={1,2,3}
print(type(s))
##ii)list is ordered whereas set is unordered
l=[3,2,4]
print(l)
s={3,2,4}
print(s)
##iii)set doesnt have duplicacy whereas list have
l=[2,1,1]
print(l)
s={2,1,1}
print(s)
##question 11 declaration and printing of a string
sentence='Hello! myself Rakhi Ahuja'
print(sentence)
##question 12 asking if variable is a part of a list
print('apple' in fruits)
##question 13 conversion of a string type variable to integer type
i='5'
j=int(i)
print(j)
##question 14 use of not operator
##not is a logical operator which is used to negate truth value of boolean expression
x=2>3
print(x)
print(not x)
##question 15 declaring a number list
numbers=[1,2,3,4,5]
print(numbers)
##question 16 deleting an element of list 
numbers.pop(2)
print(numbers)
##question 17 declaration of a string set
letters={'a','b','c'}
print(letters)
##question 18 adding element in a set
letters.add('d')
print(letters)
##question 19 use of % operator
##% is an arithmetic operator which is used to give modulus
print(2%3)
##question 20 checking length of a list greater than a number
print(len(fruits)>3)