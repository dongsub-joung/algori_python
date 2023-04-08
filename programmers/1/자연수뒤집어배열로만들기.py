# not work
def solution(n):
    arr= []
    
    while n >= 10:
        arr.append(n % 10)
        n%= 10
    
    return arr

def solution2(n: int):
    return list(map(int, reversed(str(n))))

def solution3(n: int):
    return [int(i) for i in str(n)][::-1]

print(solution(12345))
print(solution2(12345))
print(solution3(12345))


