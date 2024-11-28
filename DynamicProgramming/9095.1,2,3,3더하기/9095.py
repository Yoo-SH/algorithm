def count_ways_to_sum(n: int) -> int:
    # DP 테이블 초기화
    if n == 0:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1  # 아무것도 더하지 않는 경우
    dp[1] = 1  # 1을 만드는 방법 [1]

    if n >= 2:
        dp[2] = 2  # 2를 만드는 방법 [1+1, 2]
    if n >= 3:
        dp[3] = 4  # 3을 만드는 방법 [1+1+1, 1+2, 2+1, 3]

    # 점화식에 따라 DP 테이블 채우기
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(count_ways_to_sum(n))
