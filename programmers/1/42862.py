def solution(n, lost, reserve):
    answer = 0
    _reserve= [r for r in reserve if r not in lost]
    _lost= [l for l in lost if l not in reserve]

    for r in _reserve:
        f= r- 1
        b= r+ 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n-len(_lost)

def solution2(n, lost, reserve):
    _reserve= set(reserve) - set(lost)
    _lost= set(lost) - set(reserve)
    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)
    return n - len(_lost)