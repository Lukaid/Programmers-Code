def make_3(n):
    q = n // 3
    r = str(n % 3)
    
    if q == 0:
        return r
    else:
        return make_3(q) + r

def solution(n):
    tmp_2 = ""
    tmp = list(make_3(n))
    for i in range(len(tmp)):
        tmp_2 += tmp.pop()

    
    return int(tmp_2, 3)