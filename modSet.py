'''
Program 14 - Set Module
Members: Kyle, Henok, Rojan
'''

class CustomSet:
    """
    Description: This function creates a class Called CustomSet
    Pre-Condition:None 
    Post-Condition:None
    """

    def __init__(self, tmpSetList = ["None"]):
        """
        Description: creates a CustomSet Object
        Pre-Condition: tmpSetList is type set
        Post-Condtion: updates the value of attributes
        """

        newList = []
        for ch in tmpSetList:
            if ch not in newList:
                newList.append(ch)
        
        self._setList = newList

        




    def getSetList(self):
        """
        Description: retrives self._setList
        Pre-Condition: None
        Post-Condtion: None
        """

        return self._setList



    def __add__(self, newSet):
        """
        Description: creates a union set by adding two different set
        Pre-Condition: newSet is type set
        Post-Condtion: returns new object union which is type list
        """

        union = []
        for ch in self._setList:
            union.append(ch)
        for ch in newSet.getSetList():
            if ch not in self._setList:
                union.append(ch)

        return CustomSet(union)

        
    
     

        

    def setIntersection(self, newSet):
        """
        Description: creates a intersection set by adding only common character
                     from two different set
        Pre-Condition: newSet is type list
        Post-Condtion: returns new object intersection which is type list
        """

        intersection = []

        for num in self._setList:
            if num in newSet.getSetList():
                intersection.append(num)
        return CustomSet(intersection)



    def __str__(self):
        """
        Description: returns all of the value of attributes
        Pre-Condition:
        Post-Condition:
        """

        tmp = ""
        tmp += str(self._setList)
        return tmp
        
