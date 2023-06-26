# 3-2-5

'''
#문제5
여행객들의 총 교통비를 계산하려고 합니다.
교통편은 "Bus", "Ship", "Airplane" 총 3가지입니다.
나이가 20살 이상이면 어른 요금을, 그렇지 않으면 어린이 요금을 받습니다.
각 교통편별 가격은 다음과 같습니다.

|          | 어른     |   어린이 |
|----------|----------|----------|
| Bus      | 40,000원 | 15,000원 |
| Ship     | 30,000원 | 13,000원 |
| Airplane | 70,000원 | 45,000원 |

여행객들이 10명 이상인 경우 연령에 따라 할인을 받습니다.

| 어른 | 어린이 |
|------|--------|
| 10%  |    20% |

여행객들의 나이를 담고 있는 리스트 member_age와 교통편인 transportation이
매개변수로 주어질 때, 총 교통비를 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

---
#####매개변수 설명
여행객들의 나이를 담고 있는 리스트 member_age와 교통편인  transportation이
solution 함수의 매개변수로 주어집니다.

* member_age의 길이는 1 이상 1,000 이하입니다.
* member_age의 원소는 1 이상 100 이하입니다.
* transportation은 "Bus" 또는 "Ship" 또는 "Airplane" 입니다.

---
#####return값 설명
교통비 총액을 return 해주세요.

---
#####예시

| member_age | transportation | return |
|------------|----------------|--------|
| [13, 33, 45, 11, 20] | "Bus" | 150000 |
| [25, 11, 27, 56, 7, 19, 52, 31, 77, 8] | "Ship" | 203600 |

---
#####예시 설명
예시 #1
여행객들의 나이는 [13, 33, 45, 11, 20]이고 교통수단으로는 "Bus"를 이용하려합니다. 나이가 20살 미만인 인원은 2명으로 어린이 요금은 30,000원이고 나이가 20살 이상인 인원은 3명으로 어른 요금은 120,000원입니다. 따라서 교통비 총액은 150,000원입니다.

예시 #2
여행객들의 나이는 [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]이고 교통수단으로는 "Ship"을 이용하려합니다. 여행객들이 10명 이상이므로 교통비가 할인됩니다. 나이가 20살 미만인 인원은 4명으로 어린이 요금은 41,600원이고 나이가 20살 이상인 인원은 6명으로 어른 요금은 162,000원입니다. 따라서 교통비 총액은 203,600원입니다.

'''
def solution(member_age, transportation):
	if transportation == 'Bus':
		adult_expense = 40000
		child_expense = 15000
	elif transportation == 'Ship':
		adult_expense = 30000
		child_expense = 13000
	elif transportation == 'Airplane':
		adult_expense = 70000
		child_expense = 45000

	if len(member_age) >= 10:
		adult_expense = adult_expense /10 * 9   # adult_expense = @@@
		child_expense = child_expense /10 * 8  # child_expense = @@@

	total_expenses = 0
	for age in member_age:
		if age >= 20:   # if @@@:
			total_expenses += adult_expense
		else:
			total_expenses += child_expense

	return total_expenses


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")


