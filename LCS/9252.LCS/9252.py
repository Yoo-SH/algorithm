def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 역추적
    i, j = n, m
    lcs_result = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # LCS 결과 반환
    lcs_result.reverse()
    return dp[n][m], "".join(lcs_result)


if __name__ == "__main__":
    # 입력 받기
    s1 = input().strip()
    s2 = input().strip()

    # LCS 계산 및 출력
    length, lcs_sequence = lcs(s1, s2)
    print(length)
    print(lcs_sequence)
