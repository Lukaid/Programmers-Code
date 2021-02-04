def solution(numbers):
    answer, tmp = [] ,[]

    for i in range(len(numbers)):
        for k in range(i+1, len(numbers)):
            tmp.append(numbers[i] + numbers[k])
    
    answer = sorted(list(set(tmp)))

    return answer