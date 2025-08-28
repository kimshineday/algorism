def solution(angle):
    """
    이 함수는 주어진 각도가 예각, 직각, 둔각, 평각을 분류해서 각각 1, 2, 3, 4로 리턴을 합니다.
    """
    if angle <= 90:
        if not angle == 90: # 직각이 아닐 경우 예각
            return 1 # 예각임을 출력
        return 2 # 직각일 경우.
    else :
        if not angle == 180: # 평각이 아닐 경우
            return 3 # 둔각임을 출력
        return 4 # 평각일 경우.