import math
import os
import random
import re
import sys



def breakingRecords(scores):
    contMin = 0
    contMax = 0
    minScores = scores[0]
    maxScores = scores[0]
    for i in range(len(scores)):
        if(maxScores > scores[i]):
            contMax += 1
            maxScores = scores[i]
        elif(minScores < scores[i]):
            contMin += 1
            minScores = scores[i]

    return maxScores, minScores



#Programa Principal
num1 , num2 = breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])
print(num1  num2)
