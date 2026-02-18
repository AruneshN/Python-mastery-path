'''
Topic :List

Disc:
1)List is ordered - element stored in sequence [0]
2) List is mutaple
3)List allow duplicate
4)list is ordered - if we add values order not changed
'''


#1)creating List
lst=[]

#2)list allow multiple data type together
Lst=["arunesh",22,3.9,True]

#3)Access List
lst=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(lst[0]) #access lst through index

"""
negative indexing start -1
1) we use access last value
real time example:
1.last transaction
2.latest message
"""
print(f' access through negative index :{lst[-1]}')

#4) Range of indexing
"""
we can access indexing through range,
real time example:
1)last 5 transaction
"""
lst=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(f'Access through range: {lst[2:6]}')
print(f'Access through range: {lst[-5::]}')

#5) Check if Item Exists

if "melon" in lst:
    print("melon in list")

#-----------------------------------------------------------Change list items

fruits=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


#-------------------------------------------------------- Add List items
fruits=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#add grapes in kiwi place
fruits[4]="grapes"

#insert 
"""
1)insert used without replacing any item it add items.
2)used for add specific value in specific index
"""
fruits.insert(3,"kiwi")

#append
"""
1)append add values in last
"""

fruits.append("berry")
print(fruits)

#-------------------------------------------------------- remove list
fruits=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#remove
"""
remove method used to specific items
"""
fruits.remove("apple")
print(fruits)

#pop
"""
pop used to remove through index
1)remove single element
"""
fruits.pop(5)
fruits.pop() #remove last element

#del
'''
del used to remove multiple element 
'''
fruit=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

del fruit[1:6]
print(fruits)

#list slice

fruit[1:3]=[]
print(fruit)

#-------------------------------------------------List comprehension 
"""
list comprehension is create new list based on existence
"""

numbers=[x for x in range(1,50)]

even=[x for x in numbers if x%2 ==0 ]

# if else list Comprehension

result=["even" if x%2==0 else "odd" for x in numbers]

#-------------------------------------------------- Sort List
numbers=[x for x in range(1,50)]
numbers.sort()
# print(numbers)

numbers.sort(reverse=True)
# print("sorted to reverse")
# print(numbers)

#reverse
numbers.reverse()
print(numbers)


#------------------------------------------------- join list
lst1=[x for x in range(1,10)]
lst2=[x for x in range(21,40)]

lsts=lst1+lst2
print(lsts)

#extends
lst1.extend(lst2)
print(lst1)