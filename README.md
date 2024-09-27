# 알고리즘 문제풀이 태도

## 1. `기록하기`

문제를 푸는 과정에서 무엇이든 많이 기록해야한다. 모든 문제는 완벽하게 풀 수 없다. 하지만 중간까지는 갈수 있다. 

문제를 보고 어떤 알고리즘을 적용하려고 했는지, 근거는 무엇인지, 문제를 푸는 과정에서 내가 떠올린 알고리즘을 어떻게 코드로 만들려 했는지 등을 기록할 수 있다. 

이렇게하면 정답까지는 가지 못할지언정 나중에 답안을 보면서 나의 기록과 비교하며 더 효율적으로 공부할 수 잇다. 답안 코드와 내 기록이 다르다면 어디가 다른지 확인하며 복기할 수있다. 또한 , 복기하며 비교하면 무엇을 모르는지 명확하게 알 수 있어 이후 공부에 좋은 영향을 줄 수 있다.

## 2. `시험보듯 공부하기`

주기적으로 자체 시험을 보면 좋은 결과를 얻을 수 있다. 우선 시간에 대한 이야기를 하면, 시험을 준비하는 과정에서 시간을 간과하는 경우가 굉장히 많다. 하지만, 시험이란 것은 주어진 시간을 효율적으로 사용하여 최대의 점수를 내는 것이 목표이다. 

그러니, 평소 시간 배분 전략을 미리 연습한 사람과 그렇지 않은 사람은 결과가 많이 다를 것이다. 또한, 긴장도 훈련할 수 있다. 어떤 사람은 시험 떄 긴장을 너무 많이 해서 그르치는 경우가 있지만, 평소에 긴장감을 연습한다면 연습하지 않았을 때보다 더 좋은 결과를 얻을 수 있을 것이다.

## 3. `요약하기`
인간의 뇌는 굉장히 긍정적이다. 남이 작성한 글을 보고 내가 이해했다고 착각하기 쉽다. 정말 이해했는지 확인하는 방법은 이해한 내용을 요약해보는 것이다.

만약, 요약을 잘할 수 있다면 실제 문제를 풀 때도 이해한 내용이 쉽게 떠오를 것이다. 내가 공부한 개념을 나만의 언어로 요약하는 것에 초점을 맞춰라.


## 4. `짧은 시간 공부해서 절대 코딩 테스트를 통과할 수 없다`
코딩 테스트를 준비하는 분들에게 코딩테스트는 '최소한' 한 달에서  두 달 정도를 매우 집중해서 공부해야한다.


# 알고리즘 문제 분석 연습하기

## 1. `문제를 쪼개서 분석하기`
문제 전체를 분석하는 것보다 문제를 좀더 '동작단위로 쪼개서 분석'하는 것이 유리하다. 한번에 생각하는 양을 줄이면 문제에 좀 더 유연하게 접근할 수 있다..

## 2. `제약사항을 파악하고 테스트 케이스를 추가`
문제에는 제약사항이 존재한다. 제학 사항을 정리해두고 이를 고려해서 테스트 케이스를 추가하는 연습을 하는게 좋다.

 이 과정은 어떤 알고리즘을 사용할지 고민할 때 유용하고, 추후 코드를 구현하는 단계에서 예외를 거를 때 도움이 된다.

 ## 3. `입력값을 분석하라`
 보통 알고리즘의 시간 복잡도는 입력값이 결정하는 경우가 많다. 입력값의 크기를 확인하면 문제를 제한 시간 내에 풀 수 있는 알고리즘과 그렇지 않은 알고리즘을 미리 걸러낼 수 있다. 그러니 구현전에는 시간복잡도와 상황을 고려하여라.

 ## 4. `핵십키워드를 파악하라`
문제의 핵심 키워드가 A이면 무조건 a알고리즘을 적용하라는 것은 아니지만, 핵심 키워드는 곧 특정 알고리즘을 암시하는 경우가 많고, 핵심 키워드를 파악하면 좀 더 빠르게 문제를 파악하고 좋은 알고리즘을 선택해 코드를 작성할 수 있으므로 연습해둬도 좋다.

|알고리즘|키워드|상황 |
|:---:|:---:|---|
|스택|"쌍이 맞는지", "최근"| 무언가를 저장 or 반대로 처리|
|큐|"순서대로", "스케줄링", "~대로 동작하는 경우"| 시작 지점부터 목표 지점까지 최단거리
|깊이 우선 탐색|"모든경로"|백트래킹 문제 풀 때, 메모리 사용량 제한적일 떄
|너비 우선 탐색|"최적", "레벨 순회", "최소 단계" | 최단 경로나 최소 횟수를 찾을 때
|백트래킹| "조합", "순열", "부분집합"| 조합 및 순열 문제, 특정조건을 만족하는 부분집합|
|최단 경로| "최소시간", "최소비용", "트래픽", "단일 출발점 경로"| 다익스트라: 특정지점에서 나머지 지점까지 가는 최단 경로, 벨만 포트: 음의 가중치를 가진 그래프에서 최단경로|



## 5. `데이터 흐름이나 구성을 파악하라`
데이터 흐름이나 구성을 파악하는 것도 중요. 만약 데이터의 삽입과 삭제가 빈번하게 일어날 거 같으면 힙 자료구조를 고려하는게 좋고, 입력 데이터가 50개 미만이고 입력값을 깔끔하게 정리하기 어렵다면 하드 코딩을 고려하기 한다. 또또 데이터 간의 격차가 크면 데이터값 자체를 인덱스로 피하는 게 좋다. 


# 의사코드로 설계하기.

## 1. `세부 구현이 아닌 동작 중심으로 작성`
의사 코드를 구현할 때 세부 구현을 고민하는 사람이 많다. 하지만 세부 구현을 고민하는 순간부터 의사코드는 설계가 아닌 구현이 주 목표가 된다. 이러면 의사 코드를 작성하는 장점이 사라진다. 

## 2. `문제 해결 순서로 작성하라`
의사 코드가 완성되면 이를 토대로 코드를 구현할 것이므로 의사 코드는 문제 해결 순서대로 작성해야 한다. 또 의사코 코드 자체는 실제 구현할 코드의 주석이 되기도 하므로 이렇게 순서대로 작성하면 나중에 자신의 코드를 코드를 분석하기도 상당히 용이하다.

## 3. `충분히 테스트 해라.`
구현단계로 갈수록 잘못된 부분을 수정하는데 드는 비용은 점차 커지므로 의사 코드가 미리 생각해본 테스트 케이스를 통과할 수 있을지를 고민해봐야한다. 이후, 코드가 대부분의 테스트 케이스를 통과할 수 있을 것 같을 떄 구현을 시작하면 된다.