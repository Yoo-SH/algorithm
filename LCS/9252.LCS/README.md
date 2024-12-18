# [LCS 2](https://www.acmicpc.net/problem/9252)

## input

## output

## precode

* 자료구조
    - list  
* 알고리즘
    - DP
        - (DP)를 사용하여 두 문자열의 공통 부분 수열 길이를 계산하고, 이를 바탕으로 역추적하여 실제 공통 부분 수열을 생성.
    - LCS
        - 두 문자열의 최장 공통 부분 수열을 찾는 문제.
* 시간복잡도
DP 테이블 채우기: 𝑂(𝑛×𝑚)
역추적: O(n+m).
전체 시간복잡도: 𝑂(𝑛×𝑚)


* 참고자료
    - [[알고리즘] 그림으로 알아보는 LCS 알고리즘 - Longest Common Substring와 Longest Common Subsequence](https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence)