# Its not work
def solution(numbers):
    answer = 0
    lens= len(numbers)

    for i in range(0, lens):
        for j in range(i+1, lens):
            for k in range(j+1, lens):
                if (numbers.get(i)+ numbers.get(j)+ numbers.get(k)) == 0:
                    answer+=1
    return answer

# https://somjang.tistory.com/entry/Programmers-%EC%82%BC%EC%B4%9D%EC%82%AC-Python
from itertools import combinations
def solution2(numbers):
    num_combinations= [sum(comb) for comb in list(combinations(numbers, 3)) if sum(comb) == 0]
    return len(num_combinations)


def solution3(number):
    answer = 0
    for i in combinations(number,3):
        if sum(i) == 0:
            answer +=1
    return answer


numbers1= {-2, 3, 0, 2, -5} 
# 2
print(solution2(numbers1))

numbers2= {-3, -2, -1, 0, 1, 2, 3}
# 5
print(solution3(numbers2))

numbers3= {-1, 1, -1, 1}
# 0
print(solution3(numbers3))