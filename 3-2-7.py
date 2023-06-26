# 3-2-7

'''
#문제7
주스 1잔을 만들려면 사과 3개와 당근 1개가 필요합니다.
그런데 키우는 토끼에게 먹이를 주기 위해 사과와 당근 종류에 상관없이
k개를 빼놓으려고 합니다. 주스는 최대한 많이 만들수록 좋습니다.

사과 개수 num_apple과 당근 개수 num_carrot,
토끼에게 줄 먹이 개수 k가 주어질 때
주스를 최대 몇 잔 만들 수 있는지 return 하도록 solution 함수를 작성했습니다.
그러나, 코드 일부분이 잘못되어있기 때문에,
몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---
#####매개변수 설명
사과 개수 num_apple과 당근 개수 num_carrot,
토끼에게 줄 먹이 개수 k가 solution 함수의 매개변수로 주어집니다.
* 사과 개수 num_apple과 당근 개수 num_carrot는 0 이상 200 이하인 정수입니다.
* 토끼에게 줄 먹이 개수 k는 0 이상 `num_apple+num_carrot` 이하인 정수입니다.

---
#####return 값 설명
주스를 최대 몇 잔 만들 수 있는지 return 해주세요.

---
#####예시

| num_apple | num_carrot | k | return |
|-----------|------------|---|--------|
| 5         |          1 | 2 | 1      |	
| 10        | 5          | 4 | 2      |

#####예시 설명
예시 #1
사과 2개를 먹이로 주면 사과 3개, 당근 1개가 남습니다.
남은 재료로 주스를 1잔 만들 수 있습니다.

예시 #2
사과 2개와 당근 2개를 먹이로 주면 사과 8개, 당근 3개가 남습니다.
남은 재료로 주스를 2잔 만들 수 있습니다.
'''
def solution(num_apple, num_carrot, k):
    answer = 0
    
    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    else:
        answer = num_carrot    

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0

    k = k-(num_apple + num_carrot)  # add
    
    while k> 0 :  #  before adj -> while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0:
            answer = answer -1 # before adj -> answer += 1
        i = i + 1
        k = k-1  # add
        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")


