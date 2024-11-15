import math

def count_coprime_triplets(N : int) -> int:
    count = 0
    for A in range(2, N + 1):
        for B in range(A, N + 1):
            for C in range(B, N + 1):
                # A, B, C가 서로수인지 확인
                print(A, B, C)
                if math.gcd(A, B) == 1 and math.gcd(B, C) == 1 and math.gcd(A, C) == 1:
                    count += 1
                    
    return count

# 예제 입력
n = input("N: ") # type: ignore
n = int(n)
# 결과 출력
print(count_coprime_triplets(n))  

