def solution(numbers, hand):

    arr = {1 : [1, 4], 2 : [2, 4], 3 : [3, 4],
           4 : [1, 3], 5 : [2, 3], 6 : [3, 3],
           7 : [1, 2], 8 : [2, 2], 9 : [3, 2],
           '*' : [1, 1], 0 : [2, 1], '#' : [3, 1]
           }

    answer = ''
    left = "*"
    right = "#"
    for i in numbers:
        if i in (1, 4, 7):
            answer += 'L'
            left = i

        elif i in (3, 6, 9):
            answer += 'R'
            right = i

        else:
            left_i = (abs(arr[left][0] - arr[i][0]) + abs(arr[left][1] - arr[i][1]))
            right_i = (abs(arr[right][0] - arr[i][0]) + abs(arr[right][1] - arr[i][1]))
            if left_i > right_i:
                answer += 'R'
                right = i
            elif left_i < right_i:
                answer += 'L'
                left = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                elif hand == 'left':
                    answer += 'L'
                    left = i
    
    return answer