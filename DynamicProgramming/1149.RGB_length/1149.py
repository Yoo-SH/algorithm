if __name__ == "__main__":
    # 1. 리스트안에, 딕셔너리로 값을 저장한다.
    N = int(input())
    RGB_store = [{"R": 0, "G": 0, "B": 0} for _ in range(N)]

    for i in range(N):
        R_cost, G_cost, B_cost = map(int, input().split())
        RGB_store[i]["R"] = R_cost
        RGB_store[i]["G"] = G_cost
        RGB_store[i]["B"] = B_cost

    # 2. 동적 계획법(DP)을 위한 리스트를 초기화한다.
    #    dp[i]["R"]: i번째 집까지의 최소 비용으로 R을 선택한 경우
    #    dp[i]["G"]: i번째 집까지의 최소 비용으로 G를 선택한 경우
    #    dp[i]["B"]: i번째 집까지의 최소 비용으로 B를 선택한 경우
    dp = [{"R": 0, "G": 0, "B": 0} for _ in range(N)]

    # 3. 첫 번째 집의 비용은 그대로 DP 테이블에 저장한다.
    dp[0] = RGB_store[0]

    # 4. 두 번째 집부터 N번째 집까지 DP 점화식을 적용하여 최소 비용 계산
    for i in range(1, N):
        dp[i]["R"] = RGB_store[i]["R"] + min(dp[i - 1]["G"], dp[i - 1]["B"])
        dp[i]["G"] = RGB_store[i]["G"] + min(dp[i - 1]["R"], dp[i - 1]["B"])
        dp[i]["B"] = RGB_store[i]["B"] + min(dp[i - 1]["R"], dp[i - 1]["G"])

    print(min(dp[N - 1]["R"], dp[N - 1]["G"], dp[N - 1]["B"]))
