"""
Topics:
set

Disc:
1) set is unorder which means on index
2)set is immutable
3) set not allow duplicates
"""

thisisset={"apple","orange","kiwi","berry","grapes"}


#Access set items

for x in thisisset:
    print(x)

print("kiwi" in thisisset)

#Add set items

thisisset.add("mango")

print(thisisset)


#Add sets
tropical = {"pineapple", "mango", "papaya"}
thisisset.update(tropical)

print(thisisset)


#add any Iterable
fruits=thisisset
mylist=["pineapple", "mango", "papaya","mango"]

fruits.update(mylist)
print(fruits)


#remove
"""
remove the value from set
1)discard - not raise the error if element not exist
2)remove - raise the error if elment not exist
"""

name={"arunesh","john","martin","shreya","salim"}
name.discard("arunesh")
print(name)
name.remove("john")

# try:    
#     name.remove("arunesh")
# except KeyError as a:
#     print(a,"no arunesh exist")


#loop sets

for x in name:
    print(x)

#--------------------------------------------------------------- joint sets

"""
joint sets used to joint the two or more sets

"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3=set1.union(set2)
print(set3)

#update set

set4={"x","y","z"}
set4.update(set3)

print(set4)


#frozenset
"""
unlike sets frozenset is immutable

1)data as a read only mode
2)our data is unchange
"""