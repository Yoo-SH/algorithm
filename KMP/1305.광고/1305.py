def compute_lps(pattern: str) -> list[int]:
    """주어진 패턴에 대한 LPS(Longest Prefix Suffix) 배열을 계산"""
    lps = [0] * len(pattern)  # LPS 배열 초기화
    j = 0  # 접두사 끝 포인터

    for i in range(1, len(pattern)):
        # 접두사와 접미사가 일치하지 않을 경우
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        # 접두사와 접미사가 일치하는 경우
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def min_advertising_length(length: int, text: str) -> int:
    """광고판의 최소 길이를 계산"""
    lps = compute_lps(text)  # LPS 배열 계산
    return length - lps[-1]  # 최소 광고판 길이 = 전체 길이 - 마지막 LPS 값


def main():
    import sys

    input = sys.stdin.read

    # 입력 처리
    length = int(input().strip())  # 문자열 길이
    text = input().strip()  # 문자열 내용

    # 결과 계산 및 출력
    print(min_advertising_length(length, text))


if __name__ == "__main__":
    main()
