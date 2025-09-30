# 📝 알고리즘 문제 풀이 설계 양식

## 1. 문제 정보

* **문제 이름/번호:**:카드뭉치
* **문제 링크:** https://school.programmers.co.kr/learn/courses/30/lessons/159994
* **핵심 요구사항:** 카드 뭉치에서 특정 카드를 찾는 문제
* **제약조건:**
- 1 ≤ cards1의 길이, cards2의 길이 ≤ 10
    - 1 ≤ cards1[i]의 길이, cards2[i]의 길이 ≤ 10
    - cards1과 cards2에는 서로 다른 단어만 존재합니다.
- 2 ≤ goal의 길이 ≤ cards1의 길이 + cards2의 길이
    - 1 ≤ goal[i]의 길이 ≤ 10
    - goal의 원소는 cards1과 cards2의 원소들로만 이루어져 있습니다.
- cards1, cards2, goal의 문자열들은 모두 알파벳 소문자로만 이루어져 있습니다.

---

## 2. 입출력 정리

* **Input:**: cards1, cards2, goal
* **Output:**: boolean

---

## 3. 아이디어 구상

- goal의 각 단어를 순서대로 확인하면서 cards1과 cards2에서 해당 단어를 찾는다.
- cards1과 cards2에서 단어를 찾을 때, 각 카드 뭉치를 앞에서 부터 확인하며 찾는다.(cards1과 cards2 앞에 있는 단어만 사용 가능하므로 queue 사용)
- 만약 goal의 단어를 cards1과 cards2에서 모두 찾지 못하면 "No"를 반환한다.
- 모든 단어를 찾으면 "Yes"를 반환한다

---

## 4. 접근 방법

* **자료구조:**: queue,
* **알고리즘/패러다임:**: Greedy
* **접근 이유:** : 각 카드 뭉치에서 앞에 있는 단어만 사용 가능하므로 queue를 사용하여 앞에서부터 단어를 확인하는 것이 적합하다.

---

## 5. 풀이 절차 (precode)

1. 입력 처리
2. 주요 데이터 구조 세팅
3. 핵심 로직 순서도
4. 종료 조건 및 결과 반환

---

## 6. 예제 확인

* **주어진 예제:** 직접 손으로 풀어서 풀이 검증
* **엣지 케이스:** 최소 입력 / 최대 입력 / 특수 상황

---

## 7. 시간/공간 복잡도 분석

* 시간 복잡도:
* 공간 복잡도:

---

## 8. 구현 시 주의할 점

* 인덱스 / off-by-one
* 자료형 범위 (int vs long long)
* 입력 크기 때문에 `sys.stdin.readline` 같은 fast I/O 필요 여부

---

## 9. 코드 작성

```python
def solution(cards1 : list, cards2 : list, goal: list):
    
    for index, value in enumerate(goal):

        if cards1 and value == cards1[0]:
            cards1.pop(0)
        elif cards2 and value == cards2[0]:
            cards2.pop(0)
        else:
            return "No"


    return "Yes"
```
---


## 10. AI 피드백

좋은 시도 하셨어요 👍 제가 요청해주신 형식으로 피드백 드릴게요.

---

### 1. 잘한 점

* **직관적인 접근**: `goal` 배열을 순서대로 탐색하면서 `cards1`과 `cards2`에서 맨 앞 카드를 비교하는 방식은 문제 요구사항을 정확히 반영한 올바른 접근입니다.
* **간결한 흐름**: 불필요한 변수를 만들지 않고 `if-elif-else` 구조로 바로 조건을 처리해서 로직이 깔끔합니다.
* **경계 조건 처리**: `if cards1 and ...`, `if cards2 and ...` 형태로 빈 리스트에서 인덱스를 참조하지 않도록 안전하게 처리한 점이 좋습니다.

---

### 2. 개선할 점

* **성능 최적화 필요**: `list.pop(0)`은 **O(n)** 연산이므로, 리스트 길이가 길어지면 비효율적입니다. → `collections.deque`를 사용하면 맨 앞 원소를 뽑는 연산이 \*\*O(1)\*\*이 됩니다.
* **가독성 개선**: `for index, value in enumerate(goal):` 에서 `index`는 사용되지 않으므로 불필요합니다. 단순히 `for value in goal:`이 더 깔끔합니다.
* **함수 선언의 타입 힌트 개선**: Python에서는 `list`보다는 `List[str]` 같은 구체적인 타입을 적는 것이 더 명확합니다. (`from typing import List` 필요)

---

### 3. 개선한 버전 예시

```python
from collections import deque
from typing import List

def solution(cards1: List[str], cards2: List[str], goal: List[str]) -> str:
    # deque로 변환해서 pop(0) 대신 popleft() 사용 (O(1))
    cards1, cards2 = deque(cards1), deque(cards2)

    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.popleft()
        elif cards2 and word == cards2[0]:
            cards2.popleft()
        else:
            return "No"
    return "Yes"
```

**개선 포인트 설명**

* `deque.popleft()`를 사용해서 성능을 개선했습니다.
* `for word in goal:`로 불필요한 변수 제거 → 가독성 향상.
* `List[str]` 타입 힌트로 입력 자료형을 명확히 표현했습니다.

---
