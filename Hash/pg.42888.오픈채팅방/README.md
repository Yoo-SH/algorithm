# 📝 알고리즘 문제 풀이 설계 양식

## 1. 문제 정보

* **문제 이름/번호:**: 오픈채팅방
* **문제 링크:**: https://programmers.co.kr/learn/courses/30/lessons/42888
* **핵심 요구사항:**: 채팅방에서 유저의 닉네임 변경 이력을 바탕으로 최종적으로 남은 메시지를 반환
* **제약조건:**:
- record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
- 다음은 record에 담긴 문자열에 대한 설명이다.
    - 모든 유저는 [유저 아이디]로 구분한다.
    - [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
    - [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
    - [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
    - 첫 단어는 Enter, Leave, Change 중 하나이다.
    - 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
    - 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
    - 유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
    - 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.

---

## 2. 입출력 정리

* **Input:** record: ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
* **Output:** ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다.", "Ryan님이 나갔습니다."]

---

## 3. 아이디어 구상

* **핵심 아이디어:**
1. 각 유저의 최종 닉네임을 저장하기 위해 딕셔너리 사용
2. 기록을 순회하며 Enter와 Change 명령어에 대해 딕셔너리 업데이트
3. 다시 기록을 순회하며 Enter와 Leave 명령어에 대해 최종 메시지 생성



---

## 4. 접근 방법

* **자료구조:** 딕셔너리
* **알고리즘/패러다임:** 해시 맵
* **접근 이유:** 유저의 최종 닉네임을 빠르게 조회하고 업데이트하기 위해

---

## 5. 풀이 절차 (precode)

1. 빈 딕셔너리 `user_dict` 생성
2. `record` 배열을 순회하며:
   - 명령어를 공백으로 분리
   - 명령어가 "Enter" 또는 "Change"인 경우, `user_dict`에 유저 아이디와 닉네임 저장/업데이트
3. 빈 리스트 `result` 생성
4. `record` 배열을 다시 순회하며:
   - 명령어를 공백으로 분리
   - 명령어가 "Enter"인 경우, `user_dict`에서 유저 아이디로 닉네임 조회 후 "님이 들어왔습니다." 메시지 추가
   - 명령어가 "Leave"인 경우, `user_dict`에서 유저 아이디로 닉네임 조회 후 "님이 나갔습니다." 메시지 추가
5. `result` 리스트 반환
---

## 6. 예제 확인

* **주어진 예제:** 직접 손으로 풀어서 풀이 검증
* **엣지 케이스:** 최소 입력 / 최대 입력 / 특수 상황

---

## 7. 시간/공간 복잡도 분석

* 시간 복잡도: O(n) - record 배열을 두 번 순회
* 공간 복잡도: O(m) - m은 유저의 수 (최대 100,000명)

---

## 8. 구현 시 주의할 점

* 인덱스 / off-by-one
* 자료형 범위 (int vs long long)
* 입력 크기 때문에 `sys.stdin.readline` 같은 fast I/O 필요 여부

---

## 9. 코드 작성

```python
def solution(record):

    user_dict :dict = {}
    result = []

    # 유저 최종 닉네임 확인
    for i in record:
        parts = i.split()
        command = parts[0]
        user_id = parts[1]

        if command in ["Enter", "Change"]:
            nick_name = parts[2]
            user_dict[user_id] = nick_name


    # 유저 채팅방 결과 생성
    for i in record:
        parts = i.split()
        command = parts[0]
        user_id = parts[1]

        if command == "Enter":
            result.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif command == "Leave":
            result.append(f"{user_dict[user_id]}님이 나갔습니다.")
    
    
    return result
```

---




## 10. AI 피드백

좋습니다 👍 요청해주신 형식에 맞춰 피드백 드릴게요.

---

### 1. 잘한 점

* **최종 닉네임을 먼저 계산**한 뒤 메시지를 만드는 구조 → `Change` 이벤트가 과거 기록까지 반영되는 문제 요구사항을 올바르게 처리했음.
* **`dict`를 활용**하여 `user_id → nick_name` 매핑을 관리한 점이 효율적임. O(1) 접근 가능.
* **조건 분기 명확성**: `Enter`, `Leave`, `Change`를 구분하여 로직을 단순화한 점이 가독성에 좋음.

---

### 2. 개선할 점

* **중복된 split() 호출**: 두 번의 반복에서 각각 문자열을 `split()`하고 있어 불필요한 연산이 발생함. 한 번 파싱해 리스트에 저장하면 더 효율적.
* **가독성 개선**: `"Enter"`, `"Leave"`, `"Change"` 문자열 비교가 반복되는데, 이를 `if-elif` 구조 대신 명시적으로 처리하거나 이벤트 타입 분리하면 더 직관적.
* **타입 힌트 보강**: 함수 인자와 반환 타입에 타입 힌트를 추가하면 가독성과 유지보수성이 향상됨.

---

### 3. 개선한 버전 예시

```python
from typing import List

def solution(record: List[str]) -> List[str]:
    user_dict = {}
    actions = []  # (command, user_id)만 저장

    # 1. 유저 닉네임 최신화
    for rec in record:
        parts = rec.split()
        command, user_id = parts[0], parts[1]

        if command in ("Enter", "Change"):
            nick_name = parts[2]
            user_dict[user_id] = nick_name

        # 메시지 출력에 필요한 이벤트만 기록
        if command in ("Enter", "Leave"):
            actions.append((command, user_id))

    # 2. 결과 메시지 생성
    result = []
    for command, user_id in actions:
        if command == "Enter":
            result.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        else:  # "Leave"
            result.append(f"{user_dict[user_id]}님이 나갔습니다.")

    return result
```

**개선 포인트 설명**

* `split()` 결과를 한 번만 사용하도록 `actions` 리스트에 `(command, user_id)` 저장 → 불필요한 반복 제거.
* `actions`에 필요한 이벤트만 저장 → 로직이 깔끔해짐.
* `typing.List`를 활용해 입력/출력 타입 명확히 표시 → 유지보수성 강화.

---

👉 이 방식은 시간복잡도 **O(N)**, 공간복잡도 **O(N)**으로 동일하지만, 중복 연산을 줄이고 코드 가독성을 개선합니다.

원하시면 제가 **메모리 최적화 버전 (in-place 처리)** 도 한번 만들어드릴까요?
