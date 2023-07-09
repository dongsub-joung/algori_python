#  콜라 문제 

def solution(a, b, n):
    answer = 0
    while (n>=a):
        new_coka= n // a * b
        left_over= n % a 

        answer+= new_coka
        n= left_over+ new_coka
    return answer

solution2 = lambda a, b, n: max(n - b, 0) // (a - b) * b

a=2
b=1
n=20
# 19
# print(solution(a,b,n))
print(solution2(a,b,n))  