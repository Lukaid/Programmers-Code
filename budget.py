def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        while True:
            d.remove(max(d))
            if sum(d) <= budget:
                break
    return len(d)