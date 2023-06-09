# 1-2-5
'''#문제5
주어진 리스트의 순서를 뒤집으려고 합니다.

예를 들어 주어진 리스트가 [1, 4, 2, 3]이면, 순서를 뒤집은 리스트는 [3, 2, 4, 1]입니다.

정수가 들어있는 리스트 arr가 매개변수로 주어졌을 때, arr를 뒤집어서 return 하도록 solution 함수를 작성하려 합니다.
빈칸을 채워 전체 코드를 완성해주세요.

---
##### 매개변수 설명
정수가 들어있는 리스트 arr가 solution 함수의 매개변수로 주어집니다.
* arr의 길이는 1 이상 100 이하입니다.
* arr의 원소는 -100 이상 100 이하의 정수입니다.

---
##### return 값 설명
리스트 arr의 순서를 뒤집어서 return 해주세요.

---
##### 예시

| arr          | return       |
|--------------|--------------|
| [1, 4, 2, 3] | [3, 2, 4, 1] |

##### 예시 설명
[1, 4, 2, 3]을 뒤에서부터 읽으면 3, 2, 4, 1입니다. 따라서 [1, 4, 2, 3]의 순서를 뒤집은 결과는 [3, 2, 4, 1]이 됩니다.

'''
def solution(arr):
    left, right = 0, len(arr)-1
    # while @@@: 
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")

