# [광고](https://www.acmicpc.net/problem/1305)

## input
첫째 줄에 광고판의 크기 L이 주어지고, 둘째 줄에 현재 광고판에 보이는 문자열이 주어진다.

## output
첫째 줄에 가능한 광고의 길이중 가장 짧은 것의 길이를 출력한다.

## precode
1. LPS(Longest Proper Prefix which is also Suffix)를 이용한 KMP 알고리즘을 이용하여 시간복잡도를 줄인다.
2. LPS를 구하는 함수를 구현한다.
3. LPS를 이용하여 KMP 알고리즘을 구현한다.
4. KMP 알고리즘을 이용하여 광고의 길이를 구한다.
5. 광고의 길이를 출력한다.


* 자료구조
    - list
* 알고리즘
    - KMP 
        - 문자열에서 반복되는 패턴을 제거하고 최소 광고판 길이를 구하려면 접두사(prefix)와 접미사(suffix)가 일치하는 최대 길이를 찾아야 합니다.
        - LPS 배열의 마지막 값 LPS[−1]은 문자열의 접두사와 접미사가 일치하는 가장 긴 길이를 나타냅니다.
        - 전체 문자열 길이 L에서 LPS[−1]을 빼면, 반복되는 패턴을 제거한 최소 길이를 구할 수 있습니다.

       

* 시간 복잡도
* 참고자료
- [KMP 알고리즘](https://bowbowbow.tistory.com/6)
- [KMP 알고리즘](https://woo-niverse.tistory.com/230)
