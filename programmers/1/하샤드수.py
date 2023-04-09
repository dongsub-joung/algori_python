def solution(x):
    suming= 0
    
    for n in str(x):
        suming+= int(n)

    if x % suming != 0:
        return False

    return True

print(solution(12))
print(solution(13))
