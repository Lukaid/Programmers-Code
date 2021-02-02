def solution(dartResult):
    chk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    answer = 0
    num = []


    for i in range(len(dartResult)):

        if dartResult[i] in chk:
            if dartResult[i] == '1':
                if dartResult[i+1] == '0':
                    num.append(10)
                else:
                    num.append(int(dartResult[i]))
            elif dartResult[i] == '0':
                if dartResult[i-1] == '1':
                    pass
                else:
                    num.append(int(dartResult[i]))
            else:        
                num.append(int(dartResult[i]))
        elif dartResult[i] == "S":
            pass
        elif dartResult[i] == "D":
            a = num.pop()
            num.append(a * a)
        elif dartResult[i] == "T":
            a = num.pop()
            num.append(a * a * a)
        elif dartResult[i] == "*":
            try:
                a = num.pop()
                b = num.pop()
                num.append(b * 2)
                num.append(a * 2)
            except:
                num.append(a * 2)
        elif dartResult[i] == "#":
            a = num.pop()
            num.append(-1 * a)

    for i in num:
        answer += i
    
    return answer