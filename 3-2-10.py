# 3-2-10

'''
#문제10
리스트 원소인 자신을 2로 나눈 값이 리스트에 있는 수의 개수를 구하려고 합니다.
예를 들어, 리스트가 [4, 8, 3, 6, 7]인 경우, 6/2 = 3, 8/2 =4이므로
자신을 2로 나눈 값이 리스트에 들어있는 수의 개수는 총 2개입니다. 
숫자가 담긴 리스트 arr가 주어졌을 때,
자신을 2로 나눈 값이 리스트에 들어있는 수가 몇 개인지 return 하는 solution 함수를
작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에,
코드가 올바르게 동작하지 않습니다.
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요. 

--- 

##### 매개변수 설명 
숫자가 담긴 리스트 arr가 solution 함수의 매개변수로 주어집니다. 

* arr의 크기는 1 이상 1,000 이하입니다. 
* arr의 원소는 1,000 이하의 자연수입니다. 

--- 

##### return 값 설명 
자신을 2로 나눈 값이 리스트에 들어있는 수가 몇 개인지 return 해주세요. 

##### 예시 

| arr |return | 
|:---|:---:|---|:---:|---|:---:|--|:--------:|--------:| 
| [4, 8, 3, 6, 7] |2| 

--- 

##### 예시 설명 

4/2=2이고, 2는 리스트에 없습니다. 
8/2=4이고 4는 4 이고 4는 리스트에 존재합니다. 
3/2=1.5이고 1.5는 리스트에 없습니다. 
6/2=3이고 3은 리스트에 존재합니다. 
7/2=3.5이고 3.5는 리스트에 없습니다. 
따라서 자신을 2로 나눈 값이 리스트에 들어있는 수가 총 2개이므로 2를 return 합니다.
'''
def solution(arr):
    answer = 0
    for i in arr:
        if i/2 in arr:   # (before) for i/2 in arr:
            answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
arr = [4, 8, 3, 6, 7]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
