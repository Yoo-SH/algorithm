if __name__ == "__main__":
    strings = input().strip()  # 문자열 앞뒤 공백 제거 
    words = strings.split()  #공백(스페이스, 탭, 줄 바꿈 등 모든 공백 문자)을 기준으로 문자열을 분리
    word_num = len(words)  # 단어의 개수 계산
    print(word_num)


    