def solution(arr, divisor):
    answer = []

    for element in arr:
        if (element%divisor==0):
            answer.append(element)
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer 
