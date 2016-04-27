'''
Program 14 - Set Module Test File
Members: Kyle, Henok, Rojan
'''


from modSet import *



set1 = CustomSet([1,2,3,4,5])
set2 = CustomSet([3,4,5,6])
set3 = CustomSet([1,1,1,1,])

print("Custome Set: " , set3)
print("\n")


union = set1.unionSet(set2)

print("Union Set: ",union)
print("\n")

intersection = set2.interSectionSet(set1)

print("Intersection Set: ",intersection)
