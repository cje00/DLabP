# 1-2-9
'''
#문제9
# 알파벳 문자열이 주어질 때, 연속하는 중복 문자를 삭제하려고 합니다.
# 예를 들어, "senteeeencccccceeee"라는 문자열이 주어진다면, "sentence"라는 결과물이 나옵니다.
# 영어 소문자 알파벳으로 이루어진 임의의 문자열 characters가 매개변수로 주어질 때,
# 연속하는 중복 문자들을 삭제한 결과를 return 하도록 solution 함수를 작성하였습니다.
# 그러나, 코드 일부분이 잘못되어있기 때문에, 코드가 올바르게 동작하지 않습니다.
# 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요
'''
def solution(characters):
    result = ""
    result += characters[0]
    for i in range(1, len(characters)):   # starting vaue is 1 not 0.
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
