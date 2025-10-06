# 📝 알고리즘 문제 풀이 설계 양식

## 1. 문제 정보

* **문제 이름/번호:**: 신고 결과 받기 / 92334
* **문제 링크:**: https://programmers.co.kr/learn/courses/30/lessons/92334
* **핵심 요구사항:**: 각 유저가 신고한 유저 목록과 신고 결과를 바탕으로, 각 유저가 받을 수 있는 경고 메시지의 수를 계산해야 한다.
* **제약조건:**:
- 2 ≤ id_list의 길이 ≤ 1,000
    - 1 ≤ id_list의 원소 길이 ≤ 10
    - id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
    - id_list에는 같은 아이디가 중복해서 들어있지 않습니다.
- 1 ≤ report의 길이 ≤ 200,000
    - 3 ≤ report의 원소 길이 ≤ 21
    - report의 원소는 "이용자id 신고한id"형태의 문자열입니다.
    - 예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
    - id는 알파벳 소문자로만 이루어져 있습니다.
    - 이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
    -  자기 자신을 신고하는 경우는 없습니다.
- 1 ≤ k ≤ 200, k는 자연수입니다.
    -  return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.

---

## 2. 입출력 정리

* **Input:** 
  - `id_list`: 유저 ID 목록 (예: ["muzi", "frodo", "apeach", "neo"])
  - `report`: 신고 기록 목록 (예: ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"])
  - `k`: 정지 기준 신고 횟수 (예: 2)
* **Output:**: 각 유저가 받을 수 있는 정지 처리 완료된 메일의 수 (예: [2, 1, 1, 0])

---

## 3. 아이디어 구상

- 역으로 날 신고한 사람을 value로 가지는 딕셔너리를 만든다.
- 신고한 사람은 set으로 중복을 제거한다.
- k번 이상 신고된 사람을 찾는다.
- k번 이상 신고된 사람을 신고한 사람들에게 메일을 보낸다.
---

## 4. 접근 방법

* **자료구조:**
  - 딕셔너리 해쉬 (defaultdict, dict)
  - 집합 (set)
  - 리스트 (list)
* **알고리즘/패러다임:** 
  - 구현
  - 시뮬레이션
  - 해쉬맵
* **접근 이유:** 
  - 효율적인 조회와 삽입을 위해 해쉬맵 사용
  - 중복 신고를 제거하기 위해 집합 사용
  - 결과를 순서대로 반환하기 위해 리스트 사용

---

## 5. 풀이 절차 (precode)

1. `report` 리스트를 순회하며, 각 신고 기록을 파싱하여 신고자와 피신고자를 분리한다.
2. 피신고자를 키로, 신고자를 값으로 가지는 딕셔너리를 생성한다. 이때, 신고자는 집합(set)으로 저장하여 중복 신고를 방지한다.
3. 딕셔너리를 순회하며, 각 피신고자가 받은 신고 횟수를 계산한다.
4. 신고 횟수가 `k` 이상인 피신고자를 찾는다.
5. 각 피신고자를 신고한 신고자들에게 메일을 보내기 위해, 신고자별로 메일 수를 카운트하는 딕셔너리를 생성한다.
6. 최종적으로 `id_list` 순서에 맞게 각 유저가 받은 메일 수를 리스트로 반환한다.
---

## 6. 예제 확인

* **주어진 예제:** 직접 손으로 풀어서 풀이 검증
* **엣지 케이스:** 최소 입력 / 최대 입력 / 특수 상황

---

## 7. 시간/공간 복잡도 분석

* 시간 복잡도: O(n) - n은 report의 길이
* 공간 복잡도: O(m) - m은 id_list의 길이

---

## 8. 구현 시 주의할 점

* 인덱스 / off-by-one
* 자료형 범위 (int vs long long)
* 입력 크기 때문에 `sys.stdin.readline` 같은 fast I/O 필요 여부

---

## 9. 코드 작성

```python
from collections import defaultdict

def solution(id_list, report, k):

    reported_dict = defaultdict(set)
    id_mail_dic = defaultdict(int)
    result = []

    # `report` 리스트를 순회하며, 각 신고 기록을 파싱하여 `reported_dict`에 신고당한 사람을 키로, 신고한 사람을 값으로 추가 (중복 제거 위해 집합 사용)
    for r in report:
        reporter, reported = r.split()
        reported_dict[reported].add(reporter)
    
    # `reported_dict`의 리스트 크기를 확인하여, 각 사람이 몇 번 신고당했는지 계산
    for reported, reporter_set in reported_dict.items():
        if len(reporter_set) >= k:
            for reporter in reporter_set:
                id_mail_dic[reporter] += 1
        
    # `id_list` 순서대로 결과 리스트를 생성하여 반환
    for id in id_list:
        result.append(id_mail_dic[id])

    return result
```
## 10. AI 피드백

좋습니다 👍 주신 코드에 대해 문제 설명과 함께 피드백을 드릴게요.

---

### 1. 잘한 점

* **자료구조 선택이 적절함**:
  `defaultdict(set)`을 사용해서 중복 신고를 자연스럽게 제거한 점이 매우 좋습니다.
  `defaultdict(int)`로 메일 횟수 초기값을 `0`으로 관리한 것도 깔끔합니다.
* **로직이 명확하게 분리됨**:
  신고 내역을 저장하는 단계 → 정지된 유저 확인 → 메일 횟수 집계 → 최종 결과 반환 단계로 나누어 가독성이 좋습니다.
* **문제 조건을 충실히 반영**:
  같은 사람이 여러 번 같은 유저를 신고해도 한 번만 반영되도록 set을 사용한 점이 문제 조건에 잘 맞습니다.

---

### 2. 개선할 점

* **변수명 개선**:
  `id_mail_dic` → `mail_count`, `reported_dict` → `reported_by` 같이 좀 더 직관적으로 표현하면 가독성이 좋아집니다.
* **리스트 컴프리헨션 활용**:
  마지막 결과 리스트 생성 부분을 `for` 루프 대신 컴프리헨션으로 바꾸면 더 간결해집니다.
* **중간 자료구조 재활용 가능성**:
  `reported_dict`를 만들고 다시 순회하는 대신, 동시에 신고 횟수를 카운트하는 방식으로 메모리를 조금 줄일 수 있습니다. (현재 방식도 충분히 효율적이지만, 입력 크기가 커질 수 있으므로 참고할 만합니다.)

---

### 3. 개선한 버전 예시

```python
from collections import defaultdict

def solution(id_list, report, k):
    # 신고당한 유저별 신고자 집합
    reported_by = defaultdict(set)
    # 메일 횟수 결과 저장
    mail_count = defaultdict(int)
    
    # 신고 내역 정리 (중복 제거는 set이 알아서 처리)
    for r in report:
        reporter, reported = r.split()
        reported_by[reported].add(reporter)

    # 정지된 유저 확인 후, 신고자들에게 메일 횟수 추가
    for reported, reporters in reported_by.items():
        if len(reporters) >= k:
            for reporter in reporters:
                mail_count[reporter] += 1

    # id_list 순서대로 결과 반환
    return [mail_count[user] for user in id_list]
```

**개선 포인트 설명**:

* 변수명을 더 직관적으로 변경하여 코드 읽기가 쉬워졌습니다.
* 결과 리스트를 리스트 컴프리헨션으로 작성하여 더 간결하게 표현했습니다.
* 로직은 동일하되 가독성과 유지보수성을 높였습니다.

---

👉 이 문제는 **set을 통한 중복 제거**와 **defaultdict의 기본값 처리**가 핵심 포인트인데, 이미 잘 활용하셨습니다.
개선 버전은 "읽기 좋은 코드" 방향으로 최적화한 것이지, 성능적으로는 큰 차이는 없습니다.

혹시 원하시면 제가 **시간 복잡도 분석**도 같이 해드릴까요?
