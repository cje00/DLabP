# 1-2-10
#문제10
'''
평균은 자료의 합을 자료의 개수로 나눈 값을 의미합니다.
자연수가 들어있는 리스트의 평균을 구하고,
평균 이하인 숫자는 몇 개 있는지 구하려합니다.

예를 들어 주어진 리스트가 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이라면,
평균은 5.5이므로 리스트에서 평균 이하인 값은 5개입니다.
자연수가 들어있는 리스트 data가 매개변수로 주어질 때,
리스트에 평균 이하인 값은 몇 개인지 return 하도록 solution 함수를 작성했습니다.
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.
'''

def solution(data):
    total = sum(data)
    # average = len(data) / total <- x  총합 나누기 데이터 수가 평균 
    average = total / len(data)
    
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt


#The following is code to output testcase. The code below is correct and you shall correct solution function.
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")




