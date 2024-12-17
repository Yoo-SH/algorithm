n, k = map(int, input().split())  # 동전 종류의 수 n, 목표 금액 k
coins = []  # 동전 리스트

for _ in range(n):
    coins.append(int(input()))  # 동전 입력 받기

coins.sort(reverse=True)  # 내림차순으로 정렬 (큰 동전부터 사용)

count = 0  # 사용한 동전 개수

for coin in coins:
    if k == 0:  # 목표 금액이 0이면 종료
        break
    if coin <= k:  # 현재 동전이 남은 금액보다 작거나 같을 때
        count += k // coin  # 해당 동전으로 최대한 사용할 수 있는 개수 추가
        k %= coin  # 남은 금액 갱신

print(count)
