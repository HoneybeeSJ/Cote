def solution(a, d, included):
    # 등차수열 생성
    sequence = [a + i * d for i in range(len(included))]
    
    # included에 따라 True인 항만 선택하여 합산
    result = sum(sequence[i] for i in range(len(included)) if included[i])
    
    return result