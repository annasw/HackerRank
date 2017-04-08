class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        lowest = self.__elements[0]
        highest = self.__elements[0]
        for e in self.__elements:
            if e>highest: highest = e
            if e<lowest: lowest = e
        self.maximumDifference = highest-lowest
    
    # End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
