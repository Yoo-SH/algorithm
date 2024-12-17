import sys

input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())  # 멀티탭 구멍 수 N, 사용 횟수 K
arr = list(map(int, input().split()))  # 기기 사용 순서

multitap = []  # 멀티탭에 꽂혀있는 기기 리스트
count = 0  # 교체 횟수

for i in range(K):
    current_device = arr[i]

    # 이미 멀티탭에 꽂혀 있는 경우
    if current_device in multitap:
        continue

    # 멀티탭에 빈 자리가 있는 경우
    if len(multitap) < N:
        multitap.append(current_device)
        continue

    # 교체할 기기 찾기
    last_use_index = -1
    remove_device = -1

    for device in multitap:
        try:
            # 멀티탭에 꽂힌 기기 중 다음 사용 위치 확인
            next_use = arr[i + 1 :].index(device)
        except ValueError:
            # 이후에 사용되지 않는 경우
            next_use = float("inf")

        # 가장 나중에 사용될 기기 찾기
        if next_use > last_use_index:
            last_use_index = next_use
            remove_device = device

    # 가장 나중에 사용될 기기를 제거하고 새로운 기기 추가
    multitap.remove(remove_device)
    multitap.append(current_device)
    count += 1  # 교체 횟수 증가

print(count)
