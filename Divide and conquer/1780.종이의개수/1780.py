def count_paper(paper, x, y, size):
    # 3. 모두가 같은 경우가 있는지 계산한다. 같다면 해당 숫자를 카운트 한다.(size만큼 x,y를 하나씩 이동하여 전부확인)
    initial = paper[y][x]
    all_same = True
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != initial:
                all_same = False
                break
        if not all_same:
            break
    # 4. 모두가 같은 경우가 있는게 아니라면 3^(n-1)로 자르고, 해당 값이 동일하면 해당 숫자 카운트 1 증가하고, 또 아니라면, 3^(n-1)으로 반복적으로 분할하여 카운트 한다.
    if all_same:
        if initial == -1:
            counts[0] += 1
        elif initial == 0:
            counts[1] += 1
        else:
            counts[2] += 1
    else:
        new_size = size // 3
        for dy in range(3):
            for dx in range(3):
                count_paper(paper, x + dx * new_size, y + dy * new_size, new_size)


if __name__ == "__main__":
    # 1. N의 값을 입력받아, N*N 행렬을 만든다

    N = int(input())
    paper = [[0] * N for _ in range(N)]

    # 2. N*N의 값을 한 라인씩 입력받아 list에 삽입한다.
    for y in range(N):
        row = list(map(int, input().split()))
        for x in range(N):
            paper[y][x] = row[x]

    counts = [0, 0, 0]
    count_paper(paper, 0, 0, N)
    print(counts[0])
    print(counts[1])
    print(counts[2])
