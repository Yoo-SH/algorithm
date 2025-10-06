# 📝 알고리즘 문제 풀이 설계 양식

## 1. 문제 정보

* **문제 이름/번호:**: 베스트 앨범 / 42579
* **문제 링크:** https://school.programmers.co.kr/learn/courses/30/lessons/42579
* **핵심 요구사항:** 장르별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려고 합니다. 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 return 하도록 solution 함수를 완성하세요.
* **제약조건:** 
    * genres[i]는 고유번호가 i인 노래의 장르입니다.
    * plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
    * genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
    * 장르 종류는 100개 미만입니다.
    * 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
    * 모든 장르는 재생된 횟수가 다릅니다.

---

## 2. 입출력 정리

* **Input:**: 
    * genres: ["classic", "pop", "classic", "classic", "pop"]
    * plays: [500, 600, 150, 800, 2500]
* **Output:**: [4, 1, 3]

---

## 3. 아이디어 구상

- 장르별로 노래를 그룹화하고, 각 장르의 총 재생 횟수를 계산합니다.
- 각 장르 내에서 노래를 재생 횟수 기준으로 정렬하고, 재생 횟수가 같은 경우 고유번호 기준으로 정렬합니다.
- 총 재생 횟수를 기준으로 장르를 내림차순으로 정렬합니다.
- 각 장르에서 최대 두 개의 노래를 선택하여 결과 리스트에 추가합니다.
---

## 4. 접근 방법

* **자료구조:**: 해쉬, 리스트
* **알고리즘/패러다임:** 정렬, 그리디
* **접근 이유:** 장르별로 노래를 그룹화하고 정렬하는 것이 핵심이므로, 해쉬맵을 사용하여 장르별 노래 리스트를 관리하고, 정렬을 통해 우선순위를 쉽게 결정할 수 있습니다.

---

## 5. 풀이 절차 (precode)

1. 장르별로 노래를 그룹화하고, 각 장르의 총 재생 횟수를 계산합니다.
   - `genre_to_songs`: 장르를 키로 하고, (재생 횟수, 고유번호) 튜플의 리스트를 값으로 가지는 딕셔너리 생성
   - `genre_to_total_plays`: 장르를 키로 하고, 총 재생 횟수를 값으로 가지는 딕셔너리 생성
2. 각 장르 내에서 노래를 재생 횟수 기준으로 정렬하고, 재생 횟수가 같은 경우 고유번호 기준으로 정렬합니다.
3. 총 재생 횟수를 기준으로 장르를 내림차순으로 정렬합니다.
4. 각 장르에서 최대 두 개의 노래를 선택하여 결과 리스트에 추가합니다.
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
from collections import defaultdict

def solution(genres, plays):
    genre_to_songs_dict = defaultdict(list)
    genre_to_total_plays_dict = defaultdict(int)
    result =[]

    # 장르를 키로 하고, (재생 횟수, 고유번호) 튜플의 리스트를 값으로 가지는 딕셔너리 생성
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_to_songs_dict[genre].append((play, index))

    #  장르를 키로 하고, 총 재생 횟수를 값으로 가지는 딕셔너리 생성 + 각 장르 내에서 노래를 재생 횟수 기준으로 정렬하고, 재생 횟수가 같은 경우 고유번호 기준으로 정렬합니다.
    for genre, play_list in genre_to_songs_dict.items():
        genre_to_total_plays_dict[genre] = sum(play for play, _ in play_list)
        play_list.sort(key=lambda x: x[0], reverse=True) # 큰 순서대로 내림차순 정렬

    #  총 재생 횟수를 기준으로 장르를 내림차순으로 정렬합니다
    genre_sorted_list = sorted(genre_to_total_plays_dict.items(), key=lambda x: x[1], reverse=True)

    # 각 장르에서 최대 두 개의 노래를 선택하여 인덱스 번호를 결과 리스트에 추가합니다.
    for genre, _ in genre_sorted_list:
        for i in range(min(2, len(genre_to_songs_dict[genre]))):  # 장르에 노래가 1개만 있을 수도 있음
            result.append(genre_to_songs_dict[genre][i][1])

    return result
```
---



## 10. AI 피드백

### 1. 잘한 점

- **적절한 자료구조 선택**: `defaultdict`를 사용하여 장르별 데이터를 깔끔하게 그룹화했고, 튜플 `(play, index)`로 재생 횟수와 고유번호를 함께 관리한 것이 효율적입니다.

- **명확한 단계별 처리**: 문제를 논리적인 단계로 나누어 구현했습니다 (데이터 그룹화 → 정렬 → 장르별 정렬 → 결과 추출). 각 단계가 주석으로 잘 설명되어 있어 코드의 의도를 쉽게 파악할 수 있습니다.

- **엣지 케이스 고려**: `min(2, len(...))`을 사용하여 장르에 노래가 1개만 있는 경우를 적절히 처리했습니다.

### 2. 개선할 점

- **불필요한 중간 정렬**: 현재 코드는 `genre_to_songs_dict`의 각 리스트를 먼저 정렬한 후, `genre_to_total_plays_dict`를 다시 정렬합니다. 이 두 작업을 하나의 루프에서 분리할 필요가 없어 코드가 다소 복잡해 보입니다.

- **정렬 기준 불완전**: 문제 조건 3번 "재생 횟수가 같은 경우 고유번호가 낮은 노래를 먼저 수록"을 처리하지 않았습니다. 현재는 재생 횟수로만 정렬하므로, 재생 횟수가 같을 때 고유번호 순서가 보장되지 않습니다.

- **변수명 개선 가능**: `play_list`, `genre_sorted_list` 등의 이름을 더 명확하게 할 수 있습니다. 예: `songs`, `sorted_genres`

### 3. 개선한 버전 예시

```python
from collections import defaultdict

def solution(genres, plays):
    # 장르별 노래 정보와 총 재생 횟수를 동시에 수집
    genre_info = defaultdict(lambda: {'songs': [], 'total': 0})
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_info[genre]['songs'].append((play, index))
        genre_info[genre]['total'] += play
    
    # 장르를 총 재생 횟수 기준으로 내림차순 정렬
    sorted_genres = sorted(genre_info.items(), key=lambda x: x[1]['total'], reverse=True)
    
    result = []
    for genre, info in sorted_genres:
        # 각 장르 내에서 노래를 정렬
        # 1순위: 재생 횟수 내림차순, 2순위: 고유번호 오름차순
        sorted_songs = sorted(info['songs'], key=lambda x: (-x[0], x[1]))
        
        # 상위 최대 2곡 선택
        for play, index in sorted_songs[:2]:
            result.append(index)
    
    return result
```

**주요 개선사항:**

1. **통합된 데이터 구조**: 장르별 노래 리스트와 총 재생 횟수를 하나의 딕셔너리에 함께 저장하여 코드가 더 간결해졌습니다.

2. **정확한 정렬 기준**: `key=lambda x: (-x[0], x[1])`을 사용하여 재생 횟수는 내림차순(-x[0]), 고유번호는 오름차순(x[1])으로 정렬합니다. 이제 문제의 모든 조건을 만족합니다.

3. **리스트 슬라이싱 활용**: `sorted_songs[:2]`를 사용하여 상위 2곡을 더 파이썬답게 추출했습니다. `min()` 함수 없이도 리스트가 2개 미만일 때 자동으로 처리됩니다.