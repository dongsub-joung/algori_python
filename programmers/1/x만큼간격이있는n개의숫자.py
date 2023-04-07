def solution(x, n):
    answer = []
    
    for number in range(x,x*n+1):
        if number % x == 0:
            answer.append(number)

    return answer


def solution2(x:int, n: int):
    answer= []

    for i in range(1, n+1):
        answer.append(x*i)

    return answer;


