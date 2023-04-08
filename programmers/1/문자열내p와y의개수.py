def solution(s):
    number_p= 0
    number_y= 0

    s= s.lower();
    
    for i in range(0, len(s)):
        if s[i] == 'p':
            number_p+= 1
        if s[i] == 'y':
            number_y+= 1

    if number_p != number_y:
        return False

    return True 

print(solution("pPoooyY"))
