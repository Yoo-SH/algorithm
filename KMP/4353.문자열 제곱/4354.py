def compute_lps(pattern):
    """
    LPS (Longest Prefix Suffix) 배열을 계산합니다.
    :param pattern: 문자열
    :return: LPS 배열
    """
    lps = [0] * len(pattern)  # LPS 배열 초기화
    length = 0  # 이전 접두사-접미사 매칭 길이
    for i in range(1, len(pattern)):
        # 매칭 실패 시, 이전 매칭 위치로 되돌아감
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]

        # 매칭 성공 시, 매칭 길이를 증가시킴
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length
    return lps


def max_repetition(s):
    """
    문자열의 최대 반복 횟수를 계산합니다.
    :param s: 입력 문자열
    :return: 최대 반복 횟수
    """
    if not s:
        return 0

    lps = compute_lps(s)  # LPS 배열 계산
    n = len(s)  # 문자열 길이
    min_unit = n - lps[-1]  # 최소 반복 단위 계산

    # 문자열 길이가 최소 반복 단위로 나누어떨어지면 반복 가능
    if n % min_unit == 0:
        return n // min_unit
    return 1  # 반복 불가능할 경우 1을 반환


def solve():
    """
    입력을 처리하고 결과를 출력합니다.
    """
    while True:
        s = input().strip()
        if s == ".":  # 종료 조건
            break
        print(max_repetition(s))  # 최대 반복 횟수 출력


# 실행
if __name__ == "__main__":
    solve()
