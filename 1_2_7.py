# 1-2-7

def solution(scores):
    count = 0
    for s in range(len(scores)):
        # if 650 <= scores[s] and scores[s] < 800:
        if 650 <= scores[s] <800:
            count += 1
    return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
