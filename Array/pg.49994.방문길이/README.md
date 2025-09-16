# [방문길이](https://school.programmers.co.kr/learn/courses/30/lessons/49994)


## input
제한시간: 없음
데이터 크기: 500이하 

## 설계
1. 지나온 길을 set에 저장하여 지나온 길의 여부를 확인한다.
2. up, down, left, right에 따른 좌표 변화에 따라 좌표를 이동한다.(좌표 이동할 때 범위를 벗어나지 않도록 유효성 검사를한다.)
3. set에 (현재 좌표, 이동한 좌표), (이동한 좌표, 현재 좌표)를 추가한다.
4. set을 통해 UPsert를 한다.(없으면 추가하고 길이 증가하고, 있으면 추가하지 않고 길이 증가하지 않는다.)

## 활용 스킬 및 시간 복잡도

- 자료구조 : set


## 코드 비교
### 나의 풀이
```python
def is_valid_pos(x, y):
    if x >= -5 and x <= 5 and y >= -5 and y <= 5:
        return True
    else:
        return False


def solution(dirs):

    pass_road = set()
    x, y = 0, 0  # 현재 위치
    pass_road_count = 0  # 지나온 길 카운트

    for direction in dirs:
        dx, dy = 0, 0
        if direction == "U":
            dy += 1
        elif direction == "R":
            dx += 1
        elif direction == "L":
            dx -= 1
        elif direction == "D":
            dy -= 1

        if is_valid_pos(x + dx, y + dy) == False:  # 유효한 길인지 검사
            print("유효한 길이 아님")
            pass
        elif ((x, y), (x + dx, y + dy)) in pass_road:  # 이미 지나온 길인지 검사
            print("이미 지나온 길입니다.")
            x += dx  # x좌표 이동
            y += dy  # y좌표 이동
            pass
        else:
            pass_road.add(((x, y), (x + dx, y + dy)))  # (현재 좌표, 이동한 좌표) 추가
            print(f"x:{x} y:{y} 에서 {x+dx}, {y+dy}로 이동")
            pass_road.add(((x + dx, y + dy), (x, y)))  # (이동한 좌표. 현재 좌표) 추가
            pass_road_count += 1
            x += dx  # x좌표 이동
            y += dy  # y좌표 이동

    answer = pass_road_count
    return answer
```

### 우수 풀이
```python
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2

```
## AI 피드백

## 📝 문제 정보
**문제 제목:** 방문 길이  
**출처:** 프로그래머스  
**난이도:** Level 2  
**문제 요약:** 캐릭터가 좌표평면에서 이동하며 **처음 걸어본 길의 길이**를 구하는 문제  
**주요 제약사항:** 좌표평면 범위 -5~5, 범위를 벗어나는 명령은 무시

## 🔍 핵심 차이점 분석

**1. 알고리즘 접근 방식**
- **내 접근법:** 별도 함수로 유효성 검사, 상세한 디버깅 출력, 카운터 변수 사용
- **우수 접근법:** 딕셔너리로 방향 벡터화, 조건부 내장, set 크기 활용

**2. 효율성 차이**
- **내 코드 문제점:**
  - `is_valid_pos` 함수 불필요 (인라인 처리 가능)
  - `pass_road_count` 변수 불필요 (set 크기로 계산 가능)
  - 디버그 print문들이 성능 저하
  
**3. 파이썬다움(Pythonic) 비교**
```python
# Before: 장황한 조건문
if direction == "U":
    dy += 1
elif direction == "R":
    dx += 1
# ...

# After: 딕셔너리 활용
d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
nx, ny = x + d[i][0], y + d[i][1]
```

## ⚡ 즉시 개선 팁

1. **방향 벡터 딕셔너리 활용** - 조건문 대신 딕셔너리로 방향 처리
2. **중복 제거** - 별도 카운터 대신 `len(s)//2` 활용  
3. **함수 분할 재검토** - 간단한 로직은 인라인으로 처리
4. **디버그 코드 제거** - 제출 전 print문 정리

