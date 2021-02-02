def fill_zero(x, n):
    if len(x) < int(n):
        for i in range(int(n) - len(x)):
            x = '0' + x
    return x

def solution(n, arr1, arr2):
    answer = []
    tmp = []
    tmp_2 =""
    arr1_bin = list(map(fill_zero, list(map(lambda x: x[2:], list(map(bin, arr1)))), [str(n)]*len(arr1)))
    arr2_bin = list(map(fill_zero, list(map(lambda x: x[2:], list(map(bin, arr2)))), [str(n)]*len(arr2)))

    for i in range(n):
        tmp.append((arr1_bin[i], arr2_bin[i]))

    for i in tmp:
        for j in range(n):
            if int(i[0][j]) + int(i[1][j]) == 0:
                tmp_2 += " "
            else:
                tmp_2 += "#"
        
        answer.append(tmp_2)
        tmp_2 = ""
    
    return answer