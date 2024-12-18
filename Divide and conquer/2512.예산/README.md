# [예산](https://www.acmicpc.net/problem/2512)

## input
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 

## output
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 

## precode
1. 지방의 수(N)에 대해서 입력값을 받아 해당 하는 수 만큼 지방 예산 요청을 리스트에 보관한 뒤, 총 예산을 입력받는다.
2. 리스트의 존재하는 값들을 모두 계산한 뒤, 총 예산보다 적으면 해당 예산 리스트 중 가장 큰 값을 출력한다.
3.  총 예산보다 예산 리스트 합들이 더 크면, 상한액을 정한다
    - 중간값(mid)을 상한선 후보로 사용하여 각 예산 항목을 상한선 이하로 제한했을 때의 총합(temp_Bugets_total)을 계산합니다.
    - temp_Bugets_total이 중앙정부 예산보다 작거나 같으면 더 큰 상한선을 탐색합니다.
    - 그렇지 않으면 더 작은 상한선을 탐색합니다.
    - 범위를 좁혀가며 조건을 만족하는 가장 큰 상한선을 찾습니다

* 자료구조
    - list
* 알고리즘
    - 이진 탐색
    
* 참고자료

```
     완전 탐색 방식: 
     상한선을 1씩 줄여가며 모든 경우를 확인하는 방식은 최악의 경우 O(M × N)의 시간 복잡도를 가집니다. 여기서 M은 상한선의 범위(최대 예산)이고, N은 요청된 예산의 개수입니다.
     만약 예산 항목 수 N이 10만 개이고 최대 예산 M이 10만이라면, 100억 번의 연산이 필요할 수 있습니다.

    이진 탐색 방식:
    상한선을 절반씩 줄여가며 확인하기 때문에 O(log(M) × N)의 시간 복잡도를 가집니다.
    같은 조건에서도 연산 횟수가 대폭 줄어듭니다. 예를 들어, 최대 예산 M이 10만이라면 log2(10만) ≈ 17번만 탐색합니다.
```
