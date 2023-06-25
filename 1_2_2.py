# 1_2_2
'''
#문제2
A 쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다.
회원 등급에 따른 할인율은 다음과 같습니다.
(S = 실버, G = 골드, V = VIP)

| 등급     | 할인율 |
|----------|--------|
| "S"      | 5%     |
| "G"      | 10%    |
| "V"      | 15%    |

상품의 가격 price와 구매자의 회원 등급을 나타내는 문자열 grade가 매개변수로 주어질 때,
할인 서비스를 적용한 가격을 return 하도록 solution 함수를 완성해주세요.

#####매개변수 설명
상품의 가격 price와 회원 등급 grade가 매개변수로 주어집니다.
* price는 100 이상 100,000 이하의 100단위 자연수입니다.
* grade는 "S", "G", "V" 세 가지 중 하나입니다.

---

#####return 값 설명
할인한 가격을 return 하도록 solution 함수를 작성해주세요.

'''
#You may use import as below.
#import math

def solution(price, grade):
    answer = 0
    #Write code here.
    
    if grade == "S":
        answer = int(price*0.95)

    if grade == "G":
        answer = int(price*0.9)

    if grade == "V":
        answer = int(price*0.85)
        
    return answer

#The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
