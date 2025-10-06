# 📝 알고리즘 문제 풀이 설계 양식

## 1. 문제 정보

* **문제 이름/번호:**: 완주하지 못한 선수
* **문제 링크:**: https://programmers.co.kr/learn/courses/30/lessons/42576
* **핵심 요구사항:**: 마라톤에 참여한 선수들의 이름과 완주한 선수들의 이름이 주어질 때, 완주하지 못한 선수의 이름을 반환
* **제약조건:**: 
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

---

## 2. 입출력 정리

* **Input:**: participant, completion 배열
  - participant: 마라톤에 참여한 선수들의 이름이 들어있는 배열
  - completion: 마라톤을 완주한 선수들의 이름이 들어있는 배열
* **Output:**: 완주하지 못한 선수의 이름

---

## 3. 아이디어 구상

* **핵심 아이디어:**: 두 배열을 정렬한 후, 인덱스를 비교하여 다른 이름을 찾는다.
* **대안 아이디어:**: 해시맵을 사용하여 각 이름의 등장 횟수를 세고, 완주한 선수들의 이름을 빼는 방법도 고려.
---

## 4. 접근 방법

* **자료구조:**: 해시맵 (딕셔너리)
* **알고리즘/패러다임:**: 해시 테이블
* **접근 이유:**: 해시맵을 사용하면 각 선수의 이름을 키로 하여 등장 횟수를 쉽게 세고, 완주한 선수들의 이름을 빠르게 확인할 수 있다. 이중 반복문으로 진행하면 시간 복잡도가 O(n^2)이 될 수 있지만, 해시맵을 사용하면 O(n)으로 해결 가능.

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
```Python
from collections import Counter

def solution(participant, completion):
    
    completion_dictionary = dict(Counter(completion)) # 특정 인원수를 기록하는 딕셔너리, 동명이인도 카운트
    result : str 

    for part in participant:
        if part not in completion_dictionary or completion_dictionary[part] == 0:
            result = part
        else: 
            completion_dictionary[part] -=1 # 동명이인이 있는 경우를 고려하여 갯수 감소


    return result
```



## 10. AI 피드백

### 1. 잘한 점

- **Counter 사용**: `collections.Counter`를 활용하여 동명이인 문제를 효과적으로 처리했습니다. 각 이름의 출현 횟수를 정확히 카운트하는 좋은 접근입니다.

- **동명이인 고려**: `completion_dictionary[part] -= 1`로 카운트를 감소시켜 동명이인이 여러 명 있는 경우도 올바르게 처리했습니다.

- **명확한 로직**: 딕셔너리에 없거나 카운트가 0인 경우를 확인하는 조건문이 직관적이고 이해하기 쉽습니다.

### 2. 개선할 점

- **시간 복잡도 비효율**: 현재 O(n)이지만 participant를 순회하면서 매번 딕셔너리를 확인하고 수정합니다. participant도 Counter로 만들어 한 번에 비교하면 더 효율적입니다.

- **불필요한 반복문**: 모든 participant를 순회하지 않고도 두 Counter 객체를 빼기 연산으로 바로 차이를 구할 수 있습니다. Counter는 빼기 연산(`-`)을 지원하여 더 간결한 코드 작성이 가능합니다.

- **타입 힌트 오류**: `result : str`로 선언했지만 초기값이 없어 잠재적 버그가 있습니다. 만약 모든 선수가 완주한 경우(문제에서는 불가능하지만) UnboundLocalError가 발생할 수 있습니다.

### 3. 개선한 버전 예시

```python
from collections import Counter

def solution(participant, completion):
    # 두 리스트를 모두 Counter로 변환
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    # Counter 빼기 연산으로 차이 계산 (완주하지 못한 선수만 남음)
    # Counter 빼기는 음수 값을 제거하므로 완주하지 못한 선수만 남음
    result_counter = participant_counter - completion_counter
    
    # 결과 딕셔너리에서 키(이름) 하나를 반환
    # most_common(1)은 [(이름, 횟수)] 형태로 반환
    return list(result_counter.keys())[0]

# 또는 더 간결한 버전
def solution_v2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
```

**주요 개선사항:**
1. **Counter 빼기 연산 활용**: `Counter(participant) - Counter(completion)`으로 한 줄에 차이를 계산하여 코드가 더 간결하고 가독성이 높아졌습니다.

2. **반복문 제거**: 명시적인 for 루프 없이 Counter의 내장 연산으로 처리하여 더 Pythonic하고 효율적입니다.

3. **안정성 향상**: 조건문과 변수 수정 없이 불변 방식으로 처리하여 논리 오류 가능성이 줄어듭니다.