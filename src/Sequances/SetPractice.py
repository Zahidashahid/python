"""
1.	Create a list/tuple/set of an integer type:

•	Calculate length, type.

•	Add elements to it.

•	Calculate sum, average of student marks? Store student subjects marks. The subjects shouldn’t exceed 5.

•	Calculate maximum marks

•	Traverse it.

•	Convert above sequences into each other. Observe if any changes being made?

•	apply single operators i.e. (+, -, *, /)

2.	Create a list/tuple/set dynamically.

"""

"""
   SEQUENCES LECTURE
   =================
              1. LIST         2. TUPLE            3.SET      4.DICTIONARY
--------------------------------------------------------------------------
Id            []               ()                 {}
order         Ordered          Ordered            Un-ordered
change        Changeable       Unchangeable       --
duplication   Duplicate        Duplicate          Un-duplicate
indexing      indexing         indexing           Un-indexed
-------------------------------------------------------------------------
keyword       list             tuple              set
len           len()            len()              len()
datatype      any, mixture     any, mixture       any, mixture
init          [],list(())      (), tuple(())      set(())
extras        --               single=>(value,)   {}=>means dict
--------------------------------------------------------------------------
"""
intSet = set((5, 10, 4, 25, 1, 6, 6))
intSetB = set((30, 10, 20, 51, 2, 5, 3))
print("\n-----------Simple functions on Set----------\n")
typeOfintSet = type(intSet)
lenOfintSet = len(intSet)


print("Set A", intSet)
print("Set B", intSetB)

intSet.remove(1)
print("Set A after removing 1 from it ",
      intSet)  # To avoid error if element want to remove that is not present in set use intSet.discard(1)


maxOfIntSet = max(intSet)

print("Type of variable iniSet is:", typeOfintSet)
print("Length of variable iniSet is:", lenOfintSet)

"""
----------------Adding New value to set-----------------
"""
intSet.add(50)
print("Set A values after adding new values:", intSet)
result = sum(intSet)
print("Sum of  values of set A", result)

"""
------------------ Average of a set-----------------
"""
avg = result / len(intSet)
print("Average of  values of set A ", avg)
print("Maximum of  values of set A", maxOfIntSet)

"""
--------Traversing a set---------------
"""
print("---------Traversing a set -------------- ")
for i in intSet:
    print(" ", i)

"""
--------------Reversing a Set ----------------
"""

"""
----------Typecasting of Set Data type
"""
print("----------Typecasting of Set Data type ")
print("Change into List",list(intSet))
print("Change into Tuple",tuple(intSet))
# print(dict(intSet)) # set can't typecast into dict

"""
---------------Addition of single set-----------------
"""


def sumOfSet():
    print("-------------- Sum  of A Set elements -------------")
    result = sum(intSet)
    print("Sum of all num in set A:", result)


"""
-----------------Subtraction of set--------------------
"""


def subOfSets():
    print("-------------- Difference  of 2 Sets -------------")
    print("Set A:", intSet)
    print("Set B:", intSetB)
    subOfSet = intSet.difference(intSetB)
    print("Difference:",subOfSet)

    """
    ------------------- Symmetric difference means all non common elements in sets----------
    ------------------- Symmetric difference update will update elements in set A with Symmetric difference set (all non common elements)----------
    """
    print("Symmetric difference:",intSet.symmetric_difference(intSetB))
    print("Symmetric difference update:",intSet.symmetric_difference_update(intSetB))
    print("Set A:", intSet)
    print("Set B:", intSetB)


"""
----------------Multiplication-------------------
"""


def multOfSet():
    print("-------------- Multiplication of 2 Sets -------------")


"""
---------------------Division--------------------
"""

"""
--------------------Union of set---------------------
"""


def uniOfSets():
    print("-------------- Union of 2 Sets -------------")
    uniOfSet = intSet.union(intSetB)
    print(uniOfSet)
    print("Set A:", intSet)
    print("Set B:", intSetB)


"""
---------------------Update in set---------------------
"""


def updateSets():
    print("-------------- Update of 2 Sets -------------")
    """
    ----- it is used to add multiple items to a set
    ------ here in example values of set B will add to set A
    """
    print(intSet.update(intSetB))
    print("Set A:", intSet)
    print("Set B:", intSetB)


"""
--------------Intersection of 2 sets------------------------
"""


def intersectionSets():
    print("-------------- Intersection of 2 Sets -------------")
    print(intSet.intersection(intSetB))
    print(intSet.intersection_update(intSetB))
    """
    --------------Intersection Update is used to update set A with new values that are common in both sets--------
    """
    print("Set A:", intSet)
    print("Set B:", intSetB)


sumOfSet()
subOfSets()
multOfSet()
uniOfSets()
updateSets()
intersectionSets()
