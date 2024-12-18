# 입력 처리
import sys


def compute_lps(pattern):
    """LPS 배열 생성"""
    m = len(pattern)
    lps = [0] * m
    j = 0  # 접두사 길이
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps


def kmp_search(text, pattern):
    """KMP 알고리즘을 사용한 패턴 검색"""
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    result = []
    j = 0  # 패턴 포인터
    for i in range(n):  # 텍스트 포인터
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:  # 패턴 전체 일치
                result.append(i - m + 2)  # 1-based index 저장
                j = lps[j]
            else:
                j += 1
    return result


if __name__ == "__main__":
    # 입력 처리
    input = sys.stdin.read
    data = input().splitlines()
    text = data[0]
    pattern = data[1]

    # KMP 검색 실행
    matches = kmp_search(text, pattern)

    # 결과 출력
    print(len(matches))
    print(" ".join(map(str, matches)))
