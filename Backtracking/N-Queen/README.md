# [N-Queen](https://www.acmicpc.net/problem/9663)

## input
첫째 줄에 N이 주어진다. (1 ≤ N < 15)
## output
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
## precode
1. N값을 입력받아 N*N의 체스판을 list에 배치한다.
2. [0,0지점을] 루트노드로 탐색을 시작하고, [1,0] [1,n] 까지 순차적으로 놓을 수 있는 경우를 체크한다. 
    - 조건은 대각선 불가.(x2-x1) = |y2-y1| 
3. 다음 row에서 놓을 수 있는 경우가 없는 경우, 이전 row 백트래킹 후, 다음 놓을 수 있는 경우를 다시 체크하고, 놓을 수 있는 경우 순차적으로 진행한다.
4. n개의 퀸을 전부 배치하면 경우의 수를 1개 증가한다.
5. n개의 퀸을 배치하면 이전으로 다시 백트래킹하여 경우의 수를 구하는 경우를 반복한다.

## 특이사항
1. 시간 복잡도를 줄이기 위해  promising 단계에서 모든 대각선을 검사하는 것이 아니라, 왼쪽 대각선만 검사하고 각 한 칸씩만 검사한다.

* 자료구조
    - list
* 알고리즘
    - 백트래킹
        - 브루트 포스로 진행하면 입력값이 최대 15이므로 최악의 경우 15^15가 됨. promising(체크)+pruning(가지차기)로 시간을 단축해야함.
    
* 참고자료 
    - [[알고리즘] 백트래킹(backtracking) 알아보기(& N-Queen 문제 풀이)](https://kang-james.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9backtracking-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-N-Queen-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4#google_vignette)