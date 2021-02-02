def sum(a, b, c):
    return a+b+c

def solution(expression):
    answer = []
    arr = [['+', '-', '*'],
           ['+', '*', '-'],
           ['-', '+', '*'],
           ['-', '*', '+'],
           ['*', '-', '+'],
           ['*', '+', '-']]
    
    tmp1 = list(expression)
    tmp2 = ''
    tmp3 = []
    tmp4 = 0
    
    for i in tmp1:
        tmp4 += 1
        try:
            int(i)
            tmp2 += i
        except:
            tmp3.append(tmp2)
            tmp3.append(i)
            tmp2 = ''
        finally:
            if tmp4 == len(tmp1):
                tmp3.append(tmp2)
    
    for i in arr:
        chk = tmp3.copy()
        for j in i:
            try:
                while True:
                    idx = chk.index(j)
                    ipt = str(eval(sum(chk[idx-1], chk[idx], chk[idx+1])))
                    del chk[idx-1:idx+2]
                    chk.insert(idx-1, ipt)
            except:
                pass

        answer.append(chk[0])

    answer = list(map(int, answer))
    answer = list(map(abs, answer))

    return max(answer)