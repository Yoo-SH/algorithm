def build_lps(pattern):
    """패턴에 대한 LPS(Longest Prefix Suffix) 배열 생성."""
    lps = [0] * len(pattern)
    length = 0  # 이전 접두사와 접미사가 일치하는 최대 길이

    for i in range(1, len(pattern)):
        # 현재 문자와 접두사 길이 위치의 문자가 다를 경우
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]  # 이전 접두사의 길이로 이동

        # 현재 문자와 접두사 길이 위치의 문자가 같을 경우
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length  # 현재 위치의 LPS 값을 설정

    return lps


def kmp_search(text, pattern):
    """텍스트에서 패턴을 검색하는 KMP 알고리즘."""
    lps = build_lps(pattern)  # 패턴에 대한 LPS 배열 생성
    matches = []  # 패턴이 발견된 위치 저장
    j = 0  # 패턴 인덱스 초기화

    for i, char in enumerate(text):
        # 텍스트와 패턴의 현재 문자가 일치하지 않을 경우
        while j > 0 and char != pattern[j]:
            j = lps[j - 1]  # 패턴 내에서 LPS 배열 값에 따라 이동

        # 텍스트와 패턴의 현재 문자가 일치하는 경우
        if char == pattern[j]:
            j += 1  # 패턴 인덱스 증가
            if j == len(pattern):  # 패턴 전체가 매칭된 경우
                matches.append(i - len(pattern) + 2)  # 1-based 인덱스로 저장
                j = lps[j - 1]  # 다음 매칭을 위해 패턴 인덱스 초기화

    return matches


def main():
    import sys

    # 입력 데이터 처리 (첫 줄: 텍스트, 둘째 줄: 패턴)
    text, pattern = sys.stdin.read().splitlines()
    matches = kmp_search(text, pattern)  # KMP 알고리즘 실행
    print(len(matches))  # 매칭된 패턴의 개수 출력
    print(" ".join(map(str, matches)))  # 매칭된 위치 출력


if __name__ == "__main__":
    main()
