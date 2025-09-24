# 📝 알고리즘 문제 풀이 설계 양식

## 1. 문제 정보

* **문제 이름/번호:** 괄호 회전하기 (PGS 76502)
* **문제 링크:** [링크](https://school.programmers.co.kr/learn/courses/30/lessons/76502)
* **핵심 요구사항:** 주어진 괄호 문자열이 올바른 괄호 문자열인지 판별
* **제약조건:** 문자열 길이 1 ≤ s ≤ 1,000

---

## 2. 입출력 정리

* **Input:**
    - 문자열 s
* **Output:**
    - s가 올바른 괄호 문자열이 되게 하는 x의 개수

---

## 3. 아이디어 구상

* 문자열 s를 x만큼 회전시킨다.
* 회전된 문자열이 올바른 괄호 문자열인지 확인한다.
    - 올바른 괄호 문자열인지 확인하는 방법
        - 스택 자료구조를 활용
        - 여는 괄호를 만나면 스택에 push
        - 닫는 괄호를 만나면 스택에서 pop 하여 매칭
            - 매칭 되지 않으면 올바르지 않은 문자열
        - 스택이 비어있는데 닫는 괄호가 나오면 올바르지 않은 문자열
        - 모든 문자를 다 처리한 후 스택이 비어있으면 올바른 문자열
* x를 0부터 len(s)-1까지 변화시키며 올바른 괄호 문자열인지 확인


---

## 4. 접근 방법

* **자료구조:** Stack (list 활용)
* **알고리즘/패러다임:** 
* **접근 이유:** 스택을 활용한 괄호 매칭이 직관적이고 효율적이기 때문 FILO 구조로 여는 괄호를 저장하고 닫는 괄호가 나올 때 매칭하는 방식이 적합.

---

## 5. 풀이 절차 (precode)

1. 입력 처리
    - 문자열 s를 입력받는다.
2. 주요 데이터 구조 세팅
    - 스택을 초기화한다.
3. 핵심 로직 순서도
    - 문자열 s를 x만큼 회전시킨다.
    - 회전된 문자열이 올바른 괄호 문자열인지 확인한다.
        - 여는 괄호를 만나면 스택에 push
        - 닫는 괄호를 만나면 스택에서 pop 하여 매칭
            - 매칭 되지 않으면 올바르지 않은 문자열
        - 스택이 비어있는데 닫는 괄호가 나오면 올바르지 않은 문자열
        - 모든 문자를 다 처리한 후 스택이 비어있으면 올바른 문자열
4. 종료 조건 및 결과 반환
    - x를 0부터 len(s)-1까지 변화시키며 올바른 괄호 문자열인지 확인
    - 올바른 괄호 문자열이 되는 경우의 수를 반환

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

---

## 9. 코드 작성

```Python
def check_is_matched(s:str):
    stack_for_parentheses = []

    for c in s:
        if c in "{([":
            stack_for_parentheses.append(c)
        elif c == "}":
            try:
                pop_c = stack_for_parentheses.pop()
                if pop_c != "{":
                    return False
            except IndexError:
                return False
        elif c == ")":
            try:
                pop_c = stack_for_parentheses.pop()
                if pop_c != "(":
                    return False
            except IndexError:
                return False
        elif c == "]":
            try:
                pop_c = stack_for_parentheses.pop()
                if pop_c != "[":
                    return False
            except IndexError:
                return False
    
    # 모든 문자를 다 처리한 후 스택이 비어있는지 확인
    if stack_for_parentheses:
        return False
    else:
        return True
            
    

def rotate_to_right(s:str, x: int):
    # 오른쪽으로 x칸씩 이동
    s = s[-x:] + s[:-x]
    return s

def solution(s):

    count_is_matched = 0                    

    # 회전시키면서 문자열이 맞는지 확인
    for x in range(0,len(s)):
        if check_is_matched(rotate_to_right(s,x)):
            count_is_matched += 1
        
        
    return count_is_matched
```

## 10. AI 피드백

### ✅ 잘한 점

1. **스택 활용**
   괄호 짝 검사를 전형적인 방식인 스택으로 구현하여 가독성과 직관성이 높습니다.

2. **예외 처리**
   `IndexError` 예외를 활용하여 스택이 비었을 때 잘못된 괄호 구조임을 바로 판별하는 점이 안정적입니다.

3. **코드 분리**

   * `check_is_matched` : 괄호 유효성 검사
   * `rotate_to_right` : 문자열 회전
   * `solution` : 전체 흐름 제어
     함수 분리로 인해 코드 구조가 명확하고 유지보수가 용이합니다.

4. **최종 검증**
   모든 문자를 처리한 후 스택이 비어있는지 확인하는 부분(`if stack_for_parentheses:`)이 포함되어 있어 논리적 완결성이 있습니다.

---

### ⚠️ 개선할 점

1. **중복 코드 제거**
   `check_is_matched` 함수에서 `}`, `)`, `]` 처리 로직이 유사하게 반복되고 있습니다.
   → `dict` 매핑을 사용하면 중복을 줄일 수 있습니다.

   ```python
   pairs = {")": "(", "}": "{", "]": "["}
   if c in pairs:
       if not stack_for_parentheses or stack_for_parentheses.pop() != pairs[c]:
           return False
   ```

2. **문자열 회전 최적화**
   `rotate_to_right` 함수는 문자열 슬라이싱을 매번 새로 수행합니다.

   * 길이가 `n`인 문자열에 대해 `n`번 회전하므로 O(n²) 복잡도가 발생합니다.
   * 실제로는 **왼쪽 회전**만 해도 충분합니다. (예: 오른쪽 1칸 회전 = 왼쪽 (n-1)칸 회전)
   * 또는 `collections.deque`의 `rotate()`를 활용하면 성능이 개선됩니다.

3. **함수명 개선**

   * `check_is_matched` → `is_balanced_parentheses`
   * `rotate_to_right` → `rotate_string_right`
     조금 더 직관적인 이름으로 바꾸면 다른 개발자도 이해하기 쉬워집니다.

4. **테스트 케이스 필요**
   다양한 입력값(`"()[]{}"`, `"([)]"`, `""`, `")("`)에 대한 유닛 테스트 코드가 추가되면 더 견고한 풀이가 됩니다.

---

### 🌟 개선된 버전 예시

```python
def is_balanced_parentheses(s: str) -> bool:
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack


from collections import deque

def solution(s: str) -> int:
    dq = deque(s)
    count = 0

    for _ in range(len(s)):
        if is_balanced_parentheses("".join(dq)):
            count += 1
        dq.rotate(-1)  # 왼쪽으로 1칸 회전
    return count
```

---

👉 요약하면, **현재 코드도 문제 해결에는 충분히 올바르지만, 중복 제거 / 효율성 개선 / 함수명 명확화 / 테스트 보강**을 하면 더 깔끔하고 확장 가능한 코드가 됩니다.