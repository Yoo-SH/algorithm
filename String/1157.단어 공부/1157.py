if __name__ == "__main__":
    # 1. 입력갑을 받아 리스트로 문자 하나씩 저장한다.
    input_alphabets_list = list(input())
    alphabets : dict = { }

    # 2. 대문자 알파벳 A,B,C....Z까지 딕셔너리에 {알파벳:개수}로 저장한다
    ## ord는 유니코드를 반환.
    for char in range(ord('A'), ord('Z') + 1): 
        alphabets[chr(char)] = 0 


    # 3. 입렵값을 세면서 딕셔너리의 값을 증가시킨다.
    for char in input_alphabets_list:
        char = char.upper()
        alphabets[char] += 1

    # 4. 딕셔너리를 순회하면서 가장 큰 값을 추출하고, 해당 큰 값을 2개 이상 가지고 있으면 ? 를 출력한다.
    maxNum = max(alphabets.values())
    maxAlphas = [key for key, value in alphabets.items() if value == maxNum]

    if len(maxAlphas) > 1:
        print("?")
    else:
        print(maxAlphas[0])
