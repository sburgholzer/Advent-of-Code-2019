# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:13:24 2019

@author: Scott
"""


#intcode=[1,1,1,4,99,5,6,0,99]
#intcode[1] = 12
#intcode[2] = 2

def run(noun, verb):
    intcode=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0]
    intcode[1] = noun
    intcode[2] = verb

    count = 0
    
    while count < (len(intcode)):
        indexOne = -999
        indexTwo = -999
        outputIndex = -999
        if intcode[count] == 1:
            indexOne = count + 1
            indexTwo = count + 2
            outputIndex = count + 3
            itemOneIndex = intcode[indexOne]
            itemTwoIndex = intcode[indexTwo]
            outputIndex = intcode[outputIndex]
            itemOne = intcode[itemOneIndex]
            itemTwo = intcode[itemTwoIndex]
            
            mySum = itemOne + itemTwo
            intcode[outputIndex] = mySum
        
        elif intcode[count] == 2:
            indexOne = count + 1
            indexTwo = count + 2
            outputIndex = count + 3
            itemOneIndex = intcode[indexOne]
            itemTwoIndex = intcode[indexTwo]
            outputIndex = intcode[outputIndex]
            itemOne = intcode[itemOneIndex]
            itemTwo = intcode[itemTwoIndex]
            
            myMult = itemOne * itemTwo
            intcode[outputIndex] = myMult
        elif intcode[count] == 99:
            break
            
        
        count += 4
    return intcode[0]


for i in range(100):
    for j in range(100):
        data = run(i, j)
        if data == 19690720:
            print(i, j)
            print(100 * i + j)

