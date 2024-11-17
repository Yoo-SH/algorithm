# [RGB거리](https://www.acmicpc.net/problem/1149)

1. 입력값 (2<=N<=1000)
2. 입력값에 따른 빨,초,파 칠하는 비용 한 라인에 받음
3. 해당 하는 라인의 비용에 따라 최소 값 계산
4. N번까지 2~3과정 반복하여 비용의 최솟값 계산 

* 자료구조
    - key: value
    - 반복문으로 DP로직을 안에 넣음.
* 알고리즘
    - DP(앞에 선택한 거 고려X, **핵심은 앞에 있는 것에 영향을 받지 않아야함. 모든 케이스를 고려하면 안되고 단순화 해야함**)
        - 3.1 동일한거 제외 + 남은 두 개 비교해서 비용이 저렴한거 선택 하는 로직
            - 3.1.1 현재 색상 + 누적된 금액 저장
          
    - 왜 DP인가?(과거의 선택을 고려하면(이랬다면 어땠을까?) 경우의 수가 너무 많아짐. 현재와 미래의 최선의 선택만 고려. + 가지치지를 하면서 다 카운트 해서 다 계산한 후에 비교하면 경우의 수가 너무 많음.)
* 관련문제
15486