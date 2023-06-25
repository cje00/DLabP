# 1-2-8
'''
#문제8
앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어 또는 문장을
팰린드롬(palindrome)이라고 합니다.
예를 들어서 racecar, noon은 팰린드롬 단어입니다. 

소문자 알파벳, 공백(" "), 그리고 마침표(".")로 이루어진 문장이
팰린드롬 문장인지 점검하려 합니다.
문장 내에서 알파벳만 추출하였을 때에 팰린드롬 단어이면 팰린드롬 문장입니다.
예를 들어, "Never odd or even."과 같은 문장은 팰린드롬입니다.

소문자 알파벳, 공백(" "), 그리고 마침표(".")로 이루어진 문장 sentence가 주어질 때
팰린드롬인지 아닌지를 return 하도록 solution 함수를 작성했습니다.
그러나, 코드 일부분이 잘못되어있기 때문에,
몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.

---
##### 매개변수 설명
소문자 알파벳, 공백(" "), 그리고 마침표(".")로 이루어진 문장 sentence가 solution 함수의 매개변수로 주어집니다.

* sentence의 길이는 1이상 100이하입니다.
* sentence에는 적어도 하나의 알파벳이 포함되어 있습니다.
* setntence의 각 문자는 소문자 알파벳, 공백(" "), 또는 마침표(".")입니다.
'''
def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':  # and / or 에 주의 
            str += c
            
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[ size -1 - i]:
            return False
    return True


#The following is code to output testcase. The code below is correct and you shall correct solution function.
sentence1 = "never odd or even."
ret1 = solution(sentence1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
sentence2 = "palindrome"
ret2 = solution(sentence2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")

