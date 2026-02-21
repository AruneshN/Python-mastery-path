
"""
Topics: Tuples

Disc:
1) Tuples are immutable
2) Tuples are ordered
3) Tuples allow duplicate values
4) Tuple methods:
   - count()
   - index()
"""

#--------------------------------------------------- Access tuples
thistuple = ("apple", "banana", "cherry")

print(thistuple[2])

#----------------------------------------------- update tuples
add=list(thistuple)
add +=["kiwi"]
thistuple=tuple(add)
print(thistuple)

#------------------------------------------------- remove items

rmv=list(thistuple)
rmv.pop(3)
thistuple=tuple(rmv)
print(thistuple)


#-------------------------------------------------------------------------------- unpacking tuples
#packing tuples
user=("arunesh",22,"Python developer")

#unpacking tuples - taking value from tuples and assign variable 
name,age,role=user
print(age)

#-------------------------------------------------------------------------------- Asterrisk
"""
*arks
we dont know how many numbers we receive we use asterrisk
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(tropic)
print(tropic[0])

#----------------------------------------------------------------------------------- joint tuples

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

vegetables = ("carrot", "potato", "onion", "tomato", "cabbage")

market= fruits + vegetables


#------------------------------------------------------------------------- Tuple method
'''
1) count
2) index
'''

print(fruits.count("apple"))
print(market.index("onion"))
