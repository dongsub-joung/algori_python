def solution(n):
    answer = 0
    
    n= list(map(int, n))

    for i in range(len(n)):
        answer+= n[i]

    return answer
