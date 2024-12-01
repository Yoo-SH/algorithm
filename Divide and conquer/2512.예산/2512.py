if __name__ == "__main__":
    # 입력 처리
    N = int(input())
    localGovernmentRequireBugets = list(map(int, input().split()))
    centralGovernmentBuget = int(input())

    # 요청 예산 총합 계산
    localGovernmentRequireBugets_total = sum(localGovernmentRequireBugets)

    # 요청 예산이 중앙정부 예산보다 작으면 가장 큰 요청 예산 출력
    if localGovernmentRequireBugets_total <= centralGovernmentBuget:
        print(max(localGovernmentRequireBugets))
    else:
        # 상한선 초기값 설정
        upperLimit = max(localGovernmentRequireBugets)

        # 상한선을 이진 탐색으로 찾기
        start = 0
        end = upperLimit
        result = 0

        while start <= end:
            mid = (start + end) // 2  # 현재 상한선 후보
            temp_Bugets_total = 0

            # 상한선을 기준으로 예산 총합 계산
            for budget in localGovernmentRequireBugets:
                temp_Bugets_total += min(budget, mid)

            # 중앙정부 예산에 맞는지 확인
            if temp_Bugets_total <= centralGovernmentBuget:
                result = mid  # 가능한 상한선 저장
                start = mid + 1  # 더 큰 상한선을 탐색
            else:
                end = mid - 1  # 더 작은 상한선을 탐색

        print(result)
