# [부녀회장이 될테야](https://www.acmicpc.net/problem/2775)

## input
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

## output
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

## precode
1. 아파트 층수 및 호수를 나타내는 15x15 배열 초기화
2. 0층 1호부터 14호까지 초기화
3. 각 층의 1호부터 14호까지의 사람 수 계산



* 알고리즘
    - DP
        - 이전 호실의 사람이 이미 계산되어 있으므로 이를 이용하여 계산. 처음 부터 다시 구할 필요가 없음
* 자료구조
    - list
* 관련자료