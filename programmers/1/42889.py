def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer

N= 5 	
STAGES= [2, 1, 2, 6, 2, 4, 3, 3] 	
# [3,4,2,1,5]
solution(N,STAGES)