def solution(t, p):
    count= 0
    interval= len(t) - len(p)
    for i in range(0, interval+1):
        pivot= t[i:(i+len(p))]
        if pivot <= p:
            count+=1
    return count


T= "500220839878"
P= "7"
 	# 8
print(solution(T,P))