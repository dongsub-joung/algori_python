import math

def solution(n):
    sqrts= math.sqrt(n)
    if sqrts % 1 ==0:
        return pow(sqrts+1, 2)
    else:
        return -1
