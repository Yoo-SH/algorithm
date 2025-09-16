# [두 개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644#)

## input
제한시간: 없음

## 설계

1. for 반복문을 이중으로 구현하여 두개의 합의 조합을 구한다.
2. 중복을 제거해야하므로 set 자료구조를 활용하여 리스에 저장한다.
3. 오름차순으로 정렬한다.

## 활용스킬 및 시간복잡도

* 자료구조
    - set, list
* 알고리즘
    - sort

* 시간 복잡도
    - O(n^2) : 이중 for문
    - O(n^2): 집합 변환
    - O(n log n) : 정렬
    - 최종: O(N^2 log N^2) = O(N^2 log N)

## 다른 풀이

```python
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j]) 
    return sorted(list(set(answer))) 
```

### 장점
- 연산횟수가 보다 적다
- 모든 경우의수를 조사하면서, 중복체크를 일일히 하지 않아도 된다.
- 리스트를 셋에 넣고 다시 리스트에 넣는 식으로 중복제거를 간단하게 하며 정렬까지 한번에 처리한다.