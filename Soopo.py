def solution(answers):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    score_1 = 0
    score_2 = 0
    score_3 = 0

    for i in answers:
        if i == soopo_1[count_1]:
            score_1 += 1
            count_1 += 1 
        else:
            count_1 += 1

    for i in answers:
        if i == soopo_2[count_2]:
            score_2 += 1
            count_2 += 1 
        else:
            count_2 += 1            

    for i in answers:
        if i == soopo_3[count_3]:
            score_3 += 1
            count_3 += 1 
        else:
            count_3 += 1

    valid = max([score_1, score_2, score_3])
    answer = []

    if score_1 == valid:
        answer.append(1)

    if score_2 == valid:
        answer.append(2)

    if score_3 == valid:
        answer.append(3)

    return answer


a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

soopo_1 = []
soopo_2 = []
soopo_3 = []

for i in range(1, 2001):
    for k in range(0, 5):
        soopo_1.append(a[k])


for i in range(1, 1251):
    for k in range(0, 8):
        soopo_2.append(b[k])


for i in range(1, 1001):
    for k in range(0, 10):
        soopo_3.append(c[k])