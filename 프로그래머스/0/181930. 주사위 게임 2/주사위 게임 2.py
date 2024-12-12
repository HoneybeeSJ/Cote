a = 5
b = 3
c = 3

def solution(a, b, c):
    answer = 0

    case_1 = (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    case_2 = a+b+c
    case_3 = (a+b+c) * (a**2+b**2+c**2)

    if a == b == c : 
        answer  = case_1
    elif a == b or b == c or a == c : 
        answer  = case_3
    else: 
        answer  = case_2
    return answer

print(solution(a, b, c))