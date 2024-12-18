# [가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)

## input
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

## output
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.


## precode
1. N(수열의 크기)와 수열 A를 입력받는다.
2. dp 리스트를 생성한다. dp[i]는 i번째 원소를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이를 저장한다.
3. dp[i]를 1로 초기화한다.
4. 0부터 i-1까지의 j에 대해, A[i] > A[j]이면 dp[i] = max(dp[i], dp[j] + 1)을 수행한다.
5. dp 리스트의 최댓값을 출력한다.



* 자료구조
    - list
* 알고리즘
    - DP
       - LIS(Longest Increasing Subsequence), 최장 증가 부분 수열
* 시간 복잡도

* 참고 자료
    - [[알고리즘] LIS 알고리즘인데 DP를 이용한](https://velog.io/@doorbals_512/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-LIS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B8%EB%8D%B0-DP%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C)