
if __name__ == "__main__":
    
    divisor_count = int(input())
    divisors = list(map(int, input().split()))
    divisors.sort() #오름차순 정렬
    N : int = divisors[0] * divisors[-1] #가장 작은 약수와 가장 큰 약수의 곱이 N이다.
    print(N)
    
    

    

