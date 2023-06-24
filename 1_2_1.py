#You may use import as below.
#import math

def solution(shirt_size):
    #Write code here.
    size_counter = [0 for _ in range(6)]
    for ss in shirt_size:
        if ss =="XS":
            size_counter[0]+=1

        elif ss =="S":
            size_counter[1] += 1

        elif ss == "M":
            size_counter[2]+= 1

        elif ss == "XL":
            size_counter[4] += 1

        elif ss == "XXL":
            size_counter[5] +=1

    return size_counter

    answer = []
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
