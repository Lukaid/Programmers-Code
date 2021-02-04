def solution(n, lost, reserve):

    have = [1 for i in range(n)]
    for i in reserve:
        have[i-1] += 1

    for i in lost:
        have[i-1] -= 1

    for i in range(len(have)-1):
        if have[i] == 0:
            if have[i + 1] == 2:
                have[i] = 1
                have[i + 1] = 1

    for i in range(1, len(have)):
        if have[i] == 0:
            if have[i - 1] == 2:
                have[i - 1] = 1
                have[i] = 1
    
    return len(have) - have.count(0)