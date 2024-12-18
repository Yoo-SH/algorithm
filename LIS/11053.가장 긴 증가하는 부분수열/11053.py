# 백준 11053번 문제 풀이
n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열 입력

dp = [1] * n  # LIS 길이를 저장하는 DP 배열 초기화

# LIS 계산
for i in range(n):
    for j in range(i):  # i보다 앞의 원소들 탐색
        if arr[j] < arr[i]:  # 증가 조건 확인
            dp[i] = max(dp[i], dp[j] + 1)

# 최댓값 출력
print(max(dp))
