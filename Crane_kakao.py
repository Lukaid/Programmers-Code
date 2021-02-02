def solution(board, moves):
        
    bucket = []
    answer = 0

    for i in moves:
        for j in board:
            if j[i-1] == 0:
                pass
            else:
                bucket.append(j[i-1])
                j[i-1] = 0

                if len(bucket) > 1:
                    if bucket[-2] == bucket[-1]:
                        bucket.pop()
                        bucket.pop()
                        answer += 2
                break

    return answer