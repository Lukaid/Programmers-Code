def solution(N, stages):
    stack = {}
    tried = {}
    fail_rate = {}
    a = 0

    for i in range(1, N+2):
        stack[i] = 0
        tried[i] = 0
        fail_rate[i] = 0

    for i in stages:
        stack[i] += 1

    for i in range(1, N+2):
        tried[i] = len(stages) - a
        a += stack[i]

    for i in range(1, N+2):
        try:
            fail_rate[i] = stack[i] / tried[i]
        except:
            fail_rate[i] = 0

    del fail_rate[N+1]

    return sorted(fail_rate, key = fail_rate.get, reverse=True)