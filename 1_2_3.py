# 1_2_3

'''
#문제3
시작 날짜와 끝 날짜가 주어질 때, 두 날짜가 며칠만큼 떨어져 있는지(D-day)를 구하려 합니다.
이를 위해 다음과 같이 3단계로 간단히 프로그램 구조를 작성했습니다.
(단, 윤년은 고려하지 않습니다.)

~~~
1단계. 시작 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
2단계. 끝 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
3단계. (2단계에서 구한 날짜) - (1단계에서 구한 날짜)를 구합니다.
~~~

시작 날짜의 월, 일을 나타내는 start_month, start_day, 끝 날짜의 월, 일을 나타내는 end_month, end_day가 매개변수로 주어질 때, 시작 날짜와 끝 날짜가 며칠만큼 떨어져 있는지 return 하도록 solution 함수를 작성했습니다. 이때, 위 구조를 참고하여 중복되는 부분은 func_a라는 함수로 작성했습니다. 코드가 올바르게 동작할 수 있도록 빈칸을 알맞게 채워주세요.

---
##### 매개변수 설명
시작 날짜의 월, 일을 나타내는 start_month, start_day, 끝 날짜의 월, 일을 나타내는 end_month, end_day가 solution 함수의 매개변수로 주어집니다.

* 잘못된 날짜가 주어지는 경우는 없습니다.
* 끝 날짜는 항상 시작 날짜보다 뒤에 있는 날이 주어집니다.
* 끝 날짜가 다음 해로 넘어가는 경우는 주어지지 않습니다.
  * 즉, start_month <= end_month를 항상 만족합니다.
  * start_month = end_month라면 start_day <= end_day를 항상 만족합니다.
* 각 달의 날짜 수는 1월부터 순서대로 [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 이며, 윤년은 고려하지 않습니다.
'''
def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
    # for i in @@@:
    for i in range(month -1):  # (0, 11)
        # total += @@@
        total += month_list[i]
    # total += @@@
    total += day
    return total - 1
        
def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

#The following is code to output testcase.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

# je
print('func_a(1,2)',func_a(1,2))

for i in range(0):
    print('i==0', i)

for i in range(1):
    print('i==1',i)
