#문제
https://litmus.jbnu.ac.kr/problem/11713

# 내 풀이(24.09.30) 
# 왜 이걸로 해야하는지??!?!?!?!?!? 를 생각해보기.
리스트값을 인자로 받음.

매직스퀘어 초기상태 
(1,2,3,4)
(5,6,7,8)

그리고, input_list 갯수에 따라서 2줄로 나눠서 할당받기
딕셔너리를 인자로 받는 클래스를 이용하여 매직스퀘어를 만들기

트리를 A,B,C,D 가지로 지속적으로 만들면서 
A,B,C,D 경로에 따라 결과값을 만들면서 목표값과 비교하고, 해당 목표값에 동일하게 되면 카운트 종료.

A,B,C,D 들어가서도 일관적으로 처리해야함.
# JBNU
모델링 문제

1.문제를 이해하고, 모델링을 해야함.
    - input값과 output값을 이해하고, 어떻게 모델링을 할지 생각하기
    - 어떤 알고리즘으로 풀지 생각 + 어떤 자료구조로 풀지 생각

2.최소동작 횟수를 찾아야함.(그래프 + BFS로 찾기 + 백트래킹-가지치기)
    - 그래프로 모델링을 하고, BFS로 최소동작횟수를 찾기
    - 백트래킹을 이용하여, 가지치기를 하면서 최소동작횟수를 찾기

3. 어떻게? 노드 하나 단위로 생각하기
    - 노드 하나 단위로 생각하고, 어떻게 최소동작횟수를 찾을지 생각하기

4. if문으로 제약조건을 많이 걸고있다면, 올바른 알고리즘을 사용하지 않고 있을 가능성이 높음.
    - if문을 최소화하고, 올바른 알고리즘을 사용하는지 생각하기