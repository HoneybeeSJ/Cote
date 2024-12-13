def solution(numLog):
    # 결과 문자열을 저장할 리스트
    result = []
    
    # numLog의 값 변화를 순회하며 조작 문자열 생성
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff == 1:
            result.append("w")
        elif diff == -1:
            result.append("s")
        elif diff == 10:
            result.append("d")
        elif diff == -10:
            result.append("a")
    
    # 리스트를 문자열로 결합하여 반환
    return ''.join(result)