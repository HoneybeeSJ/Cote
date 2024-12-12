def solution(code):
    mode = 0  # 초기 모드 설정
    ret = ""  # 결과 문자열

    for idx in range(len(code)):
        if mode == 0:  # mode가 0일 때
            if code[idx] == "1":
                mode = 1  # 모드 전환
            elif idx % 2 == 0:  # 짝수 인덱스일 때만
                ret += code[idx]
        else:  # mode가 1일 때
            if code[idx] == "1":
                mode = 0  # 모드 전환
            elif idx % 2 == 1:  # 홀수 인덱스일 때만
                ret += code[idx]

    return ret if ret else "EMPTY"  # 결과 반환