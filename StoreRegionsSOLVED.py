# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:17:47 2019

@author: Travis
"""

#Store Region Problem
"""
Hypothetical store location problem

26 regions
Each region has an identifying number
Each region is designated either Rural “R” or Urban “U”
Each region has a cost 
Each region has an “attractiveness” value (1-20)
Every region must either have a store on it, or have a store neighboring it

Constraints:
One store per region only
Each region must either have a store on it, or neighboring it
Each region cannot be covered by more than 3 stores
4 stores must be located in rural 
4 stores must be located in urban
There must be at least 2 stores in each row of regions
There must be at least 2 stores located in the “internal” regions
The average location attractiveness value must be at least 14.9
"""



"""
Region Data Attributes:
	Store = True/False
    Row = 0,1,2,3 = Int
	Interior = True/False
	Urban = True/False
	Cost = Float
	Attractiveness = Float
	Neighbors = List of Regions
	Coverage = Int
"""

# import itertools
import ast
import sympy

class Region(object):
    def __init__(self, row, interior, urban, cost, attractiveness):
        self.store = False
        self.row = row
        self.interior = interior
        self.urban = urban
        self.cost = cost
        self.attractiveness = attractiveness
        self.neighbors = []
        self.coverage = 0
    
    def addStore(self):
        self.store = True
    
    def serve(self):
        if self.store:
            self.coverage += 1
            for neighbor in self.neighbors:
                neighbor.coverage += 1
    
    def clear(self):
        self.store = False
        self.coverage = 0
        


"""
Region Rows are assigned 0-3 for convenience, instead of 1-4
"""

R1 = Region(0,False,True,52500,18)
R2 = Region(0,False,True,41750,13)
R3 = Region(0,False,False,33450,10)
R4 = Region(0,False,True,56000,9)
R5 = Region(0,False,False,48880,14)
R6 = Region(0,False,False,31455,15)

R7 = Region(1,False,False,34800,9)
R8 = Region(1,True,False,56800,8)
R9 = Region(1,True,True,90500,7)
R10 = Region(1,True,True,92500,9)
R11 = Region(1,True,False,75000,12)
R12 = Region(1,True,False,66000,13)
R13 = Region(1,False,True,42570,18)

R14 = Region(2,False,True,38000,11)
R15 = Region(2,True,False,49000,10)
R16 = Region(2,True,False,65675,12)
R17 = Region(2,True,True,125000,9)
R18 = Region(2,True,True,108900,15)
R19 = Region(2,False,False,64320,19)

R20 = Region(3,False,False,35000,11)
R21 = Region(3,False,False,45000,16)
R22 = Region(3,False,True,77800,10)
R23 = Region(3,False,True,67845,12)
R24 = Region(3,False,False,72450,11)
R25 = Region(3,False,False,48000,18)
R26 = Region(3,False,False,34345,17)

regions = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26]
 

R1.neighbors = [R2,R7,R8]
R2.neighbors = [R1,R3,R8,R9]
R3.neighbors = [R2,R4,R9,R10]
R4.neighbors = [R3,R5,R10,R11]
R5.neighbors = [R4,R6,R11,R12]
R6.neighbors = [R5,R12,R13]
R7.neighbors = [R1,R8,R14]
R8.neighbors = [R1,R2,R7,R9,R14,R15]
R9.neighbors = [R2,R3,R8,R10,R15,R16]
R10.neighbors = [R3,R4,R9,R11,R16,R17]
R11.neighbors = [R4,R5,R10,R12,R17,R18]
R12.neighbors = [R5,R6,R11,R13,R18,R19]
R13.neighbors = [R6,R12,R19]
R14.neighbors = [R7,R8,R15,R20,R21]
R15.neighbors = [R8,R9,R14,R16,R21,R22]
R16.neighbors = [R9,R10,R15,R17,R22,R23]
R17.neighbors = [R10,R11,R16,R18,R23,R24]
R18.neighbors = [R11,R12,R17,R19,R24,R25]
R19.neighbors = [R12,R13,R18,R25,R26]
R20.neighbors = [R14,R21]
R21.neighbors = [R14,R15,R20,R22]
R22.neighbors = [R15,R16,R21,R23]
R23.neighbors = [R16,R17,R22,R24]
R24.neighbors = [R17,R18,R23,R25]
R25.neighbors = [R18,R19,R24,R26]
R26.neighbors = [R19,R25]


def countStores(regions):
    #returns number of regions with a True value for self.store
    total = 0
    for region in regions:
        if region.store:
            total += 1
    return total

def countInterior(regions):
    #returns number of stores with a True value for self.interior
    total = 0
    for region in regions:
        if region.store:    
            if region.interior:
                total += 1
    return total

def countUrban(regions):
    #returns number of stores with a True value for self.urban
    total = 0
    for region in regions:
        if region.store:
            if region.urban:
                total += 1
    return total

def countRural(regions):
    #returns number of stores with a False value for self.urban
    total = 0
    for region in regions:
        if region.store:
            if not region.urban:
                total += 1
    return total

def getCost(regions):
    #returns total cost of all stores
    total = 0
    for region in regions:
        if region.store:
            total += region.cost
    return total

def getAvgAttractiveness(regions):
    #returns average attractiveness of all stores
    total = 0
    for region in regions:
        if region.store:
            total += region.attractiveness
    return (total/countStores(regions))

def checkCoverage(regions):
    #makes sure every region is served by more than 0, but less than 4 stores
    #returns True if the check Fails
    for region in regions:
        region.serve()
    for region in regions:
        if region.coverage > 3 or region.coverage == 0:
            return True
    return False

def checkRows(regions):
    #makes sure every row has no less than 2 stores in it
    #returns True if the check fails
    rows = [0,0,0,0]
    for region in regions:
        if region.store:
            rows[region.row] += 1
    for row in rows:
        if row < 2:
            return True
    return False
            
def clearAll(regions):
    for region in regions:
        region.clear()
        

def checkConstraints(regions):
    if countInterior(regions) < 2:
        return False
    if countUrban(regions) < 4:
        return False
    if countRural(regions) < 4:
        return False
    if getAvgAttractiveness(regions) < 14.9:
        return False
    if checkCoverage(regions):
        return False
    if checkRows(regions):
        return False
    
    return True

def getStoreCombs(numstores):
    #creates a list of length 26 with numstores 1s in it
    #returns a generator for all unique permutations of this list
    binarylist = []
    for i in range(numstores):
        binarylist.append(1)
    while len(binarylist) < 26:
        binarylist.append(0)
    return sympy.iterables.multiset_permutations(binarylist)


# Generate a txt file and fill it with every binary permutation of X stores
# temp = getStoreCombs(8) 
# file1 = open("storecombs.txt","w")
# for i in temp:
#     file1.write(str(i) + "\n")
# file1.close()

# Open the text file and read binary combs into a list (so they dont have to be generated every time)
# file1 = open("storecombs.txt","r")
# combs = []
# for line in file1:
#     combs.append(ast.literal_eval((line.strip())))
# file1.close()


def runTest(combs,regions):
    #runTest(getStoreCombs(numstores),regions)
    successfulcombs = []       
    for i in combs:
        for j in range(26):
            if i[j] == 1:
                regions[j].addStore()
        if checkConstraints(regions):
            # print("solution found")
            # print(i)
            successfulcombs.append(i)
            successfulcombs.append(getCost(regions))
        clearAll(regions)
    return successfulcombs


eight_store_solutions = runTest(getStoreCombs(12),regions)
print(eight_store_solutions)

# nine_store_solutions = runTest(getStoreCombs(9),regions)
# print(nine_store_solutions)

# ten_store_solutions = runTest(getStoreCombs(10),regions)
# print(ten_store_solutions)

# eleven_store_solutions = runTest(getStoreCombs(11),regions)
# print(eleven_store_solutions)

"""
The test above prints out:
    
[[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1], 487690, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], 501345, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1], 472945, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0], 486600, [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1], 505115, [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], 518770, [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0], 504025, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1], 480485, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], 454660, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1], 465740, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0], 479395]

This is the binary string for each 8 store possibility that passes all constraints, each possibility immediately followed by the total cost of all the stores. 
So, to format it - 

[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1], 487690
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], 501345
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1], 472945 ... etc

This code takes less than a minute to run

"""

"""
9 store solutions:

[[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], 496210, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 509865, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0], 519820, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 493190, [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 480020, [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], 513635, [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 527290, [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 497445, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], 489005, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 502660, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0], 512615, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], 472330, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 485985, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], 442840, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 472815, [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 527315, [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], 543095, [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 483770, [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 501195, [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 499195, [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 490815]

"""
"""
10 store solutions:
    
[[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0], 537660, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 540660, [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], 474295, [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0], 556220, [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], 537960, [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 551615, [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0], 518770, [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], 521770, [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], 491720, [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 569040]
"""
"""
There are no 11 store solutions.

This means that the lowest cost solution out of 8,9,10 store solutions is the answer, so 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], 442840
is the answer

"""